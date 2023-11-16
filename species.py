from inventory import *
from armor_weapon import *

class character():
    def __init__(self, name, inventory, distance = 0, weakness = None, health = 0, weapon1 = punch, weapon2 = kick, turned = 0, armor = Clothes):
        self.name = name
        self.inventory = inventory
        self.weapon1 = weapon1
        self.weapon2 = weapon2
        self.armor = armor
        self.distance_from_player = distance
        self.weakness = weakness
        self.health = health
        self.turned = turned
