import random
import sys, time
from replit import audio
from dataclasses import dataclass


@dataclass

class Character:
    name: str
    health: int
    speed: int
    heals: int
    berries: int
    bats: bool
    key: bool
    mouse: bool
    badlands: bool
    cave: bool
    chestplate: bool
    weapon: bool
    boots: bool
    armor_vendor: bool
    weapons_vendor: bool


@dataclass
class Enemy:
    name: str
    health: int
    speed: int
    damage: int


blank = Enemy("", 0, 0, 0)
skeleton_1 = Enemy("Jonely Bonely", 1, 60, random.randint(10, 15))
skeleton_2 = Enemy("Bones Malone", 1, 60, random.randint(10, 15))
gator_1 = Enemy("Bill Gators", 100, 40, random.randint(15, 20))
gator_2 = Enemy("Big Al", 100, 40, random.randint(15, 20))
spider_1 = Enemy("Mr. Webb", 80, 75, random.randint(12, 18))
spider_2 = Enemy("Jerry Stringer", 80, 75, random.randint(12, 18))
vulture_1 = Enemy("Cuh Caw", 60, 60, random.randint(8, 12))
vulture_2 = Enemy("Can Yun", 60, 60, random.randint(8, 12))
otter_1 = Enemy("First Mate Otty Otterton", 1, 75, random.randint(10, 15))
otter_2 = Enemy("Captain Otto", 1, 75, random.randint(10, 15))
snake = Enemy("Piethon", 120, 85, random.randint(15, 25))
boss = Enemy("Ember Gaze The Death Bringer", 1, 90, random.randint(30, 40))



def texttime_1(words):
    for c in words:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)


def texttime_2(words):
    for c in words:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)


intro = texttime_1(
    """
  --------------------- Welcome --------------------
  --------------------------------------------------
  ----------------------- To -----------------------
  --------------------------------------------------
  -------------- Into The Thick Of It --------------
  --------------------------------------------------
  """
)
choose_message = texttime_1(
    """ Choose your character!
- [Rascal] - Raccoon - Ranged - A Trickster
- [Luna] - Wolf - Swordsman - An Edgelord
- [Ted] - Bear - Tank - Has the Power of Friendship
"""
)

rascal_info = """You have chosen Rascal. You have always been on the run. You've never relied on anyone but yourself. You don't want to get too close to anyone. Like ever. You are a ranged fighter wielding a bow.

Your attacks include:
- Deadshot: 30 - 40 dmg to a single enemy - 80% hit
- Arrow Storm: 20 - 25 dmg to multiple enemies - 70% hit
- Tactical Whack: 20 - 30 dmg to a single enemy - 90% hit

*** If you ever want to check your berry count just input 'Berry Amount' ***
"""
luna_info = """ You have chosen Luna. You come from an overbearing family of 10. You have seven siblings who are all very annoying. Your parents never wanted you to leave their side. You decide to venture out by yourself to live your own life. You are a close-combat swordsman wielding a katana.

Your attacks include:
- Frontal Slash: 25 - 35 dmg to a single enemy - 80% hit
- Sword Dance: 15 - 25 dmg to multiple enemies - 70% hit
- Piercing Strike: 20 - 30 dmg to a single enemy - 90% hit

*** If you ever want to check your berry count just input 'Berry Amount' ***
"""

ted_info = """You have chosen TED. You use the power of nature to call upon your strength. You're basically a strong-willed kind-hearted person. You are an upfront tank wielding a battleaxe.

Your attacks include:
- Crushing Blow: 20 - 30 dmg to a single enemy - 80% hit
- Earthquake: 15 - 20 dmg to multiple enemies - 70% hit
- Fatal Chop: 20 - 25 dmg to a single enemy - 90%

*** If you ever want to check your berry count just input 'Berry Amount' ***
"""

