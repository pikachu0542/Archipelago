from typing import Dict, NamedTuple
from BaseClasses import ItemClassification


class ItemData(NamedTuple):
    code: int
    classification: ItemClassification


PROGRESSIVE_ITEM_BASE_ID = 10000
ITEM_UNLOCK_BASE_ID = 11000
BLOCK_UNLOCK_BASE_ID = 12000
GAMERULE_BASE_ID = 13000
FILLER_ITEM_BASE_ID = 14000

# ── Progressive unlock items ───────────────────────────────────────────────
# Sent multiple times. The mod tracks receipt count and applies the
# matching stage tier (stone → gold → iron → diamond → netherite).
# ──────────────────────────────────────────────────────────────────────────

progressive_items: Dict[str, ItemData] = {
    "Progressive Tools":         ItemData(10000, ItemClassification.progression),
    "Progressive Armor":         ItemData(10001, ItemClassification.progression),
    "Progressive Tools (Gift)":  ItemData(10002, ItemClassification.useful),
    "Progressive Armor (Gift)":  ItemData(10003, ItemClassification.useful),
}

PROGRESSIVE_ITEM_COUNTS = {
    "Progressive Tools":         5,  # stone, gold, iron, diamond, netherite
    "Progressive Armor":         6,  # leather, gold, chainmail, iron, diamond, netherite
    "Progressive Tools (Gift)":  6,  # wooden, stone, gold, iron, diamond, netherite
    "Progressive Armor (Gift)":  6,  # leather, gold, chainmail, iron, diamond, netherite
}

# ── Individual unlock items ────────────────────────────────────────────────
# Each sent once. Unlocks the ability to USE that item type.
# Items marked with (Gift) in filler are the physical give version.
# ──────────────────────────────────────────────────────────────────────────

# Unlocks for items that the player can use
item_unlocks: Dict[str, ItemData] = {
    "Boat":             ItemData(11000, ItemClassification.progression),
    "Bone Meal":        ItemData(11001, ItemClassification.useful),
    "Bow":              ItemData(11002, ItemClassification.progression),
    "Bucket":           ItemData(11003, ItemClassification.progression),
    "Crossbow":         ItemData(11004, ItemClassification.progression),
    "Elytra":           ItemData(11005, ItemClassification.progression),
    "Ender Pearl":      ItemData(11006, ItemClassification.progression),
    "End Crystal":      ItemData(11007, ItemClassification.progression),
    "Eye of Ender":     ItemData(11008, ItemClassification.progression),
    "Fishing Rod":      ItemData(11009, ItemClassification.progression),
    "Flint and Steel":  ItemData(11010, ItemClassification.progression),
    "Golden Apple":     ItemData(11011, ItemClassification.progression),
    "Mace":             ItemData(11012, ItemClassification.progression),
    "Map":              ItemData(11013, ItemClassification.filler),
    "Name Tag":         ItemData(11014, ItemClassification.filler),
    "Ominous Bottle":   ItemData(11015, ItemClassification.progression),
    "Potion":           ItemData(11016, ItemClassification.progression),
    "Shears":           ItemData(11017, ItemClassification.progression),
    "Shield":           ItemData(11018, ItemClassification.progression),
    "Spyglass":         ItemData(11019, ItemClassification.progression),
    "Totem of Undying": ItemData(11020, ItemClassification.progression),
    "Trident":          ItemData(11021, ItemClassification.progression),
    "Turtle Shell":     ItemData(11022, ItemClassification.useful),
}

# Unlocks for blocks that can be placed and/or interacted with
block_unlocks: Dict[str, ItemData] = {
    "Anvil":                ItemData(12000, ItemClassification.useful),
    "Beacon":               ItemData(12001, ItemClassification.progression),
    "Bed":                  ItemData(12002, ItemClassification.progression),
    "Brewing Stand":        ItemData(12003, ItemClassification.progression),
    "Campfire":             ItemData(12004, ItemClassification.progression),
    "Composter":            ItemData(12005, ItemClassification.useful),
    "Conduit":              ItemData(12006, ItemClassification.progression),
    "Enchanting Table":     ItemData(12007, ItemClassification.progression),
    "Ender Chest":          ItemData(12008, ItemClassification.useful),
    "Furnace":              ItemData(12009, ItemClassification.progression),
    "Grindstone":           ItemData(12010, ItemClassification.useful),
    "Lightning Rod":        ItemData(12011, ItemClassification.progression),
    "Lodestone":            ItemData(12012, ItemClassification.progression),
    "Respawn Anchor":       ItemData(12013, ItemClassification.progression),
    "Shulker Box":          ItemData(12014, ItemClassification.useful),
    "Smithing Table":       ItemData(12015, ItemClassification.progression),
    "Target":               ItemData(12016, ItemClassification.progression),
    "TNT":                  ItemData(12017, ItemClassification.useful),
    "Torch":                ItemData(12018, ItemClassification.useful),
}

