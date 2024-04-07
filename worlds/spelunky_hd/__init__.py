# SpecsHD and the Cheat Engine table were both used for addresses/structures/enums etc

from typing import NamedTuple
from worlds.AutoWorld import World
from BaseClasses import Region, Location, Item, ItemClassification

journal_locations = {
    # places
    "The Mines" : 300, # implicit?
    "Jungle" : 301,
    "Ice Caves" : 302,
    "Temple" : 303,
    "Hell" : 304,
    # "Cemetery" : 305 # unused
    "Haunted Castle" : 306,
    "Black Market" : 307,
    "Worm" : 308,
    # "Yeti Cave" : 309 # unused 
    "Mothership" : 310,
    "City Of Gold" : 311,
    # monsters
    "Snake" : 1001,
    "Cobra" : 1036,
    "Bat" : 1003,
    "Spider" : 1002,
    "Spinner Spider" : 1037,
    "Giant Spider" : 1018,
    "Skeleton" : 1012,
    "Scorpion" : 1029,
    "Caveman" : 1004,
    "Damsel" : 1005,
    "Shopkeeper" : 1006,
    "Tunnel Man" : 1022, # is this implicit with Jungle?
    "Scarab" : 1024,
    "Tiki Man" : 1041,
    "Frog" : 1007,
    "Fire Frog" : 1021,
    "Giant Frog" : 1038,
    "Mantrap" : 1008,
    "Piranha" : 1013,
    "Old Bitey" : 1023,
    "Killer Bee" : 1032,
    "Queen Bee" : 1034,
    "Snail" : 1043,
    "Monkey" : 1015,
    "Golden Monkey" : 1050,
    "Jiang Shi" : 1019,
    "Green Knight" : 1045,
    "Black Knight" : 1049,
    "Vampire" : 1020,
    "Ghost" : 1017,
    "Bacterium" : 1035,
    "Worm Egg" : 1046,
    "Worm Baby" : 1047,
    "Yeti" : 1009,
    "Yeti King" : 1025,
    "Mammoth" : 1039,
    "Alien" : 1026,
    "UFO" : 1010,
    "Alien Tank" : 1040,
    "Alien Lord" : 1016,
    "Alien Queen" : 1048,
    "Hawk Man" : 1011,
    "Croc Man" : 1044,
    "Magma Man" : 1027,
    "Scorpion Fly" : 1042,
    "Mummy" : 1014,
    "Anubis" : 1033,
    "Anubis II" : 1054,
    "Olmec" : 1055,
    "Vlad" : 1028,
    "Imp" : 1030,
    "Devil" : 1031,
    "Succubus" : 1051,
    "Horse Head" : 1052,
    "Ox Face" : 1053,
    "King Yama" : 1056,
    # items
    "Rope Pile" : 500,
    "Bomb Bag" : 501,
    "Bomb Box" : 502,
    "Spectacles" : 503,
    "Climbing Gloves" : 504,
    "Pitcher's Mitt" : 505,
    "Spring Shoes" : 506,
    "Spike Shoes" : 507,
    "Paste" : 508,
    "Compass" : 509,
    "Mattock" : 510,
    "Boomerang" : 511,
    "Machete" : 512,
    "Crysknife" : 513,
    "Web Gun" : 514,
    "Shotgun" : 515,
    "Freeze Ray" : 516,
    "Plasma Cannon" : 517,
    "Camera" : 518,
    "Teleporter" : 519,
    "Parachute" : 520,
    "Cape" : 521,
    "Jetpack" : 522,
    "Shield" : 523,
    "Royal Jelly" : 524,
    "Idol" : 525,
    "Kapala" : 526,
    "Udjat Eye" : 527,
    "Ankh" : 528,
    "Hedjet" : 529,
    "Scepter" : 530,
    "Book of the Dead" : 531,
    "Vlad's Cape" : 532,
    "Vlad's Amulet" : 533,
    # traps
    "Spikes" : 100,
    "Arrow Trap" : 101,
    "Powder Box" : 102,
    "Boulder" : 103,
    "Tiki Trap" : 104,
    "Acid" : 105,
    "Spring" : 106,
    "Mine" : 107,
    "Turret" : 108,
    "Forcefield" : 109,
    "Crush Trap" : 110,
    "Ceiling Trap" : 111,
    "Spike Ball" : 113,
    "Lava" : 112,
}