forest_info = """
You arrive at the Forest. You are surrounded by towering trees in every direction. You wander along the leafy path into the heart of the forest. You come across an intersection. To the west you can hear the rushing of water. To the south you can see bright lights in the distance. To the east the path continues into darkness.

Where would you like to go?
- Go [East]
- Go [West]
- Go [South]
"""
path_1_info = """
You arrive at an intersection at the edge of the forest. To the east you see the path leading back to the center of the forest. To the south you see some sort of gathering of animals. To the west you see some old ruins, withered away by time.

What would you like to do?
- Go [East]
- Go [South]
- Go [West]

"""
path_2_info = """
You arrive at an intersection close to the plains. To the north you can see the makings of an isolated castle. To the west you can see a marshy area forming. To the east you can see a few buildings. To the south you see a large expanse of grasslands. 

What would you like to do?
- Go [North]
- Go [West]
- Go [East]
- Go [South]
"""
path_3_info = """ 
You reach an intersection at the edge of the plains. To the west you see an immense area of grasslands. To the north you can see a small rocky hill with a tiny opening. To the east you can see a drop in the landscape.

What would you like to do?
- Go [West]
- Go [North]
- Go [East]
"""
path_4_info = """ 
You arrive at an intersection surrounded by sand. To the east you can see more sand. To the south you see some sandy hills and a bit of an opening. To the west you can see what looks to be a crater.

What would you like to do?
- Go [West]
- Go [East]
- Go [South]
"""
path_5_info = """ 
You arrive at an intersection closer to the water. To the north you see a crystal blue bay. To the west you can hear waves crashing against the shore. To the east you see a wasteland. To the south you see a large expanse of sand.

What would you like to do?
- Go [North]
- Go [West]
- Go [East]
- Go [South]
"""
sanctuary_info = """
You arrive at Sanctuary. The sun shines through the leaves onto some beds of grass. This is the place where animals go to restore themselves back to full health. An armadillo is walking around treating injured animals. He walks up to you.

Armadillo: Hey man, what's up? Welcome to Sanctuary. I'm Randy. I take care of everybody here so they can live their best life. If you ever need some patching up you let me know, k?

The only entrance to sanctuary is the way you entered.

What would you like to do?
- [Heal]
- Go back to the [Path]
"""
ruins_info_1 = """
You arrive at the Ruins. The blistering sun beams down on the decaying fortress and the wind whistles through the terraformed castle. In one corner of the ruins you see a pile of bones. Curious, you walk over. Surprisingly, the bones spring up and form skeletons as they grasp nearby swords.
"""
ruins_info_2 = """
You arrive at the Ruins. The blistering sun beams down on the decaying fortress and the wind whistles through the terraformed castle. You see the pile of bones from your previous battle in the center of the ruins. To the east you see the forest where you started your journey. To the south you see a vast expanse of grasslands.

What would you like to do?
- Go [East]
- Go [South]
"""
swamp_info_1 = """
You arrive at the Untamed Swamp. The ground beneath you squishes as you tread forward. In the distance you can see a murky pond in the middle of the marsh. You walk closer to the water and see a few logs floating in the water, but they aren't logs. Gators rise from the water clutching weapons.
"""
swamp_info_2 = """
You arrive at the Untamed Swamp. The ground beneath you squishes as you tread forward. In the distance you can see a murky pond in the middle of the marsh. You view the bodies from your previous battle floating on the surface of the water. The only path from the marsh is the one you came from.

What would you like to do?
- Go back to the [Path]
"""
tavern_info = """
You arrive at the Tavern. Animals from all species gather here to meet friends and share stories. Across the tavern you see a bar, behind it... a mouse. In the corner of the room, a bunny sits with 2 lady bunnies on each side (He looks like his name is Jack). The only path to the tavern is the one you came from.

What would you like to do?
- Go back to the [Path]
- Talk to the [Mouse]
"""
plains_info = """
You arrive at the Plains. The only thing you can see is grass. To the north you see grass. To the east you see... more grass.

What would you like to do?
- Go [North]
- Go [East]
"""
den_info_1 = """
You arrive at the Den of Darkness. You see a small hole in the ground and descend into the abyss. You crawl down into a dirt cave. Spider webs hang from every inch of the den. As you walk deeper into the cave, you come across a family of spiders.
"""
den_info_2 = """
You arrive at the Den of Darkness. You see a small hole in the ground and descend into the abyss. You crawl donw into a dirt cave. Spider webs hang from every inch of the den.  At the back of the cave you see the crumpled bodies of the spider family you slaughtered previously. The only entrance to the den is the way you came from.

What would you like to do?
- Go back to the [Path]
"""
canyon_info_1 = """
You wander towards what seems to be a ravine. You arrived at Corrupted Canyon. On one side of the canyon, all you can see is sand. On the other, you can start to see grass growing. You clamber towards the edge of the ravine and peer into the abyss, but a few vultures shoot up out of the gorge and land close to you looking for a battle.
"""
canyon_info_2 = """
You wander towards what seems to be a ravine. You arrived at Corrupted Canyon. On one side of the canyon, all you can see is sand. On the other, you can start to see grass growing. You clamber towards the edge of the ravine and peer into the abyss. You look down into the gorge and see the dead carcasses of the birds you defeaterd earlier. To the north you can see lots of bright lights. To the west you can see the beginnings of the grasslands. To the east all you can see is sand.

What would you like to do?
- Go [North]
- Go [West]
- Go [East]
"""
cavern_info_1 = """
You arrived at the Blackbrook caverns.  You enter and emerge into a dimly lit cave. There is a family of bats hanging in the back. They don't seem to be hostile. Their belongings are scattered all over the caverns and a pile of berries lay on a table nearby.

What would you like to do?
- Go back to the [Path]
- Talk to the [Bats]
- Steal the [Berries]
"""
desert_info_1 = """
You have arrived at the Barren Lands. Nothing but sand surrounds you. The only visible things are a few dead bushes and some sand dunes. You wander through the desert looking for some sort of sign or path. From behind one of the sand dunes, a large snake emerges and sits there... menacingly.
"""
desert_info_2 = """
You arrive at the Barren Lands. Nothing but sand surrounds you. The only visible things are a few dead bushes and some sand dunes. You wander through the desert looking for some sort of sign or path. You glance around one of the sand dunes and see the gigantic snake that you slaughtered earlier. To the north there is sand. To the west there is more sand.

What would you like to do?
- Go [North]
- Go [West]
"""
badlands_info_1 = """
You have arrived at the Badlands. There are tons of dead trees surrounding you, almost as if someone burned them all. Alone in the middle of the badlands sits a stone tower. You look up to see fire erupting from the top window. You try to open the door but it's locked.

What would you like to do?
- Go back to the [Path]
"""
badlands_info_2 = """
You have arrived at the Badlands. There are tons of dead trees surrounding you, almost as if someone burned them all. Alone in the middle of the badlands sits a stone tower. You look up to see fire erupting from the top window. You use the key that you found in the Den of Darkness and the door opens.

What would you like to do?
- Go back to the [Path]
- [Enter]
"""
shores_info = """
You arrive at Sunshine Shores. You look into the distance to see the beautiful horizon and the mystic sea. You walk along the beach to find a path, but you find none. The only path is the one you took. 

What would you like to do?
- Go back to the [Path]
"""
cove_info_1 = """
You arrive at Pirate's Cove. You found a boat along the shore and decide to take it. You sail towards the center of the bay when you see a large ship in the distance. The boat begins to approach you and you start to realize that the ship is full of pirate otters.
"""
cove_info_2 = """
You arrive at Pirate's Cove. You found a boat along the shore and decide to take it. You sail towards the center of the bay when you see a large ship floating in the water. You begin to approach the boat and remember the pirate otters you defeated previously. To the west you can see a river leading towards the forest. To the south you see the edge of the bay and a path leading from it.

What would you like to do?
- Go [West]
- Go [South]
"""
market_info = """
 You arrive at the market. Different animals bustle through the marketplace searching for random items. Vendors set up with their booths selling various goods. One vendor has a display of weapons on a rack. Another has a stand furnished with armor.

 What would you like to do?
 - Talk to the [Weapons] vendor
 - Talk to the [Armor] vendor
 - Go [North]
 - Go [South]
"""

def is_valid_character(character_name):
    return (
        character_name == "Rascal"
        or character_name == "Luna"
        or character_name == "Ted"
    )


