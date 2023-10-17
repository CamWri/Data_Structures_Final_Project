class Sword:
    def __init__(self, name, damage, value, elemental = None, elemental_damage = 0):
        self.damage = damage
        self.value = value
        self.name = name
        self.range = 1
        self.type = "slashing"
        self.type2 = "piercing"

    def attack(self, target):
        pass

Wood_Sword = Sword("Wooden Sword", 2, 5)
Bronze_Sword = Sword("Bronze Sword", 3, 15)
Flame_Sword = Sword("Flame Sword", 2, 25, elemental= "fire", elemental_damage= 2)
Iron_Sword = Sword("Iron Sword", 5,30)
Light_Bringer_Sword = Sword("Light Bringer Sword", 7, 100, elemental = "light", elemental_damage = 7)
Dark_Creators_Sword = Sword("Dark Creator's Sword", 7, 175, element = "darkness", elemental_damage = 7)
Calamity_Sword = Sword("Sword of Calamity", 13, 500)
Celestial_Sword = Sword("Celestial Sword", 10, 2500, elemental = "celestial", elemental_damage = 10)


class Greatsword:
    def __init__(self, name, damage, value, elemental = None, elemental_damage = 0):
        self.damage = damage
        self.value = value
        self.name = name
        self.range = 3
        self.type = "slashing"
        self.type2 = None

    def attack(self, target):
        pass

Wood_Greatsword = Greatsword("Wooden Great Sword", 2, 7)
Bronze_Greatsword = Greatsword("Bronze Great Sword", 3, 20)
Iron_Greatsword = Greatsword("Iron Great Sword", 5, 35)
Celestial_Greatsword = Greatsword("Celestial Great Sword", 10, 2750, elemental = "celestial", elemental_damage = 10)




class Spear:
    def __init__(self, name, damage, value, elemental = None, elemental_damage = 0):
        self.damage= damage
        self.value = value
        self.name = name
        self.range = 3
        self.type = "thrusting"
        self.type2 = None

    def attack(self, targer):
        pass

Ice_spear = Spear("Ice Tipped Spear", 5, 35, elemental= "ice", elemental_damage= 5)


class Hammer:
    def __init__(self, name, damage, value):
        self.damage = damage
        self.value = value
        self.name = name
        self.range = 2
        self.type = "bludgeoning"
        self.type2 = None

    def attack(self, target):
        pass
class Wand:
    def __init__(self, name, value, spells):
        self.name = name
        self.value = value
        self.spells = spells

class Spell:
    def __init__(self, name, damage = 0, heal = 0, armor= 0, range = 0, type = "", displacement = 0, num_targets = 1):
        self.name = name
        self.damage = damage
        self.heal = heal
        self.armor = armor
        self.range = range
        self.type = type
        self.displacement = displacement
        self.num_targets = num_targets

    def spell_into(self):
        pass

    def cast_spell(self):
        pass



class Armor:
    def __init__(self, name, armor_value, value, resistances):
        self.armor_value = armor_value
        self.value = value
        self.name = name
        self.resistances = resistances




