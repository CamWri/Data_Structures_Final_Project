from colorama import *

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
    def __init__(self, name, strength, intelligence, resilience, agility, health, wisdom, charisma):
        self.name = name
        self.strength = strength
        self.intelligence = intelligence
        self.resilience = resilience
        self.agility = agility
        self.health = health
        self.wisdom = wisdom
        self.charisma = charisma

    def species_sheet(self, character, char_name):
        print(f'Character Name: {char_name}')
        print(f'Strength: {character.strength}')
        print(f'Intelligence: {character.intelligence}')
        print(f'Resilience: {character.resilience}')
        print(f'Agility: {character.agility}')
        print(f'Health: {character.health}')
        print(f'Wisdom: {character.wisdom}')
        print(f'Charisma: {character.charisma}')

    def get_attributes_asList(self):
        list = []
        list.append(self.strength)
        list.append(self.intelligence)
        list.append(self.resilience)
        list.append(self.agility)
        list.append(self.health)
        list.append(self.wisdom)
        list.append(self.charisma)
        return list

    def attribute(self, species, attriubte, number, points_left):
        print(f'Attribute {number} out of 7:\t', end="")
        species.attriubte = species.establish_attributes(attriubte)
        points_left = points_left - species.attriubte
        print(f'\t\tPoints Remaining:{points_left}\n', end="")

        return species.attriubte, points_left

    def establish_attributes(self, attribute):

        attribute_value = -1

        while (attribute_value <= -1 or attribute_value > 10):
            try:
                attribute_value = int(input(f'Please input the {attribute} of your species: '))
                if attribute_value == 0:
                    print('\t' + attribute_explanation[attribute] + '\n')
                    attribute_value = int(input(f'Please input the {attribute} of your species: '))
            except ValueError:
                print("Please input the {attribute} of your species with values from 0 to 10: \n")
                attribute_value = -1

        return attribute_value


    def character_attributes(self, player_species):
        print("\nYou will have a total of 40 points over 7 categories going from 1 - 10. For any of these, press '0' for information on this attribute.")
        print("Your attributes are strength, Intelligence, resilience, agility, health, wisdom and charisma")

        attributes_total = True

        while attributes_total:
            points_left = 40
            player_species.strength, points_left = self.attribute(player_species, "strength", 1, points_left)
            player_species.intelligence, points_left = self.attribute(player_species, "intelligence", 2, points_left)
            player_species.resilience, points_left = self.attribute(player_species, "resilience", 3, points_left)
            player_species.agility, points_left = self.attribute(player_species, "agility", 4, points_left)
            player_species.health, points_left = self.attribute(player_species, "health", 5, points_left)
            player_species.wisdom, points_left = self.attribute(player_species, "wisdom", 6, points_left)
            player_species.charisma, points_left = self.attribute(player_species, "charisma", 7, points_left)

            if points_left == 0:
                break
            else:
                print("\nPlease enter the attribute values that have a sum of 40 going from 1 - 10 where 0 is for information on the attribute")