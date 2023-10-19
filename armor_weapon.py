from time import *


class Sword:
    def __init__(self, name, damage, value, elemental = None, elemental_damage = 0):
        self.damage = damage
        self.value = value
        self.name = name
        self.range = 2
        self.type_of_damage = "slashing"
        self.type_of_damage2 = "thrusting"
        self.element = elemental
        self.elemental_damage = elemental_damage
        self.type = "weapon1"

    def attack(self, target):
        pass

    def examine(self):
        print(f"\tItem: {self.name}")
        print(f"\tValue: {self.value}")
        print(f"\tDamage: {self.damage}")
        print(f"\tElement: {self.element}")
        print(f"\tElement Damage: {self.elemental_damage}")
        print(f"\tType of Damage: {self.type_of_damage} and {self.type_of_damage2}")
        print(f"\tThe Range of this weapon: {self.range}")

Wood_Sword = Sword("Wooden Sword", 2, 5)
Bronze_Sword = Sword("Bronze Sword", 3, 15)
Flame_Sword = Sword("Flame Sword", 2, 25, elemental= "fire", elemental_damage= 2)
Iron_Sword = Sword("Iron Sword", 5,30)
Light_Bringer_Sword = Sword("Light Bringer Sword", 4, 100, elemental = "light", elemental_damage = 4)
Dark_Creators_Sword = Sword("Dark Creator's Sword", 7, 175, elemental = "darkness", elemental_damage = 3)
Celestial_Sword = Sword("Celestial Sword", 10, 2500, elemental = "celestial", elemental_damage = 5)


class Greatsword:
    def __init__(self, name, damage, value, elemental = None, elemental_damage = 0):
        self.damage = damage
        self.value = value
        self.name = name
        self.range = 3
        self.type_of_damage = "slashing"
        self.type_of_damage2 = None
        self.element = elemental
        self.elemental_damage = elemental_damage
        self.type = "weapon1"

    def attack(self, target):
        pass

    def examine(self):
        print(f"Item: {self.name}")
        print(f"Value: {self.value}")
        print(f"Damage: {self.damage}")
        print(f"Element: {self.element}")
        print(f"Element Damage: {self.elemental_damage}")
        print(f"Type of Damage: {self.type_of_damage}")
        print(f"The Range of this weapon: {self.range}")

Wood_Greatsword = Greatsword("Wooden Great Sword", 2, 7)
Bronze_Greatsword = Greatsword("Bronze Great Sword", 3, 20)
Earth_Imbued_Greatsword = Greatsword("Earth Imbued Greatsword", 4, 65, elemental = "earth", elemental_damage = 5)
Iron_Greatsword = Greatsword("Iron Great Sword", 7, 35)
Energized_Greatsword = Greatsword("Energized Greatsword", 7, 500, elemental="light", elemental_damage=5)
Celestial_Greatsword = Greatsword("Celestial Great Sword", 10, 2750, elemental = "celestial", elemental_damage = 7)




class Spear:
    def __init__(self, name, damage, value, elemental = None, elemental_damage = 0):
        self.damage= damage
        self.value = value
        self.name = name
        self.range = 3
        self.type_of_damage = "thrusting"
        self.type_of_damage2 = None
        self.element = elemental
        self.elemental_damage = elemental_damage
        self.type = "weapon1"

    def attack(self, targer):
        pass

    def examine(self):
        print(f"Item: {self.name}")
        print(f"Value: {self.value}")
        print(f"Damage: {self.damage}")
        print(f"Element: {self.element}")
        print(f"Element Damage: {self.elemental_damage}")
        print(f"Type of Damage: {self.type_of_damage}")
        print(f"The Range of this weapon: {self.range}")

Wood_Spear = Spear("Wooden Spear", 2, 5)
Bronze_Spear = Spear("Bronze Spear", 4, 13)
Iron_Spear = Spear("Iron Spear", 6, 35)
Ice_Spear = Spear("Ice Tipped Spear", 5, 35, elemental= "ice", elemental_damage= 5)
Calamity_Spear = Spear("Calamity Spear", 13, 500)
Celestial_Spear =  Spear("Celestial Spear", 12, 2700, elemental="celestial", elemental_damage= 10)


class Wand:
    def __init__(self, name, value, spells):
        self.name = name
        self.value = value
        self.spells = spells
        self.type_of_damage = "magical"
        self.type = "weapon2"

    def examine(self):
        print(f"\tItem: {self.name}")
        print(f"\tValue: {self.value}")
        for i in self.spells:
            i.examine()

    #Make sure to examine spells as well

