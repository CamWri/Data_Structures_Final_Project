from inventory import *
from armor_weapon import *

attribute_explanation = {
    "strength": "Strength accounts for how strong your character is. The more you put into strength, the better your physical qualities and attributes are.",
    "intelligence": "Intelligence accounts for how clever your character is. The more you put into intelligence, the more knowledge you have, and the better ability to use logic and reasoning.",
    "resilience": "Resilience accounts for how much damage you mitigate from environmental and combative factors. The more you put into resiliencem the more harming factors you resist",
    "agility": "Agility determines your speed and your maneuvers against the environment, traps, and combative forces. The more you put into agility, the harder it is to hit you because you move and react faster.",
    "health": "Health determines how much damage you can take. The more you put into health, the more health you have.",
    "wisdom": "Wisdom accounts for how aware and intuitive your character is. The more you put into wisdom, the more vital clues and observations you can see. ",
    "charisma": "Charisma accounts for how persuasive you are. The more charismatic you are, the more you can talk your way out of things or get better deals."
    }


class character():
    def __init__(self, name, inventory, distance = 0, weakness = None, health = 0, weapon1 = fist, weapon2 = fist, turned = False):
        self.name = name
        self.inventory = inventory
        self.weapon1 = weapon1
        self.weapon2 = weapon2
        self.armor = Clothes
        self.distance_from_player = distance
        self.weakness = weakness
        self.health = health
        self.turned = turned
        self.dead = False

    def char_sheet(self):
        print(f'Enemy: {self.name}')
        print(f'Distance from you: {self.distance_from_player}')
        print(f"Health: {self.health}")
        print(f"Weakness: {', '.join(map(str.strip, self.weakness))}")
        if self.weapon1 == self.weapon2:
            print(f"Weapons: {self.weapon1.name}")
        else:
            if self.weapon1 is None:
                print(f"Weapon: {self.weapon2.name}")
            elif self.weapon2 is None:
                print(f"Weapon: {self.weapon1.name}")
            else:
                print(f"Weapons: {self.weapon1.name} and {self.weapon2.name}")
        print(f"Armor: {self.armor.name}")


    def attack(self, target):
        pass

    def loot(self, target):
        pass

    def sell_iteam(self, iteam, vendor):
        pass
        #Remove the iteam from the list
        #add the value of gold to the player

    def buy_iteam(self, iteam, vendor):
        pass
Corrupt_Guard_Inventory = Inventory(100, [Iron_Sword, Wood_Shield])
Corrupt_Guard = character(name = "Corrupt Guard", inventory = Corrupt_Guard_Inventory, weakness = ["electric", "ice"], health = 10, weapon1 = claws, weapon2 = claws, turned= True, distance=5)