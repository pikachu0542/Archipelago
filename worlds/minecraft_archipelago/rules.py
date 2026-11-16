from collections import defaultdict
from collections.abc import Mapping
from enum import Enum

from rule_builder.options import OptionFilter
from rule_builder.rules import And, CanReachEntrance, Has, HasAll, HasAllCounts, HasAny, HasGroup, Or, Rule, True_
from worlds.generic.Rules import set_rule
from typing import TYPE_CHECKING

from worlds.minecraft_archipelago.options import ChestLootLogic, DaylightCycle, EnderDragonRequiredArmor, OuterEndAccessLogic, PhantomSpawning, Raids, RequiredBossKills, RequiredLootableChecks, StrongholdAccessLogic, WardenSpawning, WeatherCycle

if TYPE_CHECKING:
    from . import MinecraftArchipelagoWorld

# Define enum for tool tier levels
class Tools(Enum):
    """
        Integer values for each of the possible tool tiers
    """
    WOOD = 0
    STONE = 1
    GOLD = 2
    IRON = 3
    DIAMOND = 4
    NETHERITE = 5

# Define enum for armor tier levels
class Armor(Enum):
    """
        Integer values for each of the possible armor tiers
    """
    NONE = 0
    LEATHER = 1
    GOLD = 2
    CHAINMAIL = 3
    IRON = 4
    DIAMOND = 5
    NETHERITE = 6

def can_kill_dragon(world: "MinecraftArchipelagoWorld"):
    """
    Checks if the player has unlocked the items needed to access the End.
    """

    return And(
        CanReachEntrance("Overworld -> The End"),
        HasAllCounts({
        "Eye of Ender": 1,
        "Progressive Armor": world.options.ender_dragon_required_armor.value,
        "Progressive Tools": world.options.ender_dragon_required_tools.value,
    }))

def can_kill_wither(world: "MinecraftArchipelagoWorld"):
    """
    Checks if the player has unlocked the items needed to access the Nether.
    """
    return And(
        CanReachEntrance("Overworld -> Nether"),
        HasAllCounts({
        "Flint and Steel": 1,
        "Progressive Armor": world.options.wither_required_armor.value,
        "Progressive Tools": world.options.wither_required_tools.value,
    }))

def can_kill_warden(world: "MinecraftArchipelagoWorld"):
    """
        Checks if the player has unlocked all the items needed to kill the Warden
    """
    return (
        OptionFilter(WardenSpawning, True) & Has("WardenSpawning"),
        HasAllCounts({
            "Progressive Armor": world.options.warden_required_armor.value,
            "Progressive Tools": world.options.warden_required_tools.value,
        })
    )

def can_kill_elder_guardian(world: "MinecraftArchipelagoWorld"):
    """
        Checks if the player has unlocked all the items needed to kill the Elder Guardian
    """
    return HasAllCounts({
        "Progressive Armor": world.options.elder_guardian_required_armor.value,
        "Progressive Tools": world.options.elder_guardian_required_tools.value,
    })

def can_defeat_raid(world: "MinecraftArchipelagoWorld"):
    """
        Checks if the player has unlocked all the items needed to defeat a raid
    """
    return And(
        OptionFilter(Raids, 1) & Has("Raids"),
        HasAllCounts({
            "Progressive Armor": world.options.raid_required_armor.value,
            "Progressive Tools": world.options.raid_required_tools.value,
        })
    )

def can_fight_trial_chamber(world: "MinecraftArchipelagoWorld"):
    """
        Checks if the player has unlocked all the items needed to take on trial chambers
    """
    return HasAllCounts({
        "Progressive Armor": world.options.trial_chamber_required_armor.value,
        "Progressive Tools": world.options.trial_chamber_required_tools.value,
    })

