from species import *
from colorama import *
from inventory import *
from armor_weapon import *

class Node:
    def __init__(self, value, iteam = None, gold = 0):
        self.value = value
        self.children = []
        self.children_value = []
        self.audio_file_text = ""
        self.enemies = []
        self.loot = iteam
        self.gold = gold

    def add_child(self, node):
        self.children.append(node)
        self.children_value.append(node.value)
        return node

    def establish_audio_file(self, file_name):
        self.audio_file = file_name

    def establish_enemies(self):
        pass


class Tree:
    def __init__(self):
        self.head = None

    def add_child(self, value):
        self.head = Node(value)
        return self.head



tree = Tree()


root = tree.add_child("Background Story")
root.audio_file_text = "There has and will always be good and evil. During prosperity, evil lingers in the shadows of the good. Over time though, this evil unleashes on the world. Today is one of those times with a curse spreading all across the lands corrupting the soul itself. Depending on your actions, you can be the savior of the lands or lead the curse for domination. So with the fate of the lands in your hands, who will you be?"

node_intro_1_1_1 = Node("Introduction of Soldiers")
node_intro_1_1_1.audio_file_text = "Your story begins on a blistering hot summer day. You and your family are farming to sustain your destitute life. In the distance, you hear guards approaching and talking about the public's worries over the increasing derangement of people. When the guards get to your hut, they ask for the monthly commission for being part of the city. Everyone knows people in this area can't pay it and get other needs but if you don't, you will be ostracized. Your father tells you to go get the money."
intro_1_1_1 = root.add_child(node_intro_1_1_1)

node_you_2_1_1 = Node("You go to the house to pick up the money")
node_you_2_1_1.audio_file_text = "You follow his orders. You run inisde and grab the money as quickly as possible to make the gaurds to leave even quicker. As you grab the money, you hear a loud screech of sheer fear."
you_2_1_1 = intro_1_1_1.add_child(node_you_2_1_1)

node_wisdom_check_2_1_3 = Node("Examine the silent guards demeanour")
node_wisdom_check_2_1_3.audio_file_text = "As you are about to leave, you see the guard have a slight wince of pain, twitching eyes, and sweating. You ask the gaurd if he is okay. No response. You look at the other gaurd that has started looking at paperwork. As you look back at the ill strucken gaurd, you see his soulless and bloodshot eyes. You see the guard, no, this lifeless creature, reach for the other gaurd, pumblening him to death. Everyone looks in horror, as your father demands everyone to go inside as he stands there holding his ground and drawing a blade."
wisdom_check_2_1_3 = intro_1_1_1.add_child(node_wisdom_check_2_1_3)


node_grab_run_weapon_3_1_1 = Node("You grab your sword, wand, and armour and then run outside", iteam = [Wood_Sword], gold= 10)
grab_run_weapon_3_1_1 = you_2_1_1.add_child(node_grab_run_weapon_3_1_1)

node_run_3_1_2 = Node("You run outside with the extra money to pay off the guards so they do no harm you or your family.", gold = 200)
run_3_1_2 = you_2_1_1.add_child(node_run_3_1_2)