def texttime_info(location: str, character: Character) -> None:
    if location == "Forest":
        texttime_2(forest_info)
    elif location == "Sanctuary":
        texttime_2(sanctuary_info)
    elif location == "Ruins":
        if skeleton_1.health > 0 or skeleton_2.health > 0:
            texttime_2(ruins_info_1)
            battle(character, skeleton_1, skeleton_2)
            if character.health > 0:
                texttime_2(
                    "To the east you see the forest where you started your journey. To the south you see a vast expanse of grasslands.\n\nWhat would you like to do?\n- Go [East]\n- Go [South]\n"
                )
        else:
            texttime_2(ruins_info_2)
    elif location == "Swamp":
        if gator_1.health > 0 or gator_2.health > 0:
            texttime_2(swamp_info_1)
            battle(character, gator_1, gator_2)
            if character.health > 0:
                texttime_1(
                    "The only path from the marsh is the one you came from.\n\nWhat would you like to do?\n- Go back to the [Path]\n"
                )
        else:
            texttime_2(swamp_info_2)
    elif location == "Tavern":
        texttime_2(tavern_info)
    elif location == "Plains":
        texttime_2(plains_info)
    elif location == "Den":
        if spider_1.health > 0 or spider_2.health > 0:
            texttime_2(den_info_1)
            battle(character, spider_1, spider_2)
            if character.health > 0:
                texttime_1(
                    "The only path from the den is the one you came from.\n\nWhat would you like to do?\n- Go back to the [Path]\n"
                )
        else:
            texttime_2(den_info_2)
    elif location == "Canyon":
        if vulture_1.health > 0 or vulture_2.health > 0:
            texttime_2(canyon_info_1)
            battle(character, vulture_1, vulture_2)
            if character.health > 0:
                texttime_2(
                    "To the north you can see lots of bright lights. To the west you can see the beginnings of the grasslands. To the east all you can see is sand.\n\nWhat would you like to do?\n- Go [North]\n- Go [West]\n- Go [East]\n"
                )
        else:
            texttime_2(canyon_info_2)
    elif location == "Cavern":
        if character.bats == False:
            texttime_2(cavern_info_1)
        else:
            texttime_1(
                "You aren't allowed into the Blackbrook Caverns any more. Your cavern privileges have been revoked.\n"
            )
    elif location == "Desert":
        if snake.health > 0:
            texttime_2(desert_info_1)
            battle(character, snake, blank)
            if character.health > 0:
                texttime_1(
                    "To the north there is sand. To the west there is more sand.\n\nWhat would you like to do?\n- Go [North]\n- Go [West]\n"
                )
        else:
            texttime_2(desert_info_2)
    elif location == "Badlands":
        if character.key == False:
            texttime_2(badlands_info_1)
        else:
            texttime_2(badlands_info_2)
        character.badlands = True
    elif location == "Shores":
        texttime_2(shores_info)
    elif location == "Cove":
        if otter_1.health > 0 or otter_2.health > 0:
            texttime_2(cove_info_1)
            battle(character, otter_1, otter_2)
            if character.health > 0:
                texttime_2(
                    "To the west you can see a river leading towards the forest. To the south you see the edge of the bay and a path leading from it.\n\nWhat would you like to do?\n- Go [West]\n- Go [South]\n"
                )
        else:
            texttime_2(cove_info_2)
    elif location == "Market":
	    texttime_2(market_info)
    elif location == "Path 1":
        texttime_2(path_1_info)
    elif location == "Path 2":
        texttime_2(path_2_info)
    elif location == "Path 3":
        texttime_2(path_3_info)
    elif location == "Path 4":
        texttime_2(path_4_info)
    elif location == "Path 5":
        texttime_2(path_5_info)


def is_valid_transition(location: str, action: str) -> bool:
    if location == "Forest":
        return action == "West" or action == "East" or action == "South"
    elif location == "Path 1":
        return action == "West" or action == "South" or action == "East"
    elif location == "Ruins":
        return action == "East" or action == "South"
    elif location == "Path 2":
        return (
            action == "North"
            or action == "South"
            or action == "East"
            or action == "West"
        )
    elif location == "Plains":
        return action == "North" or action == "East"
    elif location == "Path 3":
        return action == "North" or action == "West" or action == "East"
    elif location == "Canyon":
        return action == "North" or action == "West" or action == "East"
    elif location == "Market":
        return action == "North" or action == "South"
    elif location == "Path 4":
        return action == "East" or action == "West" or action == "South"
    elif location == "Desert":
        return action == "North" or action == "West"
    elif location == "Path 5":
        return (
            action == "North"
            or action == "West"
            or action == "East"
            or action == "South"
        )
    elif location == "Cove":
        return action == "West" or action == "South"
    elif location == "Sanctuary":
        return action == "Path"
    elif location == "Shores":
        return action == "Path"
    elif location == "Badlands":
        return action == "Path"
    elif location == "Tavern":
        return action == "Path"
    elif location == "Swamp":
        return action == "Path"
    elif location == "Den":
        return action == "Path"
    elif location == "Cavern":
        return action == "Path"
    else:
        return False


def change_location(location: str, action: str, char: Character) -> str:
    if location == "Forest":
        if action == "West":
            return "Path 1"
        elif action == "South":
            return "Market"
        elif action == "East":
            return "Cove"
    elif location == "Path 1":
        if action == "East":
            return "Forest"
        elif action == "West":
            return "Ruins"
        elif action == "South":
            return "Sanctuary"
    elif location == "Sanctuary":
        return "Path 1"
    elif location == "Ruins":
        if action == "East":
            return "Path 1"
        elif action == "South":
            return "Path 2"
    elif location == "Path 2":
        if action == "North":
            return "Ruins"
        elif action == "East":
            return "Tavern"
        elif action == "West":
            return "Swamp"
        elif action == "South":
            return "Plains"
    elif location == "Tavern":
        return "Path 2"
    elif location == "Swamp":
        return "Path 2"
    elif location == "Plains":
        if action == "North":
            return "Path 2"
        elif action == "East":
            return "Path 3"
    elif location == "Path 3":
        if action == "North":
            return "Den"
        elif action == "West":
            return "Plains"
        elif action == "East":
            return "Canyon"
    elif location == "Den":
        return "Path 3"
    elif location == "Market":
        if action == "North":
            return "Forest"
        elif action == "South":
            return "Canyon"
    elif location == "Canyon":
        if action == "West":
            return "Path 3"
        elif action == "North":
            return "Market"
        elif action == "East":
            return "Path 4"
    elif location == "Path 4":
        if action == "West":
            return "Canyon"
        elif action == "East":
            return "Desert"
        elif action == "South":
            return "Cavern"
    elif location == "Desert":
        if action == "West":
            return "Path 4"
        elif action == "North":
            return "Path 5"
    elif location == "Path 5":
        if action == "North":
            return "Cove"
        elif action == "West":
            return "Shores"
        elif action == "East":
            return "Badlands"
        elif action == "South":
            return "Desert"
    elif location == "Shores":
        return "Path 5"
    elif location == "Badlands":
        return "Path 5"
    elif location == "Cove":
        if action == "West":
            return "Forest"
        elif action == "South":
            return "Path 5"
    elif location == "Cavern":
        return "Path 4"


def invalid_action_message():
    texttime_1("ERRORhjkfERRORsagkdjgERRORkfaERROR\n")


