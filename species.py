from inventory import *


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
    def __init__(self, name, inventory, distance = 0, weakness = None):
        self.name = name
        self.inventory = inventory
        self.melee_weapon = None
        self.spell_weapon = None
        self.distance_from_player = distance
        self.weakness = weakness
        #Weakness is a list of all weaknesses

    def char_sheet(self, character, char_name):
        print(f'Character Name: {char_name}')
        print(f'\tInventory:', end = " ")
        for i in character.inventory.iteams:
            print(f'{i.name}', end = " ")
        print(f'\n\tGold: {character.inventory.gold}')
        print()


    def attack(self, target):
        pass

    def examine(self):
        #This lets you examine any enemey in a fight
        pass

    def change_melee_weapon(self, new_weapon):
        pass

    def change_spell_weapon(self, new_weapon):
        pass

    def loot(self, target):
        pass