achievement_locations = {
    name : id for id, name in enumerate([
        "Made It",
        "Ironman",
        "Public Enemy",
        "Casanova",
        "To Hell and Back",
        "Big Money",
        "The Entire Gang",
        "Seen It All",
        "Speedlunky",
        "Low Scorer",
    ], 10000)
}

spelunker_locations = {
    name : id for id, name in enumerate([
        "Coffin (The Mines)",
        "Coffin (The Jungle)",
        "Coffin (The Ice Caves)",
        "Coffin (The Temple)",
        "Black",
        "Aztec", # (same as Made It achievement?)
        "Meat Boy",
        "Yang", # (same as To Hell and Back achievement?)
        "Inuk",
        "The Round Girl",
        "Ninja",
        "The Round Boy",
        "Carl",
        "Viking",
        "Robot",
        "Golden Monk"
    ], 20000)
}

class ItemTuple(NamedTuple):
    id: int
    classification: ItemClassification

entity_items = {
    "Hired Help" : ItemTuple(0, ItemClassification.filler),
    "Rib Cage" : ItemTuple(11, ItemClassification.filler),
    "Ceiling Trap" : ItemTuple(42, ItemClassification.filler),
    "Trap Door" : ItemTuple(43, ItemClassification.filler),
    "Spring Trap" : ItemTuple(44, ItemClassification.trap),     # good trap
    "Crush Trap" : ItemTuple(45, ItemClassification.trap),      # ok trap
    "Landmine" : ItemTuple(92, ItemClassification.trap),        # ok trap
    "Chest" : ItemTuple(100, ItemClassification.useful),          # good treasure
    "Crate" : ItemTuple(101, ItemClassification.useful),          # great treasure
    "Gold Bar" : ItemTuple(102, ItemClassification.useful),       # ok treasure
    "Gold Pyramid" : ItemTuple(103, ItemClassification.useful),   # good treasure
    "Emerald Large" : ItemTuple(104, ItemClassification.useful),  # ok treasure
    "Sapphire Large" : ItemTuple(105, ItemClassification.useful), # good treasure
    "Ruby Large" : ItemTuple(106, ItemClassification.useful),     # good treasure
    "Live Bomb" : ItemTuple(107, ItemClassification.trap),      # good trap
    "Deploy Rope" : ItemTuple(108, ItemClassification.filler),
    "Whip" : ItemTuple(109, ItemClassification.filler),
    "Blood" : ItemTuple(110, ItemClassification.filler),          # ok treasure (if lots) (good with kapala)
    "Dirt Break" : ItemTuple(111, ItemClassification.filler),
    "Rock" : ItemTuple(112, ItemClassification.filler),           # bad treasure
    "Pot" : ItemTuple(113, ItemClassification.filler),            # bad treasure
    "Skull" : ItemTuple(114, ItemClassification.filler),          # bad treasure
    "Cobweb" : ItemTuple(115, ItemClassification.trap),         # good trap
    "Sticky Honey" : ItemTuple(116, ItemClassification.filler),
    "Bullet" : ItemTuple(117, ItemClassification.filler),
    "Gold Nugget Large" : ItemTuple(118, ItemClassification.useful), # ok treasure
    "Boulder" : ItemTuple(120, ItemClassification.trap),           # ok trap
    "Push Block" : ItemTuple(121, ItemClassification.filler),
    "Arrow" : ItemTuple(122, ItemClassification.filler),             # bad treasure
    "Gold Nugget Small" : ItemTuple(124, ItemClassification.filler), # bad treasure
    "Emerald Small" : ItemTuple(125, ItemClassification.filler),     # bad treasure
    "Sapphire Small" : ItemTuple(126, ItemClassification.filler),    # bad treasure
    "Ruby Small" : ItemTuple(127, ItemClassification.filler),        # bad treasure
    "Rope Segment" : ItemTuple(137, ItemClassification.filler),
    "Cobweb Projectile" : ItemTuple(142, ItemClassification.filler),
    "Udjat Chest" : ItemTuple(153, ItemClassification.progression), # needed unlock (for hell)
    "Golden Key" : ItemTuple(154, ItemClassification.progression),  # needed unlock (for hell)
    "Used Parachute" : ItemTuple(156, ItemClassification.filler),
    "Tiki Spikes" : ItemTuple(157, ItemClassification.filler),
    "Static Swing Attack Projectile" : ItemTuple(158, ItemClassification.filler),
    "Psychic Attack Bubbling" : ItemTuple(159, ItemClassification.filler),
    "UFO Projectile" : ItemTuple(160, ItemClassification.filler),
    "Blue Falling Platform" : ItemTuple(161, ItemClassification.filler),
    "Lantern" : ItemTuple(162, ItemClassification.filler), # bad treasure
    "Flare" : ItemTuple(163, ItemClassification.filler), # ok treasure
    "Snowball" : ItemTuple(164, ItemClassification.filler), # bad treasure
    "Vomit Fly" : ItemTuple(165, ItemClassification.filler),
    "White Flag" : ItemTuple(171, ItemClassification.filler),
    "Piranha Skeleton" : ItemTuple(172, ItemClassification.filler), # bad treasure
    "Diamond" : ItemTuple(173, ItemClassification.useful), # great treasure
    "Worm Tongue" : ItemTuple(174, ItemClassification.progression), # needed unlock (for journal)
    "Magma Cauldron" : ItemTuple(176, ItemClassification.filler), # bad treasure
    "Wide Light Emitter" : ItemTuple(177, ItemClassification.filler),
    "Spike Ball Detached" : ItemTuple(178, ItemClassification.filler), # ok trap
    "Breaking Chain Projectile" : ItemTuple(179, ItemClassification.filler),
    "Tutorial Journal" : ItemTuple(180, ItemClassification.progression),
    "Journal Page" : ItemTuple(181, ItemClassification.filler),
    "Worm Regen Block" : ItemTuple(182, ItemClassification.filler),
    "Cracking Ice Platform" : ItemTuple(183, ItemClassification.filler),
    "Leaf" : ItemTuple(184, ItemClassification.filler),
    "Decoy Chest" : ItemTuple(187, ItemClassification.filler),
    "Prize Wheel" : ItemTuple(188, ItemClassification.filler),
    "Prize Wheel Pin" : ItemTuple(189, ItemClassification.filler),
    "Prize Wheel Barricade" : ItemTuple(190, ItemClassification.filler),
    "Snail Bubble" : ItemTuple(192, ItemClassification.filler),
    "Cobra Venom Projectile" : ItemTuple(193, ItemClassification.filler),
    "Falling Icicle Projectile" : ItemTuple(194, ItemClassification.filler),
    "Broken Ice Projectiles" : ItemTuple(195, ItemClassification.filler),
    "Splashing Water Projectile" : ItemTuple(196, ItemClassification.filler),
    "Forcefield Ground Laser" : ItemTuple(197, ItemClassification.filler),
    "Forcefield Laser" : ItemTuple(198, ItemClassification.filler),
    "Freeze Ray Projectile" : ItemTuple(203, ItemClassification.trap), # good trap if on ground
    "Plasma Cannon Projectile/Shot" : ItemTuple(204, ItemClassification.trap), # ok trap
    "Mattock Head" : ItemTuple(210, ItemClassification.filler), # bad treasure
    "Coffin" : ItemTuple(211, ItemClassification.filler),
    "Turret Projectile" : ItemTuple(213, ItemClassification.filler),
    "Mothership Platform" : ItemTuple(214, ItemClassification.filler),
    "Mothership Elevator" : ItemTuple(215, ItemClassification.filler),
    "Arrow Shaft" : ItemTuple(216, ItemClassification.filler), # bad treasure
    "Olmec Enemy Spawn Projectile" : ItemTuple(217, ItemClassification.trap), # good trap
    "Splashing Water" : ItemTuple(218, ItemClassification.filler),
    "Ball & Chain" : ItemTuple(220, ItemClassification.trap), # good trap
    "Smoke Poof" : ItemTuple(221, ItemClassification.filler),
    "Ending Cutscene Camel" : ItemTuple(224, ItemClassification.filler),
    "Kill Target" : ItemTuple(225, ItemClassification.trap), # good trap
    "Activated Kill Target Laser" : ItemTuple(226, ItemClassification.trap),
    "Mothership Lights" : ItemTuple(227, ItemClassification.filler),
    "Broken Web Pouch" : ItemTuple(228, ItemClassification.trap), # ok trap
    "Breaking Animation" : ItemTuple(232, ItemClassification.filler),
    "Magma Flame Animation" : ItemTuple(233, ItemClassification.filler),
    "Anubis II Spawner" : ItemTuple(234, ItemClassification.trap), # good trap (if not too deadly)
    "TNT" : ItemTuple(235, ItemClassification.filler),
    "Spinner Spider Thread" : ItemTuple(236, ItemClassification.filler),
    "Destroyed Cobweb" : ItemTuple(237, ItemClassification.filler),
    "Decoy Yang" : ItemTuple(239, ItemClassification.filler),
    "Zero-Value Gold Nugget" : ItemTuple(240, ItemClassification.filler),
    "Lava/Water Spout" : ItemTuple(243, ItemClassification.filler),
    "Mounted Lightable Torch Holder" : ItemTuple(245, ItemClassification.filler),
    "Unlit Torch" : ItemTuple(246, ItemClassification.filler), # bad treasure
    "Purple Target" : ItemTuple(247, ItemClassification.filler),
    "Unopenable Mystery Box" : ItemTuple(248, ItemClassification.filler), # bad treasure
    "Alien Queen Corpse" : ItemTuple(249, ItemClassification.filler),
    "Crowned Skull" : ItemTuple(250, ItemClassification.filler), # ok treasure
    "Eggplant" : ItemTuple(252, ItemClassification.progression), # great treasure
    "Exploding Animation" : ItemTuple(301, ItemClassification.filler),
    "Laser Effect / Jetpack Flame" : ItemTuple(302, ItemClassification.filler),
    "Small Light" : ItemTuple(303, ItemClassification.filler),
    "Spring Rings" : ItemTuple(304, ItemClassification.filler),
    "Teleport Effect" : ItemTuple(305, ItemClassification.filler),
    "Wall Torch Flame" : ItemTuple(306, ItemClassification.filler),
    "Extinguished Torch Animation" : ItemTuple(307, ItemClassification.filler),
    "Rope Pile" : ItemTuple(500, ItemClassification.progression),  # good treasure
    "Bomb Bag" : ItemTuple(501, ItemClassification.progression),   # good treasure
    "Bomb Box" : ItemTuple(502, ItemClassification.progression),   # great treasure
    "Spectacles" : ItemTuple(503, ItemClassification.progression), # good treasure
    "Climbing Gloves" : ItemTuple(504, ItemClassification.progression), # great treasure
    "Pitcher's Mitt" : ItemTuple(505, ItemClassification.progression), # good treasure
    "Spring Shoes" : ItemTuple(506, ItemClassification.progression), # great treasure
    "Spike Shoes" : ItemTuple(507, ItemClassification.progression), # great treasure
    "Paste" : ItemTuple(508, ItemClassification.progression), # great treasure
    "Compass" : ItemTuple(509, ItemClassification.progression_skip_balancing), # great treasure
    "Mattock" : ItemTuple(510, ItemClassification.progression), # great treasure
    "Boomerang" : ItemTuple(511, ItemClassification.progression_skip_balancing), # good treasure
    "Machete" : ItemTuple(512, ItemClassification.progression_skip_balancing), # good treasure
    "Crysknife" : ItemTuple(513, ItemClassification.progression), # amazing treasure
    "Web Gun" : ItemTuple(514, ItemClassification.progression_skip_balancing), # good treasure
    "Shotgun" : ItemTuple(515, ItemClassification.progression), # great treasure
    "Freeze Ray" : ItemTuple(516, ItemClassification.progression), # great treasure
    "Plasma Cannon" : ItemTuple(517, ItemClassification.progression), # great treasure
    "Camera" : ItemTuple(518, ItemClassification.progression_skip_balancing), # good treasure
    "Teleporter" : ItemTuple(519, ItemClassification.progression), # great treasure
    "Parachute" : ItemTuple(520, ItemClassification.progression_skip_balancing), # good treasure
    "Cape" : ItemTuple(521, ItemClassification.progression), # great treasure
    "Jetpack" : ItemTuple(522, ItemClassification.progression), # amazing treasure
    "Shield" : ItemTuple(523, ItemClassification.progression), # great treasure
    "Royal Jelly" : ItemTuple(524, ItemClassification.progression), # great treasure
    "Idol" : ItemTuple(525, ItemClassification.progression), # great treasure (if I can dearm it), retextured to skull on cemetery (EVEN IF CHANGED TO ANOTHER ENTITY)
    "Kapala" : ItemTuple(526, ItemClassification.progression), # amazing treasure
    "Udjat Eye" : ItemTuple(527, ItemClassification.progression), # progression treasure (and good treasure)
    "Ankh" : ItemTuple(528, ItemClassification.progression), # progression treasure (and great treasure)
    "Hedjet" : ItemTuple(529, ItemClassification.progression), # progression treasure
    "Scepter" : ItemTuple(530, ItemClassification.progression), # progression treasure (and great treasure)
    "Book of the Dead" : ItemTuple(531, ItemClassification.progression), # progression treasure
    "Vlad's Cape" : ItemTuple(532, ItemClassification.progression), # amazing treasure
    "Vlad's Amulet" : ItemTuple(533, ItemClassification.progression), # good treasure
    "Snake" : ItemTuple(1001, ItemClassification.progression),
    "Spider" : ItemTuple(1002, ItemClassification.progression),
    "Bat" : ItemTuple(1003, ItemClassification.progression),
    "Caveman" : ItemTuple(1004, ItemClassification.progression),
    "Damsel" : ItemTuple(1005, ItemClassification.progression), # great treasure
    "Shopkeeper" : ItemTuple(1006, ItemClassification.progression),
    "Blue Frog" : ItemTuple(1007, ItemClassification.progression),
    "Mantrap" : ItemTuple(1008, ItemClassification.progression),
    "Yeti" : ItemTuple(1009, ItemClassification.progression),
    "UFO" : ItemTuple(1010, ItemClassification.progression),
    "Hawk Man" : ItemTuple(1011, ItemClassification.progression),
    "Skeleton" : ItemTuple(1012, ItemClassification.progression),
    "Piranha" : ItemTuple(1013, ItemClassification.progression),
    "Mummy" : ItemTuple(1014, ItemClassification.progression),
    "Monkey" : ItemTuple(1015, ItemClassification.progression),
    "Alien Lord" : ItemTuple(1016, ItemClassification.progression),
    "Ghost" : ItemTuple(1017, ItemClassification.progression),
    "Giant Spider" : ItemTuple(1018, ItemClassification.progression),
    "Jiang Shi" : ItemTuple(1019, ItemClassification.progression),
    "Vampire" : ItemTuple(1020, ItemClassification.progression),
    "Orange Frog" : ItemTuple(1021, ItemClassification.progression),
    "Tunnel Man" : ItemTuple(1022, ItemClassification.progression),
    "Old Bitey" : ItemTuple(1023, ItemClassification.progression),
    "Golden Scarab" : ItemTuple(1024, ItemClassification.progression), # good treasure
    "Yeti King" : ItemTuple(1025, ItemClassification.progression),
    "Little Alien" : ItemTuple(1026, ItemClassification.progression),
    "Magma Man" : ItemTuple(1027, ItemClassification.progression),
    "Vlad" : ItemTuple(1028, ItemClassification.progression),
    "Scorpion" : ItemTuple(1029, ItemClassification.progression),
    "Imp" : ItemTuple(1030, ItemClassification.progression),
    "Blue Devil" : ItemTuple(1031, ItemClassification.progression),
    "Bee" : ItemTuple(1032, ItemClassification.progression),
    "Anubis" : ItemTuple(1033, ItemClassification.progression),
    "Queen Bee" : ItemTuple(1034, ItemClassification.progression),
    "Bacterium" : ItemTuple(1035, ItemClassification.progression),
    "Cobra" : ItemTuple(1036, ItemClassification.progression),
    "Spinner Spider" : ItemTuple(1037, ItemClassification.progression),
    "Big Frog" : ItemTuple(1038, ItemClassification.progression),
    "Mammoth" : ItemTuple(1039, ItemClassification.progression),
    "Alien Tank" : ItemTuple(1040, ItemClassification.progression),
    "Tiki Man" : ItemTuple(1041, ItemClassification.progression),
    "Scorpion Fly" : ItemTuple(1042, ItemClassification.progression),
    "Snail" : ItemTuple(1043, ItemClassification.progression),
    "Croc Man" : ItemTuple(1044, ItemClassification.progression),
    "Green Knight" : ItemTuple(1045, ItemClassification.progression),
    "Worm Egg" : ItemTuple(1046, ItemClassification.progression),
    "Worm Baby" : ItemTuple(1047, ItemClassification.progression),
    "Alien Queen" : ItemTuple(1048, ItemClassification.progression),
    "Black Knight" : ItemTuple(1049, ItemClassification.progression),
    "Golden Monkey" : ItemTuple(1050, ItemClassification.progression), # great treasure
    "Succubus" : ItemTuple(1051, ItemClassification.progression), # great trap
    "Horse Head" : ItemTuple(1052, ItemClassification.progression),
    "Ox Face" : ItemTuple(1053, ItemClassification.progression),
    "Olmec" : ItemTuple(1055, ItemClassification.filler), # should probably always be unlocked
    "King Yama Head" : ItemTuple(1056, ItemClassification.filler), # ^
    "King Yama Fist" : ItemTuple(1057, ItemClassification.filler),
    "Turret" : ItemTuple(1058, ItemClassification.filler), # bad trap or bad treasure?
    "Blue Frog Critter" : ItemTuple(1059, ItemClassification.filler),
    "Alien Queen Eye" : ItemTuple(1060, ItemClassification.filler),
    "Spiderling Critter" : ItemTuple(1061, ItemClassification.filler), # cute
    "Fish Critter" : ItemTuple(1062, ItemClassification.filler), # cute
    "Rat Critter" : ItemTuple(1063, ItemClassification.filler), # cute
    "Penguin Critter" : ItemTuple(1064, ItemClassification.filler), # cute
    "Little Alien Horizontally Moving" : ItemTuple(1065, ItemClassification.filler),
    "Locust Critter" : ItemTuple(1067, ItemClassification.filler), # cute
    "Maggot Critter" : ItemTuple(1068, ItemClassification.filler), # cute
}