def set_rules(world: "MinecraftArchipelagoWorld") -> None:
    entrance_rules: defaultdict[str, Rule] = defaultdict(True_)
    location_rules: defaultdict[str, Rule] = defaultdict(True_)
    
    world.set_completion_rule(
        (OptionFilter(RequiredBossKills, RequiredBossKills.ender_dragon, "contains") & Has("Ender Dragon Kill")) &
        (OptionFilter(RequiredBossKills, RequiredBossKills.wither, "contains") & Has("Wither Kill")) &
        (OptionFilter(RequiredBossKills, RequiredBossKills.elder_guardian, "contains") & Has("Elder Guardian Kill")) &
        (OptionFilter(RequiredBossKills, RequiredBossKills.warden, "contains") & Has("Warden Kill")) &
        (OptionFilter(RequiredLootableChecks, 0, "ne") & HasGroup("Lootable Checks", world.options.required_lootable_checks.value))
    )
            
    # ── Region entrance rules ─────────────────────────────────────────────
    # These are the most important — they stop the generator softlocking
    # by hiding required items behind regions you can't access yet.

    entrance_rules["Overworld -> Nether"] = Has("Flint and Steel")
    entrance_rules["Overworld -> The End"] = HasAll("Flint and Steel", "Eye of Ender")

    # ── Story Advancements ─────────────────────────────────────────────────────────────
    
    location_rules["Getting an Upgrade"] = HasAllCounts({"Progressive Tools": Tools.STONE})

    location_rules["Acquire Hardware"] = OptionFilter(ChestLootLogic, 0) & HasAllCounts({
        "Progressive Tools": Tools.STONE,
        "Furnace": 1
    })

    location_rules["Suit Up"]  = OptionFilter(ChestLootLogic, 0) & HasAllCounts({
        "Progressive Tools": Tools.STONE,
        "Progressive Armor": Armor.IRON,
        "Furnace": 1
    })

    location_rules["Hot Stuff"] = Has("Bucket")

    location_rules["Isn't It Iron Pick"]  = OptionFilter(ChestLootLogic, 0) & HasAllCounts({
        "Progressive Tools": Tools.IRON,
        "Furnace": 1
    })

    location_rules["Not Today, Thank You"] = Has("Shield")

    location_rules["Ice Bucket Challenge"] = OptionFilter(ChestLootLogic, 0) & HasAllCounts({
        "Progressive Tools": Tools.DIAMOND
    }),

    location_rules["Diamonds!"] = OptionFilter(ChestLootLogic, 0) & HasAllCounts({
        "Progressive Tools": Tools.IRON
    })

    location_rules["We Need to Go Deeper"] = Has("Flint and Steel")

    location_rules["Cover Me with Diamonds"] = OptionFilter(ChestLootLogic, 0) & HasAllCounts({
        "Progressive Armor": Armor.DIAMOND
    })

    location_rules["Enchanter"] = Has("Enchanting Table")
    location_rules["Zombie Doctor"] = HasAll("Golden Apple", "Potion")
    location_rules["Eye Spy"] = OptionFilter(StrongholdAccessLogic, 1) & Has("Eye of Ender")
    location_rules["The End?"] = Has("Eye of Ender")

    # ── Nether (already gated by region, adding extra requirements) ───────

    location_rules["Hidden in the Depths"] = OptionFilter(ChestLootLogic, 0) & HasAllCounts({
        "Progressive Tools": Tools.DIAMOND
    })

    # TODO: Is warped fungus on a stick locked behind fishing rod

    location_rules["Cover Me in Debris"] = OptionFilter(ChestLootLogic, 0) & HasAllCounts({
        "Progressive Tools": Tools.DIAMOND,
        "Progressive Armor": Armor.NETHERITE,
        "Smithing Table": 1
    })

    location_rules["Not Quite 'Nine' Lives"] = Has("Respawn Anchor")
    location_rules["Withering Heights"] = can_kill_wither()
    location_rules["Local Brewery"] = Has("Brewing Stand")
    location_rules["Bring Home the Beacon"] = Has("Beacon") & can_kill_wither()
    location_rules["A Furious Cocktail"] = HasAll("Brewing Stand", "Potion")
    location_rules["Beaconator"] = Has("Beacon") & can_kill_wither()

    # Need all of the following:
    # - Armor and tools -> kill wither for beacon
    # - Beacon -> Haste
    # - Conduit -> Conduit Power
    # - Potion -> All potion effects
    # - Brewing Stand -> Brew all needed potions
    # - Ominous Bottle -> Bad Omen, Raid Omen, Trial Omen
    # - Warden Spawning (if randomized) -> Darkness
    location_rules["How Did We Get Here?"] = And(
        OptionFilter(WardenSpawning, 1) & Has("Warden Spawning"),
        HasAny("Bow", "Crossbow"),
        HasAllCounts({
            "Progressive Armor": max(world.options.wither_required_armor.value, world.options.raid_required_armor.value),
            "Progressive Tools": max(world.options.wither_required_tools.value, world.options.raid_required_tools.value),
            "Beacon": 1,
            "Conduit": 1,
            "Brewing Stand": 1,
            "Potion": 1,
            "Ominous Bottle": 1,
        })
    )
    
    # ── End (already gated by region, adding extra requirements) ───────
    location_rules["Free the End"] = can_kill_dragon()
    location_rules["The Next Generation"] = can_kill_dragon()
    location_rules["The City at the End of the Game"] = OptionFilter(OuterEndAccessLogic, 1) & can_kill_dragon()
    location_rules["Great View From Up Here"] = OptionFilter(OuterEndAccessLogic, 1) & can_kill_dragon()
    
    # ── Adventure ─────────────────────────────────────────────────────────

    # Dia pick and furnace to mine ancient debris for the netherite ingot in the recipe
    # Or just get one from bridge bastion chest
    location_rules["Country Lode, Take Me Home"] = And(
        OptionFilter(ChestLootLogic, 0) & HasAllCounts({
            "Progressive Tools": Tools.DIAMOND,
            "Furnace": 1
        }),
        Has("Lodestone")
    )

    location_rules["Is It a Bird"] = Has("Spyglass")

    # Only way to get armor trims is structure chests, 
    # so the chest loot logic option doesnt matter here
    location_rules["Crafting a New Look"] = Has("Smithing Table")
    location_rules["Ol' Betsy"] = Has("Crossbow")

    # Need both trident and lightning rod to do the advancement
    # Need enchanting table or anvil to get channeling on trident
    # Need weather cycle for thunder so channeling works
    location_rules["Surge Protector"] = And(
        HasAll("Trident", "Lightning Rod"),
        HasAny("Enchanting Table", "Anvil"),
        OptionFilter(WeatherCycle, 1) & Has("Weather Cycle")
    )

    location_rules["Sweet Dreams"] = OptionFilter(DaylightCycle, 1) & Has("Daylight Cycle")
    location_rules["Hero of the Village"] = can_defeat_raid()
    location_rules["Is It a Balloon?"] = CanReachEntrance("Overworld -> Nether") & Has("Spyglass")
    location_rules["A Throwaway Joke"] = Has("Trident")
    location_rules["Take Aim"] = HasAny("Bow", "Crossbow")
    
    # Need to kill every hostile mob, including bosses
    # only exception is the warden, which isnt required for this advancement
    location_rules["Monsters Hunted"] = And(
        CanReachEntrance("Overworld -> Nether"),
        CanReachEntrance("Overworld -> The End"),
        can_kill_dragon(),
        can_kill_wither(),
        can_kill_elder_guardian(),
        can_fight_trial_chamber(),
    )

    location_rules["Postmortal"] = Has("Totem of Undying")

    location_rules["Hired Help"] = And(
        OptionFilter(ChestLootLogic, 0) & HasAllCounts({
            "Progressive Tools": Tools.STONE,
            "Furnace": 1,
        }),          
        Has("Shears")
    )

    location_rules["Smithing With Style"] = And(
        OptionFilter(OuterEndAccessLogic, 1) & can_kill_dragon(),
        Has("Smithing Table")
    )

    location_rules["Two Birds, One Arrow"] = And(
        OptionFilter(PhantomSpawning, 1) & Has("Phantom Spawning"),
        Has("Crossbow"),
        HasAny("Enchanting Table", "Anvil")
    )

    location_rules["Who's the Pillager Now?"] = Has("Crossbow")
    location_rules["Arbalistic"] = Has("Crossbow") & HasAny("Enchanting Table", "Anvil")
    location_rules["Light as a Rabbit"] = HasAllCounts({"Progressive Armor": Armor.LEATHER})
    location_rules["Is It a Plane?"] = CanReachEntrance("Overworld -> The End") & Has("Spyglass")
    location_rules["Very Very Frightening"] = Has("Trident") & HasAny("Enchanting Table", "Anvil")
    location_rules["Sniper Duel"] = HasAny("Bow", "Crossbow")
    location_rules["Bullseye"] = Has("Target") & HasAny("Bow", "Crossbow")
    location_rules["Who Needs Rockets?"] = Has("Elytra") & can_fight_trial_chamber()
    location_rules["Under Lock and Key"] = can_fight_trial_chamber()
    location_rules["Revaulting"] = Has("Ominous Bottle") & can_fight_trial_chamber()
    location_rules["Blowback"] = can_fight_trial_chamber()
    location_rules["Over-Overkill"] = Has("Mace")

    # ── Husbandry ─────────────────────────────────────────────────────────
    
    location_rules["Bee Our Guest"] = Has("Campfire")
    location_rules["Whatever Floats Your Goat!"] = Has("Boat")
    location_rules["Fishy Business"] = Has("Fishing Rod")
    location_rules["Bukkit Bukkit"] = Has("Bucket")
    location_rules["Two By Two"] = CanReachEntrance("Overworld -> Nether")
    location_rules["Tactical Fishing"] = Has("Bucket")

    # Need outer end access for chorus fruit
    location_rules["A Balanced Diet"] = And(
        CanReachEntrance("Overworld -> The End"),
        OptionFilter(OuterEndAccessLogic, 1) & can_kill_dragon()
    )

    location_rules["Serious Dedication"] = And(
        CanReachEntrance("Overworld -> Nether"),
        OptionFilter(ChestLootLogic, 0) & HasAllCounts({
            "Progressive Tools": Tools.DIAMOND
        }),
        Has("Smithing Table")
    )

    location_rules["The Cutest Predator"] = Has("Bucket")
    location_rules["With Our Powers Combined!"] = CanReachEntrance("Overworld -> Nether")
    location_rules["Shear Brilliance"] = Has("Shears")

    # ── Boss kills ────────────────────────────────────────────────────────────
    location_rules["Ender Dragon Kill"] = can_kill_dragon()
    location_rules["Wither Kill"] = can_kill_wither()
    location_rules["Elder Guardian Kill"] = can_kill_elder_guardian()
    location_rules["Warden Kill"] = can_kill_warden()