def armor_vendor(character: Character) -> None:
    if character.armor_vendor == False:
        texttime_2(
            "\nYou approach the armor vendor's booth. You talk to the armor vendor - a dragon.\nDragon: Hey, what's up friend? The name's Richard. You tryna get some armor? I've got the best kind don't you worry.\n\nWhat would you like to do?\n- Buy the [Boots] - +15 Speed - 100 berries\n- Buy the [Chestplate] - +50 Health - 100 berries\n- [Leave] this conversation\n\n"
        )
        character.armor_vendor = True
    else:
        texttime_1(
            "\nYou approach the armor vendor's booth to talk to Richard.\nRichard: Hey, what's up friend? Back again for more? I know you just love my armor.\n\nWhat would you like to do?\n- [Leave] this conversation"
        )
        if character.chestplate == True:
            pass
        else:
            texttime_1("\n- Buy the [Chestplate] - +50 Health - 100 berries")
        if character.boots == True:
            pass
        else:
            texttime_1("\n- Buy the [Boots] - +15 Speed - 100 berries")
    user_action = input("\n> ").title()
    if user_action == "Boots":
        if character.berries >= 100 and character.boots == False:
            texttime_1("\nRichard: Here you go friend. A brand new pair of boots.")
            character.berries -= 100
            character.speed += 15
            character.boots = True
        elif character.boots == True:
            texttime_1(
                "\nRichard: C'mon man, you can't take all my boots. I need to sell some to other customers."
            )
        else:
            texttime_1(
                "\nRichard: Sorry pal. Come back with more berries and these boots will be all yours."
            )
    elif user_action == "Chestplate":
        if character.berries >= 100 and character.chestplate == False:
            texttime_1(
                "\nRichard: There you go. A shiny chestplate, just for you. That will help you in combat."
            )
            character.berries -= 100
            character.health += 50
            character.chestplate = True
        elif character.chestplate == True:
            texttime_1("\nRichard: You don't need two chestplates!! No deal!")
        else:
            texttime_1(
                "\nRichard: Sorry pal. Come back with more berries and this chestplate will be all yours."
            )
    elif user_action == "Leave":
        pass
    else:
        texttime_1("\nThat is not a valid action.")


def weapons_vendor(character: Character) -> None:
    if character.weapons_vendor == False:
        texttime_2(
            "\nYou approach the weapon vendor's booth. You talk to the weapons vendor - a lion.\nLion: Ayo, what's up man? How you doing? The name's Jacen by the way. Are you looking to upgrade your weapon? If you are, then I'm your lion.\n\nWhat would you like to do?\n- [Upgrade] your weapon - +10 damage - +10 crit damage - 100 berries\n- [Leave] this conversation\n\n"
        )
        character.weapons_vendor == True
    else:
        texttime_1(
            "\nYou approach the weapons vendor's booth to talk to Jacen.\nJacen: Ayo, welcome back man. Have you already upgraded your weapon? If not, then you probably should. Just saying.\n\nwhat would you like to do?\n- [Leave] this conversation"
        )
    if character.weapon == True:
        pass
    else:
        texttime_1(
            "\n- [Upgrade] your weapon - +10 damage - +10 crit damage - 100 berries"
        )
    user_action = input("\n> ")
    if user_action == "Upgrade":
        if character.berries >= 100 and character.weapon == False:
            texttime_1("\nJacen: Here you go man. Your new and improved weapon.")
            character.berries -= 100
            character.weapon = True
        elif character.weapon == True:
            texttime_1(
                "\nJacen: I don't think you can upgrade your weapon any more man. It's already pretty epic."
            )
        else:
            texttime_1(
                "\nJacen: Oof. I'm sorry man but you're gonna have to bring me some more berries next time if you want an epic weapon."
            )
    elif user_action == "Leave":
        pass
    else:
        texttime_1("\nThat is not a valid action.")


def bat_interaction_1(character: Character) -> None:
    texttime_2(
        "You walk up to the bats at the back of the cave.\nBat: Howdy pardner, how're you doing today. The name's Quinton. Most call me the Ghost Flyer. Anyways, I've just been holed up here for a while until all calms down outside. Embergaze and his minions ain't letting up anytime soon.\n\nWhat would you like to say?\n- Who is Embergaze? [1]\n- I'm sorry to hear that. [2]\n- You must be a scaredy bat. [3]\n\n"
    )
    user_action = input("> ")
    while True:
        if user_action == "1":
            texttime_2(
                "\nQuinton: You ain't heard o' Embergaze?!?You mustn't be from around these parts. Well Embergaze be this huge monster. Real meanlike. I ain't seen what he looking like, but a lot 'o his minions be wandering around this land. Embergaze stay holed up in 'is tower making them there troops do 'is bidding. I would confront 'im but I's too scared to do anything 'bout 'im.\n\nWhat would you like to say?\n- Don't worry, I'll take care of him. [1]\n- You should stop whining like a baby and go fight him like a man. [2]\n\n"
            )
            user_action = input("> ")
            if user_action == "1":
                texttime_1(
                    "\nQuinton: Well thank ya. That's mighty kind of ya. Let me know how that goes.\nYou leave.\n [Path]"
                )
                break
            elif user_action == "2":
                texttime_1(
                    "\nQuinton: Well that's terribly rude of ya to say. I reckon I shan't be talking to yehs anymore.\nYou leave.\n"
                )
                character.bats = True
                break
            else:
                texttime_1("\nThat is not a valid input.")
        elif user_action == "2":
            texttime_2(
                "\nQuinton: Well that's mighty nice of ya, but that doesn't help the fact that that ole' bastard Embergaze is still raining 'is terror on ye' land. Would you mind taking care o' him.\n\nWhat would you like to say?\n- No problem. I'll take care of him for you.[1]\n- You can fight him yourself. [2]\n\n"
            )
            user_action = input("> ")
            if user_action == "1":
                texttime_1(
                    "\nQuinton: Well thank ya very much. I 'ppreciate it.\nYou leave.\n"
                )
                break
            elif user_action == "2":
                texttime_1(
                    "\nQuinton: Well that's not very nice of ye' ter say. I reckon you should skidaddle outta here.\n\nYou skidaddle outta there.\n"
                )
                character.bats = True
                break
            else:
                texttime_1("\nThat is not a valid input.")
        elif user_action == "3":
            texttime_2(
                "\nQuinton: Yeh didn't need to be that rude, traveler. Why don't yeh leave 'ere before I give you another enemy to worry 'bout.\n\nWhat would you like to say?\n- Fine [1]\n- You can't even fight someone you haven't even seen. What makes you think you can fight me? [2]\n\n"
            )
            user_action = input("> ")
            if user_action == "1":
                texttime_1("\nYou leave.\n")
                break
            elif user_action == "2":
                damagenum = random.randint(15, 30)
                character.health -= damagenum
                texttime_2(
                    f"\nQuinton: Yer tryin' ter test my patience ain't ya? Well so be it. I guess I'll have ter prove yehs wrong.\n\nQuinton starts attacking you. He lands a few hits, but you retreat out of the cave.\n\nPlayer Health: {character.health}\n\n"
                )
                character.bats = True
                break
            else:
                texttime_1("\nThat is not a valid input.")
        else:
            texttime_1("\nThat is not a valid input.")
    character.cave = True
    location = "Path 4"


def bat_interaction_2() -> None:
    texttime_1(
        "Welcome back pardner. Feel free to hang around here.\n\nYou leave. [Path] \n"
    )
    location = "Path 4"