extra_items = {
    "Filler Item" : ItemTuple(10000, ItemClassification.filler), # todo: replace
}

all_items = {
    **entity_items,
    **extra_items
}

# please keep up to date with Dictionary in Client's EntityTypesEnabled for now,
# ideally I should find a way to automatically generate this list
one_of_each_item = [
    "Rope Pile",
    "Bomb Bag",
    "Bomb Box",
    "Spectacles",
    "Climbing Gloves",
    "Pitcher's Mitt",
    "Spring Shoes",
    "Spike Shoes",
    "Paste",
    "Compass",
    "Mattock",
    "Boomerang", # tikimen don't have boomerangs either
    "Machete",
    "Crysknife",
    "Web Gun",
    "Shotgun", # shopkeepers don't have shotguns either
    "Freeze Ray",
    "Plasma Cannon",
    "Camera",
    "Teleporter",
    "Parachute",
    "Cape",
    "Jetpack",
    "Shield",
    "Royal Jelly",
    "Idol",
    "Kapala",
    "Udjat Eye", # should the player only need to unlock key + chest
    "Ankh",
    "Hedjet", # should this be implicit to the moai statue?
    "Scepter", # anubis doesn't need this to attack
    "Book of the Dead",
    "Vlad's Cape",
    "Vlad's Amulet",

    "Damsel",

    "Udjat Chest",
    "Golden Key",
]

