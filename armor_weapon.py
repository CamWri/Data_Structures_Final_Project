class Weapon:
    def __init__(self, damage, value):
        self.damage = damage
        self.value = value

class Armor:
    def __init__(self, armor_value, value):
        self.armor_value = armor_value
        self.value = value

class Misc:
    def __init__(self, name, value):
        self.value = value
        self.name = name

Wood_Sword = Weapon(1, 5)
Bronze_Sword = Weapon()
Iron_Sword = Weapon(5, 30)


