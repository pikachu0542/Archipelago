from ast import Dict, List
from dataclasses import dataclass
from typing import Any
from Options import Choice, DefaultOnToggle, OptionGroup, Range, Toggle, DeathLink, PerGameCommonOptions, OptionSet

# ────────────────────────────────────────────────────────────────────────────
#                   Goal Options
# ────────────────────────────────────────────────────────────────────────────
class AdvancementGoal(Range):
    """
        Percentage of advancements required to meet the advancement win condition.
        Set to 0 to disable the advancement goal entirely.
        At least one win condition must be active.
    """
    display_name = "Advancement Goal"
    range_start = 0 # 0 = disbled
    range_end = 100
    default = 70

class LootableChecks(Range):
    """
        How many Archipelago Loot items are hidden in structure chests.
        Each one is a location check. 
        Set to 0 to disable lootable checks.
    """
    display_name = "Lootable Checks"
    range_start = 0
    range_end = 50
    default = 20


class RequiredLootableChecks(Range):
    """
        How many Archipelago Loot items must be claimed to meet the lootable
        checks win condition. Set to 0 to disable. Cannot exceed Lootable Checks.
    """
    display_name = "Required Lootable Checks"
    range_start  = 0
    range_end    = 50
    default      = 0


class RequiredBossKills(OptionSet):
    """
        Which bosses must be killed to satisfy the boss kill win condition.
        Leave empty to disable boss kills as a win condition entirely.
        Boss kill locations exist in the item pool regardless of this setting.

        Valid values: ender_dragon, wither, elder_guardian, warden
    """
    display_name = "Required Boss Kills"
    valid_keys = {"ender_dragon", "wither", "elder_guardian", "warden"}
    default = frozenset()

class RequiredItemCollections(OptionSet):
    """
        Which item collection sets must be completed as a win condition.
        Any combination can be selected. All selected collections must be
        completed to win. Leave empty to disable item collections as a win condition.

        Collections track items you have EVER held in your inventory.
        You do not need to hold them all simultaneously.

        Valid values:
        all_music_discs    - All 19 music discs
        all_armor_sets     - Full sets of all 7 armor materials (Leather, Chainmail, Iron, Gold, Diamond, Netherite, and Turtle Helmet: 25 pieces total)
        all_pottery_sherds - All 23 pottery sherds
        all_trims          - All 19 armor trim smithing templates (including the netherite upgrade template)
        rare_items         - 6 rare items: Mace, Elytra, Trident, Enchanted Golden Apple, Totem, Conduit
        all_flowers        - All 19 flower types
        all_heads          - All 6 mob heads
        all_dyes           - All 16 dyes
        all_weapons        - 6 weapon types: Diamond Sword, Bow, Crossbow, Trident, Mace, Shield
      """
    display_name = "Required Item Collections"
    valid_keys   = {
        "all_music_discs",
        "all_armor_sets",
        "all_pottery_sherds",
        "all_trims",
        "rare_items",
        "all_flowers",
        "all_heads",
        "all_dyes",
        "all_weapons",
    }
    default = frozenset()

# ────────────────────────────────────────────────────────────────────────────
#                   Gamerule Options
# ────────────────────────────────────────────────────────────────────────────

class DrowningDamage(Toggle):
    """
        Whether to add an item to the item pool that disables drowning damage.
    """

    display_name = "Randomize Drowning Damage"

class FireDamage(Toggle):
    """
        Whether to add an item to the item pool that disables fire damage.
    """

    display_name = "Randomize Fire Damage"

class FreezeDamage(Toggle):
    """
        Whether to add an item to the item pool that disables freeze damage.
    """

    display_name = "Randomize Freeze Damage"

class FallDamage(Toggle):
    """
        Whether to add an item to the item pool that disables fall damage.
    """

    display_name = "Randomize Fall Damage"

class KeepInventory(Toggle):
    """
        Whether to add an item to the item pool that enables the gamerule "keepInventory"
    """
    display_name = "Randomize Keep Inventory"


class NaturalRegeneration(Toggle):
    """
        Whether to add an item to the item pool that enables natural regeneration. 
        Enabling this option will make it so that until the item that enables it is received, 
        the only way to heal health is through the regeneration potion effect.

        WARNING: Enabling this option makes the game significantly more challenging. Proceed with caution.
    """
    display_name = "Randomize Natural Regeneration"

