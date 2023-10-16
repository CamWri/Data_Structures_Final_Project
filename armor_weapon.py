class Sword:
    def __init__(self, name, damage, value):
        self.damage = damage
        self.value = value
        self.name = name
        self.range = 1
        self.type = "slashing"
        self.type2 = "thrusting"

    def attack(self, target):
        pass

Wood_Sword = Sword("Wooden Sword", 2, 5)
Bronze_Sword = Sword("Bronze Sword", 3, 15)
Iron_Sword = Sword("Iron Sword", 5,30)
Light_Bringer_Sword = Sword("Light Bringer Sword", 7, 100)
Dark_Creators_Sword = Sword("Dark Creator's Sword", 10, 175)
Calamity_Sword = Sword("Sword of Calamity", 13, 500)
Celestial_Sword = Sword("Celestial Sword", 15, 2500)

class Longsword:
    def __init__(self, name, damage, value):
        self.damage = damage
        self.value = value
        self.name = name
        self.range = 3
        self.type = "slashing"
        self.type2 = None

    def attack(self, target):
        pass

class Spear:
    def __init__(self, name, damage, value):
        self.damage= damage
        self.value = value
        self.name = name
        self.range = 3
        self.type = "thrusting"
        self.type2 = None

    def attack(self, targer):
        pass

class Hammer:
    def __init__(self, name, damage, value):
        self.damage = damage
        self.value = value
        self.name = name
        self.range = 2
        self.type = "crushing"
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