unlock_items: Dict[str, ItemData] = {
    **item_unlocks,
    **block_unlocks,    
}

# ── Gamerule items ─────────────────────────────────────────────────────────
# Each permanently changes a world rule when received.
# Comments show the 1.21.1 camelCase gamerule name and the value set on receipt.
# The default value for each rule on world creation is the opposite of what is listed in the comment.
# ──────────────────────────────────────────────────────────────────────────

gamerule_items: Dict[str, ItemData] = {
    "No Drowning Damage":           ItemData(13000, ItemClassification.useful),             # drowningDamage false
    "No Fire Damage":               ItemData(13001, ItemClassification.useful),             # fireDamage false
    "No Freeze Damage":             ItemData(13002, ItemClassification.useful),             # freezeDamage false
    "No Fall Damage":               ItemData(13003, ItemClassification.useful),             # fallDamage false
    "Keep Inventory":               ItemData(13004, ItemClassification.useful),             # keepInventory true
    "Natural Regeneration":         ItemData(13005, ItemClassification.useful),             # naturalRegeneration true

    "Raids":                        ItemData(13006, ItemClassification.progression),        # disableRaids false
    "Disable Mob Griefing":         ItemData(13007, ItemClassification.useful),             # mobGriefing false

    "Phantom Spawning":             ItemData(13008, ItemClassification.progression),        # doInsomnia true
    "Pillager Patrol Spawning":     ItemData(13009, ItemClassification.useful),             # doPatrolSpawning true
    "Wandering Traders":            ItemData(13010, ItemClassification.useful),             # doTraderSpawning true
    "Warden Spawning":              ItemData(13011, ItemClassification.progression),        # doWardenSpawning true

    "Daylight Cycle":               ItemData(13012, ItemClassification.progression),        # doDaylightCycle true
    "Weather Cycle":                ItemData(13013, ItemClassification.progression),        # doWeatherCycle true
    "Lava Source Conversion":       ItemData(13014, ItemClassification.useful),             # lavaSourceConversion true
    "Water Source Conversion":      ItemData(13015, ItemClassification.useful),             # waterSourceConversion true
}

# ── Filler items ───────────────────────────────────────────────────────────
# Physically given to the player on receipt.
# Items that are also in unlock_items above use the (Gift) suffix here.
# ──────────────────────────────────────────────────────────────────────────