def jack_interaction(character: Character) -> None:
    texttime_1("You walk over to the bunny to talk to him.")
    texttime_2(
        "\nBunny: Hey Buddy, how ya doing? You taking a peek at the ladies? I wouldn't blame ya if ya did. I can tell you're new around here. In this land I'm known as the Jack Rabbit, the Jack Widow, Jack of All Trades, the Jack Mamba. You call me whatever you like, ok bud? Anyways, while you're here could you grab me a Crispy Concord?"
    )
    texttime_1(
        f"\nWhat would you like to do?\nYou have {character.berries} berries.\n- Get him a [Drink]\n- [Refuse]"
    )
    user_action = input("\n> ").title()
    if user_action == "Drink":
        texttime_1(
            "You go to the bar to get a Crispy Concord. You pay the bartender 15 berries and back to the table. You hand the Jack Rabbit his drink.\n\n"
        )
        texttime_1(
            "Jack Rabbit: Thanks buddy. Since you were kind enough to pay for my drink I'll give you some more berries.\n\nWhat would you like to do?\n- Talk to the [Mouse]\n- Go back to the [Path]\n"
        )
        character.berries += 15
    elif user_action == "Refuse":
        texttime_1(
            "Jack Rabbit: You're just gonna leave me hanging? Fine then, I'll get my own drink. HEY! BARTENDER! GET ME ANOTHER ROUND WOULD YA!"
        )
        texttime_1("\nYou leave.")
        location = "Path 2"
    else:
        texttime_1("\nThat is not a valid input.")


def information(character: Character) -> None:
    if character.badlands == True:
        texttime_1(
            "What do you want to know about?\n- Why are there [Enemies] everywhere?\n- Where is the [Market]?\n- How do you unlock the [Tower] in the Badlands?\n- [Leave] this conversation\n"
        )
    else:
        texttime_1(
            "What do you want to know about?\n- Why are there [Enemies] everywhere?\n- Where is the [Market]?\n- [Leave] this conversation\n"
        )
    user_input = input("> ").title()
    if user_input == "Enemies":
        texttime_2(
            "\nBiggie Cheese: Them enemies are all minions. Embergaze the Death Bringer they calls him. He's a mythical being from a far away land. Nobody knows where he came from. He just showed up 'ere one day and took over the land. Nobody knows what he looks like either. He only ever stay in 'is tower across the land, closer to the cove. Yeh'd be mad if yeh'd tried to find 'im.\n\nYou leave the conversation.\n\n"
        )
    elif user_input == "Market":
        texttime_2(
            "\nBiggie Cheese: The market yeh' say? The market's not too far from 'ere pal. So you see you gotta head over to the forest just northeast o' here. Then yous gotta go souths from there. And badda bing badda boom, yeh've found yourself the market.\n\nYou leave the conversation.\n\n"
        )
    elif user_input == "Tower" and character.badlands == True:
        texttime_1(
            "\nBiggie Cheese: Embergaze's tower?!?! Well I dunno too much about his tower, but I reckon you'd find some clues from some o' his minions.\n\nYou leave the conversation.\n\n"
        )
    elif user_input == "Leave":
        texttime_1("\nBiggie Cheese: Fine then! I didn't wanna talk to ye's anyways!")
        location = "Path 2"
    else:
        texttime_1("\nThat is not a valid action!")


def drink(character: Character) -> None:
    texttime_2(
        f"\nBiggie Cheese: What would you like to drink?\nYou have {character.berries} berries.\n- Crisp Concord\n- Junior Jealousy\n- Maliable Malfeasant\n- Fairly Feasible\n- Go back to the [Path]\n"
    )
    user_drink = input("> ").title()
    if user_drink == "Crisp Concord":
        texttime_1(
            "\nYou order a Crisp Concord. Biggie Cheese passes you a glass. You hand Biggie Cheese 15 berries.\n"
        )
        character.berries -= 15
    elif user_drink == "Junior Jealousy":
        texttime_1(
            "\nYou order a Junior Jealousy. Biggie Cheese hands you a glass. You give Biggie Cheese 15 berries.\n"
        )
        character.berries -= 15
    elif user_drink == "Maliable Malfeasant":
        texttime_1(
            "\nYou order a Maliable Malfeasant. Biggie Cheese slides a glass over. You hand Biggie Cheese 15 berries.\n"
        )
        character.berries -= 15
    elif user_drink == "Fairly Feasible":
        texttime_1(
            "\nYou order a Fairly Feasible. Biggie Cheese pours you a glass. You give Biggie Cheese 15 berries.\n"
        )
        character.berries -= 15
    elif user_drink == "Path":
        texttime_1("\nBiggie Cheese: Waste my time why don't cha, pal?!?\n")
        location = "Path 2"
    else:
        texttime_1("\nThat is not a valid input.")


def mouse_interaction(character: Character) -> None:
    if character.mouse == False:
        texttime_1("You walk up to the bar to talk to the mouse.")
        texttime_2(
            "\n\nMouse: Hey pal, welcome to the Salty Spitoon. I'm the Head Mouse here. The name's Biggie Cheese. You want some information or some rounds to tickle your taste buds, you let me know. K pal?"
        )
        character.mouse = True
    else:
        texttime_1("You walk up to the bar to talk to Biggie Cheese.\n")
        texttime_1(
            "Biggie Cheese: Welcome back pal. Back for some more rounds or a bit of info?"
        )
    texttime_1(
        "What would you like to do?\n- Get some [Info]\n- Buy a [Drink]\n- Go back to the [Path]"
    )
    user_input = input("\n> ").title()
    if user_input == "Info":
        information(character)
    elif user_input == "Drink":
        drink(character)
    elif user_input == "Path":
        texttime_1("Alright. See ya later pal.")
        location = "Path 2"


def boss_dialogue() -> None:
    texttime_2(
        """\nYou might be wondering why I'm doing this. You wouldn't understand. Everything was tWhether it was a bountiful harvest, or keeping away the drought, I did everything for them. But lowly creatures being the filth they are, they sought to seek my power for themselves. They maimed me. I only had passive powers, so I didn't know how to fight back.
My hatred transformed me. That's why I decided to make life for you miserable beings a living hell!!!
"""
    )