class Raids(Toggle):
    """
        Whether to add an item to the item pool that enables raids.
        Enabling this option will make it so that you cannot start raids until the item that enables it is received.
    """
    display_name = "Randomize Raids"

class MobGriefing(Toggle):
    """
        Whether to add an item to the item pool that disables mob griefing.
    """

    display_name = "Randomize Mob Griefing"

class PhantomSpawning(Toggle):
    """
    Whether to add an item to the item pool that enables phantom spawning.
    Enabling this option will make it so that phantoms cannot spawn until the item that enables it is received.
    """
    
    display_name = "Randomize Phantom Spawning"

class PillagerPatrolSpawning(Toggle):
    """
        Whether to add an item to the item pool that enables pillager patrol spawning.
        Enabling this option will make it so that pillager patrols cannot spawn until the item that enables it is received.
    """

    display_name = "Randomize Pillager Patrol Spawning"

class WanderingTraderSpawning(Toggle):
    """
        Whether to add an item to the item pool that enables wandering trader spawning.
        Enabling this option will make it so that wandering traders cannot spawn until the item that enables it is received.
    """

    display_name = "Randomize Wandering Trader Spawning"

class WardenSpawning(Toggle):
    """
        Whether to add an item to the item pool that enables warden spawning.
        Enabling this option will make it so that wardens cannot spawn until the item that enables it is received.
    """

    display_name = "Randomize Warden Spawning"

class DaylightCycle(Toggle):
    """
        Whether to add an item to the item pool that enables the daylight cycle.
        Enabling this option will make it so that it can never become nighttime until the item that enables it is received.
    """

    display_name = "Randomize Daylight Cycle"

class WeatherCycle(Toggle):
    """
        Whether to add an item to the item pool that enables the weather cycle.
        Enabling this option will make it so that it never rains or thunders until the item that enables it is received.
    """

    display_name = "Randomize Weather Cycle"

class LavaSourceConversion(Toggle):
    """
        Whether to add an item to the item pool that enables lava source conversion.
    """

    display_name = "Randomize Lava Source Conversion"

class WaterSourceConversion(Toggle):
    """
        Whether to add an item to the item pool that enables water source conversion.
        Enabling this option will make it so that water will not convert to source blocks until the item that enables it is received.
        This means that while this gamerule is disabled, infinite water sources do not exist.
    """

    display_name = "Randomize Water Source Conversion"

# ────────────────────────────────────────────────────────────────────────────
#                   Configurable Logic Options
# ────────────────────────────────────────────────────────────────────────────
class ChestLootLogic(DefaultOnToggle):
    """
        Controls whether the possible loot from structure chests should be considered when setting logic rules.
        Enabling this option will put significantly more locations in-logic early in progression, which can lead to more exploration being required to progress.
    """
    display_name = "Consider Chest Loot when Setting Logic Rules"

class StrongholdAccessLogic(DefaultOnToggle):
    """
        Whether eyes of ender are logically required to find the stronghold.
        It is technically possible to find a stronghold without eyes of ender,
        but it is extremely rare and luck based, as you would have to randomly find it while exploring.
    """
    display_name = "Require Eyes of Ender to Find Stronghold"

class OuterEndAccessLogic(DefaultOnToggle):
    """
        Whether defeating the Ender Dragon is logically required to access the outer end
    """
    display_name = "Require Defeating Ender Dragon to Access Outer End"

class EnderDragonRequiredArmor(Choice):
    """
        Controls what armor tier is logically required to be able to fight the ender dragon.

        Valid values: None, Leather, Gold, Chainmail, Iron, Diamond, Netherite
    """

    display_name = "Required Armor Tier for Ender Dragon"

    option_none = 0
    option_leather = 1
    option_gold = 2
    option_chainmail = 3
    option_iron = 4
    option_diamond = 5
    option_netherite = 6

    default = 0