class SpelunkyHDItem(Item):
    game = "Spelunky HD"

class SpelunkyHDLocation(Location):
    game = "Spelunky HD"

class SpelunkyHDWorld(World):
    game = "Spelunky HD"

    item_name_to_id = {
        name : all_items[name].id for name in all_items
    }
    location_name_to_id = {
        **journal_locations,
        **achievement_locations,
        **spelunker_locations
    }

    items_needed = 0

    def create_regions(self) -> None:
        #menu_region = Region("Menu", self.player, self.multiworld)
        #self.multiworld.regions += [menu_region]

        # # might not be true if region order is randomized (ie some might be accessable later),
        # # same if I randomize enemies (or if I add "traps" like succubus)
        # self.add_region("Menu", [
        #     "The Mines",

        #     "Snake", "Cobra", "Bat", "Spider", "Spinner Spider", "Giant Spider",
        #     "Skeleton", "Scorpion", "Caveman", "Damsel", "Shopkeeper",
        #     "Scarab", # dark levels/city of gold only
        #     # Piranha might spawn if re-enable removed Mines water level?
        #     "Golden Monkey", # sacrifice only
        #     "Ghost",
        #     # aliens can spawn in pots, but EXTREMELY rarely (0.02%)

        #     # these might not be possible if I make them unlockable?
        #     "Rope Pile", "Bomb Bag", "Bomb Box", "Spectacles", "Climbing Gloves",
        #     "Pitcher's Mitt", "Spring Shoes", "Spike Shoes", "Paste", "Compass",
        #     "Mattock", "Boomerang", "Machete", "Web Gun", "Shotgun", "Freeze Ray",
        #     # Plasma Cannon is EXTREMELY EXTREMELY RARE (0.01% in a crate)
        #     "Camera", "Teleporter", "Parachute", "Cape", "Jetpack",
        #     "Idol", "Kapala", "Udjat Eye",

        #     "Spikes", "Arrow Trap", "Powder Box", "Boulder",

        #     # "Coffin (The Mines)", "The Round Girl" (NOT IMPLEMENTED ON CLIENT YET)

        #     # Big Money is technically possible but requires lots of glitching and extreme skills
        # ])

        self.add_region("Menu", journal_locations.keys())

    def add_region(self, name: str, locations: any) -> Region:
        self.items_needed += len(locations)
        region = Region(name, self.player, self.multiworld, name)
        region.add_locations({
            name : self.location_name_to_id.get(name) for name in locations
        }, SpelunkyHDLocation)
        self.multiworld.regions += [region]
        return region

    def create_item(self, name: str) -> SpelunkyHDItem:
        item = all_items.get(name)
        if item is None:
            raise Exception(f"Item {name} not found")
        
        return SpelunkyHDItem(name, item.classification, item.id, self.player)

    def create_items(self) -> None:
        assert(self.items_needed >= len(one_of_each_item))
        for item in one_of_each_item:
            self.items_needed -= 1
            self.multiworld.itempool += [self.create_item(item)]
        for _ in range(self.items_needed):
            self.multiworld.itempool += [self.create_item("Filler Item")]
