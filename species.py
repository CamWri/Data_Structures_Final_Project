from inventory import *
from armor_weapon import *

class character():
    def __init__(self, name, inventory, distance = 0, species_weakness = [], health = 0, weapon1 = punch, weapon2 = kick, armor = Clothes, movement_distance = 3):
        self.name = name
        self.inventory = inventory
        self.weapon1 = weapon1
        self.weapon2 = weapon2
        self.armor = armor
        self.distance_from_player = distance
        self.health = health
        self.movement_distance = movement_distance
        self.weakness = set(species_weakness + self.armor.weakness)

    def examine(self):
        if len(self.weakness) != 0:
            weakness = ", ".join(self.weakness)
        else:
            weakness = f"None"
        return f"Health: {self.health}\nDistance From Player: {self.distance_from_player}\nMovement Per Turn: {self.movement_distance}\nWeakness: {weakness}"