def input_action(location: str, character: Character, boss: Enemy) -> str:
    while True:
        action = input("> ").title()
        if is_valid_transition(location, action):
            return change_location(location, action, character)
        elif action == "Berry Amount":
          texttime_1(f"\nYou have {character.berries} berries!\n\n")
        elif location == "Market" and action == "Armor":
            armor_vendor(character)
            texttime_1(market_info)
        elif location == "Market" and action == "Weapons":
            weapons_vendor(character)
            texttime_1(market_info)
        elif location == "Cavern" and action == "Bats":
            if character.cave == False:
                bat_interaction_1(character)
            else:
                bat_interaction_2()
        elif location == "Cavern" and action == "Berries":
            texttime_1("You stole the berries. The bats will remember that.\n [Path]")
            character.berries += 50
            character.bats = True
            # location = "Path 4"
        elif location == "Tavern" and action == "Jack":
            jack_interaction(character)
            texttime_2(tavern_info)
        elif location == "Tavern" and action == "Mouse":
            mouse_interaction(character)
            texttime_2(tavern_info)
        elif location == "Sanctuary" and action == "Heal":
            if character.heals <= 0:
                texttime_1(
                    "Randy: I can't heal you! I've got other patients to treat! You must suffer!"
                )
            else:
                texttime_1(
                    "Randy: Don't sweat it man! You let me take care of you!\n\nRandy healed you to max health\n\n"
                )
                character.heals -= 1
                if character.chestplate == True:
                    if character.name == "Rascal":
                        character.health = 250
                    elif character.name == "Luna":
                        character.health = 300
                    else:
                        character.health = 350
                else:
                    if character.name == "Rascal":
                        character.health = 200
                    elif character.name == "Luna":
                        character.health = 250
                    else:
                        character.health = 300
                texttime_1(f"Player Health: {character.health}\n")
                texttime_1(
                    "\nWhat would you like to do?\n- [Heal]\n- Go back to the [Path]\n"
                )
        elif location == "Badlands" and character.key == True and action == "Enter":
            boss_battle(character, boss, blank)
        elif boss.health < 0 or character.health < 0:
          break
        else:
            invalid_action_message()