class EnderDragonRequiredTools(Choice):
    """
        Controls what tool tier is logically required to be able to fight the ender dragon.

        Valid values: None, Stone, Gold, Iron, Diamond, Netherite
    """

    display_name = "Required Tool Tier for Ender Dragon"

    option_none = 0
    option_stone = 1
    option_gold = 2
    option_iron = 3
    option_diamond = 4
    option_netherite = 5

    default = 0

class WitherRequiredArmor(Choice):
    """
        Controls what armor tier is logically required to be able to fight the wither.

        Valid values: None, Leather, Gold, Chainmail, Iron, Diamond, Netherite
    """

    display_name = "Required Armor Tier for Wither"

    option_none = 0
    option_leather = 1
    option_gold = 2
    option_chainmail = 3
    option_iron = 4
    option_diamond = 5
    option_netherite = 6

    default = 0

class WitherRequiredTools(Choice):
    """
        Controls what tool tier is logically required to be able to fight the wither.

        Valid values: None, Stone, Gold, Iron, Diamond, Netherite
    """

    display_name = "Required Tool Tier for Wither"

    option_none = 0
    option_stone = 1
    option_gold = 2
    option_iron = 3
    option_diamond = 4
    option_netherite = 5

    default = 0

class ElderGuardianRequiredArmor(Choice):
    """
        Controls what armor tier is logically required to be able to fight the elder guardian.

        Valid values: None, Leather, Gold, Chainmail, Iron, Diamond, Netherite
    """

    display_name = "Required Armor Tier for Elder Guardian"

    option_none = 0
    option_leather = 1
    option_gold = 2
    option_chainmail = 3
    option_iron = 4
    option_diamond = 5
    option_netherite = 6

    default = 0

class ElderGuardianRequiredTools(Choice):
    """
        Controls what tool tier is logically required to be able to fight the elder guardian.

        Valid values: None, Stone, Gold, Iron, Diamond, Netherite
    """

    display_name = "Required Tool Tier for Elder Guardian"

    option_none = 0
    option_stone = 1
    option_gold = 2
    option_iron = 3
    option_diamond = 4
    option_netherite = 5

    default = 0

class WardenRequiredArmor(Choice):
    """
        Controls what armor tier is logically required to be able to fight the warden.

        Valid values: None, Leather, Gold, Chainmail, Iron, Diamond, Netherite
    """

    display_name = "Required Armor Tier for Warden"

    option_none = 0
    option_leather = 1
    option_gold = 2
    option_chainmail = 3
    option_iron = 4
    option_diamond = 5
    option_netherite = 6

    default = 0

class WardenRequiredTools(Choice):
    """
        Controls what tool tier is logically required to be able to fight the warden.

        Valid values: None, Stone, Gold, Iron, Diamond, Netherite
    """

    display_name = "Required Tool Tier for Warden"

    option_none = 0
    option_stone = 1
    option_gold = 2
    option_iron = 3
    option_diamond = 4
    option_netherite = 5

    default = 0

class RaidRequiredArmor(Choice):
    """
        Controls what armor tier is logically required to be able to take on raids.

        Valid values: None, Leather, Gold, Chainmail, Iron, Diamond, Netherite
    """

    display_name = "Required Armor Tier for Raids"

    option_none = 0
    option_leather = 1
    option_gold = 2
    option_chainmail = 3
    option_iron = 4
    option_diamond = 5
    option_netherite = 6

    default = 0

class RaidRequiredTools(Choice):
    """
        Controls what tool tier is logically required to be able to take on raids.

        Valid values: None, Stone, Gold, Iron, Diamond, Netherite
    """

    display_name = "Required Tool Tier for Raids"

    option_none = 0
    option_stone = 1
    option_gold = 2
    option_iron = 3
    option_diamond = 4
    option_netherite = 5

    default = 0

class TrialChamberRequiredArmor(Choice):
    """
        Controls what armor tier is logically required to be able to take on trial chambers.

        Valid values: None, Leather, Gold, Chainmail, Iron, Diamond, Netherite
    """

    display_name = "Required Armor Tier for Trial Chamber"

    option_none = 0
    option_leather = 1
    option_gold = 2
    option_chainmail = 3
    option_iron = 4
    option_diamond = 5
    option_netherite = 6

    default = 0

