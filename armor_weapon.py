
class Sword:
    def __init__(self, name, damage, value, elemental = None, elemental_damage = 0):
        self.damage = damage
        self.value = value
        self.name = name
        self.range = 2
        self.element = elemental
        self.elemental_damage = elemental_damage
        self.type = "weapon1"

    def examine(self):
        return f'Weapon 1: {self.name}\nValue: {self.value}\nDamage: {self.damage}\nRange: {self.range}\nElement: {self.element}\nElement Damage: {self.elemental_damage}'



Wood_Sword = Sword("Wooden Sword", 5, 5)
Flame_Sword = Sword("Flame Sword", 12, 25, elemental= "fire", elemental_damage= 2)
Iron_Sword = Sword("Iron Sword", 15,30)
Light_Bringer_Sword = Sword("Light Bringer Sword", 10, 100, elemental = "light", elemental_damage = 10)
Dark_Creators_Sword = Sword("Dark Creator's Sword", 10, 175, elemental = "darkness", elemental_damage = 10)
Celestial_Sword = Sword("Celestial Sword", 15, 2500, elemental = "celestial", elemental_damage = 15)


class Wand:
    def __init__(self, name, value, spells):
        self.name = name
        self.value = value
        self.spells = spells
        self.type_of_damage = "magical"
        self.type = "weapon2"
        self.range = 0

    def examine(self):
        spell_name = []
        for i in self.spells:
            spell_name.append((i.examine()))
        spell = "\n\t".join(spell_name)
        return f"Weapon 2: {self.name}\nValue: {self.value}\nSpells:\n\t{spell}"


class Spell:
    def __init__(self, name, damage = 0, armor= 0, elemental = None, elemental_damage = 0, radius = 0):
        self.name = name
        self.damage = damage
        self.armor = armor
        self.elemental = elemental
        self.elemental_damage = elemental_damage
        self.radius = radius

    def cast_spell(self):
        pass

    def examine(self):
        return f'{self.name}\nDamage: {self.damage}\nElement: {self.elemental}\nElemental Damage: {self.elemental_damage}\nDamage Radius: {self.radius}'


#Fire Spells
Flame_Orb = Spell("Flame Orb", damage = 1, elemental = "fire", elemental_damage = 4)
Firebolt = Spell("Firebolt", damage = 3, elemental = "fire", elemental_damage = 5)
Dragons_Breath = Spell("Dragons Breath", elemental = "fire", elemental_damage = 9, radius = 10)
Incinerate = Spell("Incinerate", damage = 5, elemental = "fire", elemental_damage = 15)

#Electric Spells
Spark = Spell("Spark", damage = 2, elemental = "electric", elemental_damage=2)
Electric_Veins = Spell("Electric Veins")
Lightning = Spell("Lightning", damage = 3, elemental= "electric", elemental_damage= 3)
Electrical_Surge = Spell("Electrical_Surge", damage = 5, elemental="electric", elemental_damage=5, radius = 5)
Thunder = Spell("Thunder", damage = 25, elemental = "electric", elemental_damage=25)

#Eath/Ground Spells
Vine_Grip = Spell("Vine Grip", damage = 2, elemental = "earth", elemental_damage=2)
Rock_Blast = Spell("Rock Blast", damage = 3, elemental = "earth", elemental_damage=6)
Earthquake = Spell("Earthquake", damage = 15, elemental = "earth", elemental_damage=10, radius = 3)

Water_Bubble = Spell("Water Bubble", damage = 2, elemental="water", elemental_damage=1)
Water_Gun = Spell("Water Gun", damage = 4, elemental="Water", elemental_damage=4)
Tsunami = Spell("Tsunami", damage = 8, elemental="Water", elemental_damage=12, radius = 20) #From your position, deal 20 damage to all enemies in a radius of 20

Frost = Spell("Ray of Frost", elemental="ice", elemental_damage= 1, radius=10)
Ice_Blast = Spell("Ice Blast", damage = 3, elemental = "ice", elemental_damage =3, radius = 2)
Blizzard = Spell("Blizzard", damage = 10, elemental= "ice", elemental_damage= 10, radius = 4)

Gust = Spell("Gust", damage = 1, elemental= "wind", elemental_damage= 1, radius= 30) #its 30 from the character
Tornado = Spell("Tornado", damage = 3, elemental="wind", elemental_damage=5, radius = 10)
Suffocate = Spell("Suffocate", elemental= "wind", elemental_damage= 50)

Divine_Blessing = Spell("Divine Blessing")
Bulk = Spell("Bulk")


Star_Crash = Spell("Star Crash", damage = 20, elemental= "space", elemental_damage=10, radius=20)
Astral_Force = Spell("Astral Force", damage = 50, elemental= "space", elemental_damage= 10 )


Starter_Wand = Wand("Starter Wand", 10, [Flame_Orb, Vine_Grip])
Intermediate_Wand = Wand("Intermediate Wand", 50, [])
Fire_Oracle = Wand("Fire Oracle", 1000, [Incinerate, Dragons_Breath, Divine_Blessing])
Astral_Master_Wand = Wand("Astral_Master_Wand", 10000, [Star_Crash, Astral_Force])

class Armor:
    def __init__(self, name, armor_value = 0, value = 0, weakness = []):
        self.armor_value = armor_value
        self.value = value
        self.name = name
        self.type = "armor"
        self.weakness = weakness

    def examine(self):
        weakness_list = []
        for i in self.weakness:
            weakness_list.append(i)
        weakness = ", ".join(weakness_list)
        return f'Armor: {self.name}\nValue: {self.value}\nArmor Value: {self.armor_value}\nWeakness: {weakness}'


Clothes = Armor("Clothes", armor_value=3, value = 1, weakness = ["ice"])
Leather_Armor = Armor("Leather Armor", armor_value = 4, value = 10)
Iron_Armor = Armor("Iron Armor", armor_value=6, value = 150)
Dragon_Armor = Armor("Dragon Armor", armor_value=20, value= 3000)

class Shield:
    def __init__(self, name, value, damage_mitigation):
        self.name = name
        self.value = value
        self.damage_mitigation = damage_mitigation
        self.type = "weapon2"
        self.type_of_damage = None

    def examine(self):
        return f'Weapon 2: {self.name}\nValue: {self.value}\nDamage Mitigation: {self.damage_mitigation}'


Wood_Shield = Shield("Wooden Shield", value = 3, damage_mitigation= 2)
Reinforced_Iron_Shield = Shield("Reinforced Iron Shield", value = 20, damage_mitigation= 5)

class Hand_Combat:
    def __init__(self, damage = 1, range = 2, name = "Fists"):
        self.name = name
        self.damage = damage
        self.range = range
        self.type = "Hand Attacks"
        self.type_of_damage = "Physical"
        self.spells = []
        self.elemental_damage = 0
        self.elemental = None

    def examine(self):
        return f"{self.type}: {self.name}\nDamage: {self.damage}\nRange: {self.range}"

punch = Hand_Combat(name = "Punch", damage = 5, range = 2)
kick = Hand_Combat(name = "Kick", damage = 4, range = 3)
claws = Hand_Combat(name = "Claws", damage = 3, range = 2)