def user_attack(char: Character, enemy_1: Enemy, enemy_2: Enemy) -> None:
    global attack
    attacknum = random.randint(1, 20)
    ##################################
    # Rascal
    ##################################
    # miss attack
    if char.name == "Rascal":
        texttime_1(
            "\nWhat would you like to do?\n- Deadshot\n- Arrow Storm\n- Tactical Whack\n"
        )
        attack = input("\n> ").title()
        if attack == "Deadshot":
            target = input("Who do you want to target?").title()
            if target == enemy_1.name or target == enemy_2.name:
                if attacknum <= 4:
                    texttime_1(f"You missed.")
                elif attacknum > 4 and attacknum < 18:
                    if char.weapon == True:
                        damagenum = random.randint(41, 50)
                    else:
                        damagenum = random.randint(30, 40)
                    if target == enemy_1.name:
                        enemy_1.health -= damagenum
                        texttime_1(f"You hit {enemy_1.name} for {damagenum} damage!")
                    else:
                        enemy_2.health -= damagenum
                        texttime_1(f"You hit {enemy_2.name} for {damagenum} damage!")
                else:
                    if char.weapon == True:
                        damagenum = random.randint(51, 60)
                    else:
                        damagenum = random.randint(41, 50)
                    if target == enemy_1.name:
                        enemy_1.health -= damagenum
                        texttime_1(
                            f"You did {damagenum} critical hit damage to {enemy_1.name}"
                        )
                    else:
                        enemy_2.health -= damagenum
                        texttime_1(
                            f"You did {damagenum} critical hit damage to {enemy_2.name}"
                        )
            else:
                texttime_1("That is not a valid target.")
        elif attack == "Arrow Storm":
            if attacknum <= 6:
                texttime_1(
                    f"You grab two arrows, draw them back, and shoot at your enemies. You missed."
                )
            elif attacknum > 6 and attacknum < 18:
                if char.weapon == True:
                    damagenum = random.randint(26, 35)
                else:
                    damagenum = random.randint(20, 25)
                enemy_1.health -= damagenum
                enemy_2.health -= damagenum
                texttime_1(
                    f"You grab two arrows, draw them back, and shoot at your enemies. You landed the attack!"
                )
                texttime_1(f"You do {damagenum} damage!")
            else:
                if char.weapon == True:
                    damagenum = random.randint(36, 45)
                else:
                    damagenum = random.randint(26, 35)
                    enemy_1.health -= damagenum
                    enemy_2.health -= damagenum
                    texttime_1(
                        "You grab two arrows, draw them back, and shoot at the enemies. You landed a critical hit!"
                    )
        elif attack == "Tactical Whack":
            target = input("Who do you want to target? ").title()
            if target == enemy_1.name or target == enemy_2.name:
                if attacknum <= 2:
                    texttime_1(f"You swing your bow at {target}, but you missed.")
                elif attacknum > 2 and attacknum < 18:
                    if char.weapon == True:
                        damagenum = random.randint(31, 40)
                    else:
                        damagenum = random.randint(20, 30)
                        texttime_1(
                            f"You swing your bow at {target}. You have successfully whacked them on the head!"
                        )
                    if target == enemy_1.name:
                        enemy_1.health -= damagenum
                    elif target == enemy_2.name:
                        enemy_2.health -= damagenum
                else:
                    if char.weapon == True:
                        damagenum = random.randint(41, 50)
                    else:
                        damagenum = random.randint(31, 40)
                        texttime_1(
                            f"You swing your bow extra hard at {target}. You have successfully whacked them on the head! Geez, that's gotta leave a mark."
                        )
                        if target == enemy_1.name:
                            enemy_1.health -= damagenum
                        elif target == enemy_2.name:
                            enemy_2.health -= damagenum
            else:
                texttime_1("That is not a valid target.")
        else:
            texttime_1("Please choose a valid attack.")
    ##################################
    # LUNA
    ##################################
    elif char.name == "Luna":
        texttime_1(
            "\nWhat would you like to do?\n- Frontal Slash\n- Sword Dance\n- Piercing Strike\n"
        )
        attack = input("\n> ").title()
        if attack == "Frontal Slash":
            target = input("Who do you want to target?").title()
            if target == enemy_1.name or target == enemy_2.name:
                # miss
                if attacknum <= 4:
                    texttime_1(f"You swung at the enemy, but you missed.")
                # normal attack damage
                elif attacknum > 4 and attacknum < 17:
                    if char.weapon == True:
                        damagenum = random.randint(36, 45)
                    else:
                        damagenum = random.randint(25, 35)
                    if target == enemy_1.name:
                        enemy_1.health -= damagenum
                        texttime_1(f"You hit {enemy_1.name} for {damagenum} damage!")
                    else:
                        enemy_2.health -= damagenum
                        texttime_1(f"You hit {enemy_2.name} for {damagenum} damage!")
                # critical hit
                else:
                    if char.weapon == True:
                        damagenum = random.randint(46, 55)
                    else:
                        damagenum = random.randint(36, 45)
                    if target == enemy_1.name:
                        enemy_1.health -= damagenum
                        texttime_1(
                            f"You did {damagenum} critical hit damage to {enemy_1.name}"
                        )
                    else:
                        enemy_2.health -= damagenum
                        texttime_1(
                            f"You did {damagenum} critical hit damage to {enemy_2.name}"
                        )
            else:
                texttime_1("That is not a valid target.")
        elif attack == "Sword Dance":
            # miss
            if attacknum <= 6:
                texttime_1(f"You swung at your enemies, but you missed.")
            # normal attack damage
            elif attacknum > 6 and attacknum < 18:
                if char.weapon == True:
                    damagenum = random.randint(26, 35)
                else:
                    damagenum = random.randint(15, 25)
                enemy_1.health -= damagenum
                enemy_2.health -= damagenum
                texttime_1(f"You dance around your enemies and slash them!")
                texttime_1(f"You do {damagenum} damage!")
            # critical hit
            else:
                if char.weapon == True:
                    damagenum = random.randint(46, 55)
                else:
                    damagenum = random.randint(36, 45)
                    enemy_1.health -= damagenum
                    enemy_2.health -= damagenum
                texttime_1(
                    f"You leap towards your enemies brandishing your sword and dealt {damagenum} critical damage to all enemies."
                )
        elif attack == "Piercing Strike":
            # miss
            target = input("Who do you want to target? ").title()
            if target == enemy_1.name or target == enemy_2.name:
                if attacknum <= 2:
                    texttime_1(f"You swing your sword at {target}, but you missed.")
                # normal attack damage
                elif attacknum > 2 and attacknum < 18:
                    if char.weapon == True:
                        damagenum = random.randint(31, 40)
                    else:
                        damagenum = random.randint(20, 30)
                    texttime_1(
                        f" You swing your sword at {target}. You have successfully dealt {damagenum} damage!"
                    )
                    if target == enemy_1.name:
                        enemy_1.health -= damagenum
                    elif target == enemy_2.name:
                        enemy_2.health -= damagenum
                # critical hit
                else:
                    if char.weapon == True:
                        damagenum = random.randint(41, 50)
                    else:
                        damagenum = random.randint(31, 40)
                    texttime_1(
                        f"You lunge at {target} and pierce them. You deal {damagenum} critical damage!"
                    )
                    if target == enemy_1.name:
                        enemy_1.health -= damagenum
                    elif target == enemy_2.name:
                        enemy_2.health -= damagenum
            else:
                texttime_1("That is not a valid target.")
        else:
            texttime_1("Please choose a valid attack.")
    ##################################
    # TED
    ##################################
    elif char.name == "Ted":
        texttime_1(
            "\nWhat would you like to do?\n- Crushing Blow\n- Earthquake\n- Fatal Chop\n"
        )
        attack = input("\n> ").title()
        if attack == "Crushing Blow":
            target = input("Who do you want to target?")
            if target == enemy_1.name or target == enemy_2.name:
                if attacknum <= 4:
                    texttime_1(f"You swing your axe in the air and missed.")
                elif attacknum > 4 and attacknum < 18:
                    if char.weapon == True:
                        damagenum = random.randint(36, 45)
                    else:
                        damagenum = random.randint(25, 35)
                        if target == enemy_1.name:
                            enemy_1.health -= damagenum
                            texttime_1(
                                f"You swing your axe and hit {enemy_1.name} for {damagenum} damage!"
                            )
                        else:
                            enemy_2.health -= damagenum
                            texttime_1(
                                f"You swing your axe and hit {enemy_2.name} for {damagenum} damage!"
                            )
                else:
                    if char.weapon == True:
                        damagenum = random.randint(46, 55)
                    else:
                        damagenum = random.randint(35, 45)
                        if target == enemy_1.name:
                            enemy_1.health -= damagenum
                            texttime_1(
                                f"You throw your axe at {enemy_1.name} and did {damagenum} critical hit damage."
                            )
                        else:
                            enemy_2.health -= damagenum
                            texttime_1(
                                f"You throw your axe at {enemy_1.name} and did {damagenum} critical hit damage."
                            )
            else:
                texttime_1("That is not a valid target.")
        elif attack == "Earthquake":
            if attacknum <= 6:
                texttime_1(
                    f" You jump up and attempt to throw your axe into the ground. It slapped the ground horizontally."
                )
            elif attacknum > 6 and attacknum < 18:
                if char.weapon == True:
                    damagenum = random.randint(26, 35)
                else:
                    damagenum = random.randint(15, 25)
                    enemy_1.health -= damagenum
                    enemy_2.health -= damagenum
                    texttime_1(
                        f"You jump up and throw your axe into the ground. The ground begins to shake and the earth slighly opens up."
                    )
                    texttime_1(f"You do {damagenum} damage to both enemies")
            else:
                if char.weapon == True:
                    damagenum = random.randint(36, 45)
                else:
                    damagenum = random.randint(26, 35)
                    enemy_1.health -= damagenum
                    enemy_2.health -= damagenum
                    texttime_1(
                        "You jump up and throw your axe into the ground. The ground begins to shake and you open up a large hole in the earth."
                    )
                    texttime_1(
                        f"You do {damagenum} critical damage to {enemy_1.name} and {enemy_2.name}"
                    )
        elif attack == "Fatal Chop":
            target = input("Who do you want to target? ").title()
            if target == enemy_1.name or target == enemy_2.name:
                if attacknum <= 2:
                    texttime_1(f"He swings.......and he misses.")
                elif attacknum > 2 and attacknum < 18:
                    if char.weapon == True:
                        damagenum = random.randint(31, 40)
                    else:
                        damagenum = random.randint(20, 30)
                    texttime_1(f"You swing your axe at {target}.")
                    texttime_1(f"You do {damagenum} damage!")
                    if target == enemy_1.name:
                        enemy_1.health -= damagenum
                    elif target == enemy_2.name:
                        enemy_2.health -= damagenum
                else:
                    if char.weapon == True:
                        damagenum = random.randint(41, 50)
                    else:
                        damagenum = random.randint(31, 40)
                        texttime_1(
                            f"You swing your axe at {target}. Oh my god... I think you might have cut something off. Geez, that's gotta leave a mark."
                        )
                        texttime_1(f"You do {damagenum} damage!")
                        if target == enemy_1.name:
                            enemy_1.health -= damagenum
                        elif target == enemy_2.name:
                            enemy_2.health -= damagenum
        else:
            texttime_1("That is not a valid target.")
    else:
        texttime_1("Please choose a valid attack.")