class Spell:
    def __init__(self, name, damage = 0, heal = 0, armor= 0, range = 0, damage_increase = 0, elemental = None, elemental_damage = 0, num_targets = 1, radius = 0):
        self.name = name
        self.damage = damage
        self.heal = heal
        self.armor = armor
        self.range = range
        self.elemental = elemental
        self.elemental_damage = elemental_damage
        self.num_targets = num_targets
        self.damage_increase = damage_increase
        self.radius = radius

    def cast_spell(self):
        pass

    def examine(self):
        print(f"\t\tName of Spell: {self.name}")
        print(f'\t\t\t{self.name} Damage: {self.damage}')
        if self.elemental_damage != 0:
            print(f"\t\t\t{self.name} Element: {self.elemental}")
            print(f"\t\t\t{self.name} Elemental Damage: {self.elemental_damage}")
        if self.range == 0:
            print(f"\t\t\tThe Main Target is you or has no target")
        else:
            print(f"\t\t\t{self.name} Range: {self.range}")#have it to where if it is = 0, then it states only affects you/cast is from where you are
        if self.heal != 0:
            print(f"\t\t\t{self.name} Healing: {self.heal}")
        if self.armor !=0:
            print(f"\t\t\t{self.name} Armor Increase: {self.armor}")
        if self.num_targets != 1:
            print(f"\t\t\t{self.name} Number of Targers: {self.num_targets}")
        if self.radius != 0:
            print(f"\t\t\t{self.name} Damage Radius: {self.radius}")
        if self.damage_increase != 0:
            print(f"\t\t\t{self.name} Damage Increase: {self.damage_increase}")
        sleep(1)


#Fire Spells
Flame_Orb = Spell("Flame Orb", damage = 1, range = 6, elemental = "fire", elemental_damage = 4)
Firebolt = Spell("Firebolt", damage = 3, range = 10, elemental = "fire", elemental_damage = 5)
Flame_Barrier = Spell("Flame Barrier", armor = 3, range = 1, damage_increase = 2, elemental_damage = 2)
Dragons_Breath = Spell("Dragons Breath", elemental = "fire", range = 0, elemental_damage = 9, radius = 10) #For this spell, do damage to all enemies within the range of 10
Incinerate = Spell("Incinerate", damage = 5, range = 10, elemental = "fire", elemental_damage = 15)

#Electric Spells
Spark = Spell("Spark", damage = 2, range = 8, elemental = "electric", elemental_damage=2)
Electric_Veins = Spell("Electric Veins", damage_increase=5)
Chain_Lightning = Spell("Chain Lightning", damage = 3, range = 15, elemental= "electric", elemental_damage= 3, num_targets=5)
Electrical_Surge = Spell("Electrical_Surge", damage = 5, elemental="electric", elemental_damage=5, radius = 5)
Thunder = Spell("Thunder", damage = 25, range = 20, damage_increase= -1, armor=-1, elemental = "electric", elemental_damage=25)

#Eath/Ground Spells
Vine_Grip = Spell("Vine Grip", damage = 1, range = 5, elemental = "earth", elemental_damage=2, num_targets=3)
Rock_Blast = Spell("Rock Blast", damage = 3, range = 10, elemental = "earth", elemental_damage=6)
Earthen_Bulk = Spell("Earthen Bulk", armor = 5, damage_increase= 2, heal=2)
Earthquake = Spell("Earthquake", damage = 15, range = 5, elemental = "earth", elemental_damage=10, radius = 3)

Water_Bubble = Spell("Water Bubble", damage = 2, range = 10, elemental="water", elemental_damage=1)
Water_Gun = Spell("Water Gun", damage = 4, range = 10,elemental="Water", elemental_damage=4)
Tsunami = Spell("Tsunami", damage = 8, elemental="Water", elemental_damage=12, radius = 20) #From your position, deal 20 damage to all enemies in a radius of 20

Frost = Spell("Ray of Frost", armor= 1, elemental="ice", elemental_damage= 1, radius=10)
Ice_Blast = Spell("Ice Blast", damage = 3, armor = 4, elemental = "ice", elemental_damage =3, radius = 2)
Blizzard = Spell("Blizzard", damage = 10, armor = 8, elemental= "ice", elemental_damage= 10, radius = 4)

Gust = Spell("Gust", damage = 1, elemental= "wind", elemental_damage= 1, radius= 30) #its 30 from the character
Tornado = Spell("Tornado", damage = 3, range = 10, elemental="wind", elemental_damage=5, radius = 10)
Suffocate = Spell("Suffocate", range = 30, elemental= "wind", elemental_damage= 50)

Heal = Spell("Heal", range = 30, heal = 5)
Divine_Blessing = Spell("Divine Blessing", range = 30, heal = 10, armor= 5, damage_increase=5)
Cure_All = Spell("Cure All", range = 30, heal = 50)
Bulk = Spell("Bulk", range = 30, armor = 20)


Star_Crash = Spell("Star Crash", damage = 20, elemental= "space", elemental_damage=10, radius=20)
Celestial_Magic_Armor = Spell("Celestial Magic Armor", armor=30)
Astral_Force = Spell("Astral Force", damage = 50, elemental= "space", elemental_damage= 10 )
Astral_Healing = Spell("Astral Healing")


Beginners_Wand = Wand("Beginners Wand", 10, [Flame_Orb, Vine_Grip, Heal])

class Armor:
    def __init__(self, name, armor_value = 0, value = 0, super_effective = None, not_very_effective = None):
        self.armor_value = armor_value
        self.value = value
        self.name = name
        self.super_effective = super_effective
        self.not_very_effective = not_very_effective
        self.type = "armor"