filler_items: Dict[str, ItemData] = {

    # — Food Tier 1 ————————————————————————————————————————————————————————
    "Beetroot (Gift)":              ItemData(14000, ItemClassification.filler),
    "Cookie (Gift)":                ItemData(14001, ItemClassification.filler),
    "Dried Kelp (Gift)":            ItemData(14002, ItemClassification.filler),
    "Glow Berries (Gift)":          ItemData(14003, ItemClassification.filler),
    "Melon Slice (Gift)":           ItemData(14004, ItemClassification.filler),
    "Poisonous Potato (Gift)":      ItemData(14005, ItemClassification.filler),
    "Potato (Gift)":                ItemData(14006, ItemClassification.filler),
    "Pufferfish (Gift)":            ItemData(14007, ItemClassification.filler),
    "Rotten Flesh (Gift)":          ItemData(14008, ItemClassification.filler),
    "Spider Eye (Gift)":            ItemData(14009, ItemClassification.filler),
    "Tropical Fish (Gift)":         ItemData(14010, ItemClassification.filler),

    # — Food Tier 2 ————————————————————————————————————————————————————————
    "Apple (Gift)":                 ItemData(14011, ItemClassification.filler),
    "Bread (Gift)":                 ItemData(14012, ItemClassification.filler),
    "Rabbit Stew (Gift)":           ItemData(14013, ItemClassification.filler),
    "Raw Beef (Gift)":              ItemData(14014, ItemClassification.filler),
    "Raw Chicken (Gift)":           ItemData(14015, ItemClassification.filler),
    "Raw Mutton (Gift)":            ItemData(14016, ItemClassification.filler),
    "Raw Porkchop (Gift)":          ItemData(14017, ItemClassification.filler),
    "Raw Rabbit (Gift)":            ItemData(14018, ItemClassification.filler),

    # — Food Tier 3 ————————————————————————————————————————————————————————
    "Cooked Porkchop (Gift)":       ItemData(14019, ItemClassification.filler),
    "Golden Carrot (Gift)":         ItemData(14020, ItemClassification.filler),
    "Pumpkin Pie (Gift)":           ItemData(14021, ItemClassification.filler),
    "Steak (Gift)":                 ItemData(14022, ItemClassification.filler),

    # — Weapons to give ————————————————————————————————————————————————————
    "Arrow (Gift)":                 ItemData(14027, ItemClassification.filler),
    "Bow (Gift)":                   ItemData(14025, ItemClassification.filler),
    "Crossbow (Gift)":              ItemData(14026, ItemClassification.filler),
    "Mace (Gift)":                  ItemData(14024, ItemClassification.filler),
    "Shield (Gift)":                ItemData(14028, ItemClassification.filler),
    "Trident (Gift)":               ItemData(14023, ItemClassification.filler),

    # — Blocks ————————————————————————————————————————————————————————————
    "Cobblestone (Gift)":           ItemData(14029, ItemClassification.filler),
    "Dirt (Gift)":                  ItemData(14030, ItemClassification.filler),
    "Oak Planks (Gift)":            ItemData(14031, ItemClassification.filler),
    "Scaffolding (Gift)":           ItemData(14032, ItemClassification.filler),
    "Torch (Gift)":                 ItemData(14033, ItemClassification.filler),

    # — Materials ——————————————————————————————————————————————————————————
    "Amethyst Shard (Gift)":        ItemData(14034, ItemClassification.filler),
    "Coal (Gift)":                  ItemData(14035, ItemClassification.filler),
    "Copper Ingot (Gift)":          ItemData(14036, ItemClassification.filler),
    "Diamond (Gift)":               ItemData(14037, ItemClassification.filler),
    "Emerald (Gift)":               ItemData(14038, ItemClassification.filler),
    "Glowstone Dust (Gift)":        ItemData(14039, ItemClassification.filler),
    "Gold Ingot (Gift)":            ItemData(14040, ItemClassification.filler),
    "Iron Ingot (Gift)":            ItemData(14041, ItemClassification.filler),
    "Lapis Lazuli (Gift)":          ItemData(14042, ItemClassification.filler),
    "Leather (Gift)":               ItemData(14043, ItemClassification.filler),
    "Netherite Scrap (Gift)":       ItemData(14044, ItemClassification.filler),
    "Nether Quartz (Gift)":         ItemData(14045, ItemClassification.filler),
    "Redstone (Gift)":              ItemData(14046, ItemClassification.filler),

    # — Utility ————————————————————————————————————————————————————————————
    "Boat (Gift)":                  ItemData(14047, ItemClassification.filler),
    "Bucket (Gift)":                ItemData(14048, ItemClassification.filler),
    "Compass (Gift)":               ItemData(14049, ItemClassification.filler),
    "Fishing Rod (Gift)":           ItemData(14050, ItemClassification.filler),
    "Flint and Steel (Gift)":       ItemData(14051, ItemClassification.filler),
    "Spyglass (Gift)":              ItemData(14052, ItemClassification.filler),

    # — Junk ———————————————————————————————————————————————————————————————
    "Coral (Gift)":                 ItemData(14053, ItemClassification.filler),
    "Curse Enchanted Book (Gift)":  ItemData(14054, ItemClassification.filler),
    "Dye (Gift)":                   ItemData(14055, ItemClassification.filler),
    "Flower (Gift)":                ItemData(14056, ItemClassification.filler),
    "Ink Sac (Gift)":               ItemData(14057, ItemClassification.filler),
    "Painting (Gift)":              ItemData(14058, ItemClassification.filler),
}

# ── Combined table ─────────────────────────────────────────────────────────

item_table: Dict[str, ItemData] = {
    **progressive_items,
    **unlock_items,
    **gamerule_items,
    **filler_items,
}