class TrialChamberRequiredTools(Choice):
    """
        Controls what tool tier is logically required to be able to take on trial chambers.

        Valid values: None, Stone, Gold, Iron, Diamond, Netherite
    """

    display_name = "Required Tool Tier for Trial Chambers"

    option_none = 0
    option_stone = 1
    option_gold = 2
    option_iron = 3
    option_diamond = 4
    option_netherite = 5

    default = 0

# ────────────────────────────────────────────────────────────────────────────
#                   DeathLink Options
# ────────────────────────────────────────────────────────────────────────────
class DeathLink(DeathLink):
    """
        When you die, everyone dies. Of course the reverse is true too.
        Enable this if you want to share the pain with other players.
    """
    default = 0 # off by default

# Dictionary that defines the option groups for the APWorld
minecraft_option_groups = [
    OptionGroup("Goal Options", [
        AdvancementGoal, 
        LootableChecks,
        RequiredLootableChecks, 
        RequiredBossKills, 
        RequiredItemCollections
    ]),
    OptionGroup("Gamerule Options", [
        DrowningDamage,
        FireDamage,
        FreezeDamage,
        FallDamage,
        KeepInventory,
        NaturalRegeneration,
        Raids,
        MobGriefing,
        PhantomSpawning,
        PillagerPatrolSpawning,
        WanderingTraderSpawning,
        WardenSpawning,
        DaylightCycle,
        WeatherCycle,
        LavaSourceConversion,
        WaterSourceConversion
    ]),
    OptionGroup("Logic Options", [
        ChestLootLogic,
        StrongholdAccessLogic,
        OuterEndAccessLogic,
        EnderDragonRequiredArmor,
        EnderDragonRequiredTools,
        WitherRequiredArmor,
        WitherRequiredTools,
        ElderGuardianRequiredArmor,
        ElderGuardianRequiredTools,
        WardenRequiredArmor,
        WardenRequiredTools,
        RaidRequiredArmor,
        RaidRequiredTools,
        TrialChamberRequiredArmor,
        TrialChamberRequiredTools
    ]),
]

# ────────────────────────────────────────────────────────────────────────────
#                   Options Initialization
# ────────────────────────────────────────────────────────────────────────────
@dataclass
class MinecraftArchipelagoOptions(PerGameCommonOptions):
    death_link: DeathLink

    # ──────── Goal options ─────────────────────────────────
    advancement_goal: AdvancementGoal
    lootable_checks: LootableChecks
    required_lootable_checks: RequiredLootableChecks
    required_boss_kills: RequiredBossKills
    required_item_collections: RequiredItemCollections

    # ──────── Gamerule options ─────────────────────────────────
    drowning_damage: DrowningDamage
    fire_damage: FireDamage
    freeze_damage: FreezeDamage
    fall_damage: FallDamage
    keep_inventory: KeepInventory
    natural_regeneration: NaturalRegeneration
    raids: Raids
    mob_griefing: MobGriefing
    phantom_spawning: PhantomSpawning
    pillager_patrol_spawning: PillagerPatrolSpawning
    wandering_trader_spawning: WanderingTraderSpawning
    warden_spawning: WardenSpawning
    daylight_cycle: DaylightCycle
    weather_cycle: WeatherCycle
    lava_source_conversion: LavaSourceConversion
    water_source_conversion: WaterSourceConversion

    # ──────── Logic options ─────────────────────────────────
    chest_loot_logic: ChestLootLogic
    stronghold_access_logic: StrongholdAccessLogic
    outer_end_access_logic: OuterEndAccessLogic

    ender_dragon_required_armor: EnderDragonRequiredArmor
    ender_dragon_required_tools: EnderDragonRequiredTools

    wither_required_armor: WitherRequiredArmor
    wither_required_tools: WitherRequiredTools

    elder_guardian_required_armor: ElderGuardianRequiredArmor
    elder_guardian_required_tools: ElderGuardianRequiredTools

    warden_required_armor: WardenRequiredArmor
    warden_required_tools: WardenRequiredTools

    raid_required_armor: RaidRequiredArmor
    raid_required_tools: RaidRequiredTools

    trial_chamber_required_armor: TrialChamberRequiredArmor
    trial_chamber_required_tools: TrialChamberRequiredTools