def enemy_attack(char: Character, enemy_1: Enemy, enemy_2: Enemy) -> None:
    hit_chance_1 = random.randint(1, 20)
    hit_chance_2 = random.randint(1, 20)
    if enemy_1.health > 0:
        if hit_chance_1 <= 8:
            texttime_1(f"\n{enemy_1.name} attacked you, but they missed!!")
        else:
            texttime_1(
                f"\n{enemy_1.name} attacked you, and did {enemy_1.damage} damage!"
            )
            char.health -= enemy_1.damage
    if enemy_2.health > 0:
        if hit_chance_2 <= 6:
            texttime_1(f"\n{enemy_2.name} attacked you, but they missed!!\n")
        else:
            texttime_1(
                f"\n{enemy_2.name} attacked you, and did {enemy_2.damage} damage!\n"
            )
            char.health -= enemy_2.damage


def battle(char: Character, enemy_1: Enemy, enemy_2: Enemy) -> None:
    if char.speed >= enemy_1.speed or char.speed >= enemy_2.speed:
        texttime_1("\nYou are faster than your enemies! You attack first.\n")
    else:
        texttime_1("\nYou're too slow! Your enemies attack first.\n")
    while char.health > 0:
        while enemy_1.health > 0 or enemy_2.health > 0:
            texttime_1(f"\nPlayer Health: {str(char.health)}")
            if enemy_1.health > 0:
                texttime_1(f"\n{enemy_1.name} Health: {str(enemy_1.health)}")
            if enemy_2.health > 0:
                texttime_1(f"\n{enemy_2.name} Health: {str(enemy_2.health)}\n")
                if char.speed >= enemy_1.speed or char.speed >= enemy_2.speed:
                    user_attack(char, enemy_1, enemy_2)
                    if enemy_1.health > 0 or enemy_2.health > 0:
                        enemy_attack(char, enemy_1, enemy_2)
                elif char.speed < enemy_1.speed or char.speed < enemy_2.speed:
                    enemy_attack(char, enemy_1, enemy_2)
                    if char.health > 0:
                        user_attack(char, enemy_1, enemy_2)
                break
        if enemy_1.health <= 0 and enemy_2.health <= 0:
            berrynum = random.randint(30, 40)
            texttime_1(
                f"\n\nYou have defeated you opponents! You have gained {berrynum} berries!\n\n"
            )
            char.berries += berrynum
            if enemy_1 == spider_1 and enemy_2 == spider_2:
                texttime_1(
                    "After defeating the spiders you find a golden key at the back of the den. You pick it up and store, for it might be useful later.\n\n"
                )
                char.key == True
            break
    if char.health <= 0:
        texttime_1(
            "\n\nYou're dogwater. Literal dog water. You have to start from the begining now.\n\n"
        )

def credits() -> None:
 texttime_1("""
-----------------------------------------------------
-----------------------------------------------------
---------------------- Credits ----------------------
-----------------------------------------------------
-----------------------------------------------------
---------------- Into The Thick Of It ---------------
-----------------------------------------------------
-------------------- Created By: --------------------
-----------------------------------------------------
-------------------- Isaac Jones --------------------
-----------------------------------------------------
------------------------ And ------------------------
-----------------------------------------------------
------------------- Dylan Shipton -------------------
-----------------------------------------------------
-----------------------------------------------------
-----------------------------------------------------
-----------------------------------------------------
----------- Title Assigner: Randy Trullet -----------
-----------------------------------------------------
-----------------------------------------------------
----------- Item Appointer: Jack Russell ------------
-----------------------------------------------------
-----------------------------------------------------
----------- Head of Testing: Ryan Bennett -----------
-----------------------------------------------------
-----------------------------------------------------
-----------------------------------------------------
-----------------------------------------------------
---------------- Special Thanks To: -----------------
-----------------------------------------------------
-----------------------------------------------------
------------------ Jacen Barefoot -------------------
-----------------------------------------------------
------------------- Richard Tutor -------------------
-----------------------------------------------------
------------------- Randy Trullet -------------------
-----------------------------------------------------
------------------- Jack Russell --------------------
-----------------------------------------------------
------------------------ And ------------------------
-----------------------------------------------------
---------------- Quinton Summerford -----------------
-----------------------------------------------------
-----------------------------------------------------
-----------------------------------------------------
-----------------------------------------------------
-----------------------------------------------------
-----------------------------------------------------
--------------- Thank You For Playing ---------------
-----------------------------------------------------
--------------- Into The Thick Of It ----------------
-----------------------------------------------------
-----------------------------------------------------
-----------------------------------------------------
"""
)


def boss_battle(char: Character, boss: Enemy, blank: Enemy) -> None:
    texttime_1("You walk up to the tower to confront Ember Gaze.")
    boss_dialogue()
    if char.speed >= boss.speed:
        texttime_1(
            f"""
You are faster than {boss.name}! You attack first."""
        )
    else:
        texttime_1(
            f"""
You're too slow! {boss.name} attacks first."""
        )
    bats_do_thing = 1
    while char.health > 0:
        if boss.health > 0:
            texttime_1(
                f"""
Player Health: {str(char.health)}"""
            )
            if boss.health > 0:
                texttime_1(
                    f"""
{boss.name} Health: {str(boss.health)}"""
                )
            if char.speed >= boss.speed:
                user_attack(char, boss, blank)
                enemy_attack(char, boss, blank)
            else:
                enemy_attack(char, boss, blank)
                user_attack(char, boss, blank)
            if char.health <= 20:
                if char.bats == False:
                  if bats_do_thing == 1:
                    texttime_1(
                        """
You are almost dead! You look over and see Quinton, the Ghost Flyer. He remembers how friendly you were to him. Quinton does a thing."""
                    )
                    char.health += 100
                    bats_do_thing -= 1
                else:
                    texttime_1(
                        """
You are almost dead! You look over and see Quinton, the Ghost Flyer. He is mad you stole his berries. Quinton watches you die slowly."""
                    )
        elif boss.health <= 0:
          texttime_1(
            """
You did it. You have stopped Ember Gaze's reign of Terror""")
          credits()
          break
    if char.health <= 0:
      char.health = 0
      texttime_1(
            "You're dogwater. Literal dog water. You have to start from the begining now."
        )


def choose_character() -> None:
    while True:
        user_input = input("> ").title()
        if not is_valid_character(user_input):
            texttime_1("Please choose a valid character.")
        else:
            if user_input == "Rascal":
                texttime_2(rascal_info)
                character = Character(
                    "Rascal",
                    200,
                    70,
                    3,
                    0,
                    False,
                    True,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                )
            elif user_input == "Luna":
                texttime_2(luna_info)
                character = Character(
                    "Luna",
                    250,
                    80,
                    3,
                    0,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                )
            elif user_input == "Ted":
                texttime_2(ted_info)
                character = Character(
                    "Ted",
                    300,
                    50,
                    3,
                    0,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                )
            else:
                pass
            return character
            break


def main() -> None:
	location = "Forest"
	character = choose_character()
	while True:
		  texttime_info(location, character)
		  location = input_action(location, character, boss)


if __name__ == "__main__":
        main()

