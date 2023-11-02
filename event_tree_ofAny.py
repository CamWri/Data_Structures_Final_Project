from tkinter.tix import Balloon

from species import *
from colorama import *
from inventory import *

class Node:
    def __init__(self, value, iteam = None, gold = 0, enemies = []):
        self.value = value
        self.children = []
        self.audio_file_text = ""
        self.enemies = enemies
        self.loot = iteam
        self.gold = gold
        self.bitten = False

    def add_child(self, node):
        self.children.append(node)
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

node_1_1_1 = Node("Introduction of Soldiers")
node_1_1_1.audio_file_text = "Your story begins on a blistering hot summer day. You and your family are farming to sustain your destitute life. Your father is respected from everyone you know due to being the unofficial leader of this poor community of farmers that span out miles due to his excess generosity and leadership through rough times. In the distance, you hear guards approaching and talking about the increasing derangement of people for no aparent reason, but no one, not even your family, seems to think something is wrong. From the looks of it, the guard ignores all the other huts except yours even though all have to pay for the monthly commission for being part of the city. Your mother pleads that this payment is not expected for two weeks and are not prepared to pay, but the gaurd ignores her, looks at your father, and said get your wife under control now or there will be consequences. Your father is angered, but can do nothing, so he tells you to go get the money."
tree_1_1_1 = root.add_child(node_1_1_1)

node_you_2_1_1 = Node("You go to the house to pick up the money", gold = 10)
node_you_2_1_1.audio_file_text = "You follow his orders. You run inisde and grab the money as quickly as possible to make the gaurds to leave even quicker. As you grab the money, you hear a loud screech of sheer fear."
tree_2_1_1 = tree_1_1_1.add_child(node_you_2_1_1)

node_2_1_2 = Node("You examine the silent guards demeanour")
node_2_1_2.audio_file_text = "As you are about to leave to get the money, you see the guard have a slight wince of pain, twitching eyes, and sweating. You yell at the gaurd from a decent distance to see if he is okay. No response. The other gaurd, for no apparent reason your aware of, draws a sword at the other guard ready to strike. As the guard is about strike, the ill strucken guard goes primal and pounces onto the other guard with soulless and bloodshot eyes. This thing does a quick bite, ripping a peices of skin, and then pumbles the other guard to death. Its eyes are now on your father as it prepares to jump."
tree_2_1_2 = tree_1_1_1.add_child(node_2_1_2)

#Height 3
node_3_1_1 = Node("You grab your sword, wand, and armour", iteam = [Wood_Sword, Beginners_Wand, Leather_Armor])
node_3_1_1.audio_file_text = "You run to the left side entrance to where you keep all of your equipment. All you are have is the clothes on your back and your fists. You grab and put into your inventory a wooden sword, a basic wand, and your leather armor. As you are putting your leather armor on, you mother bursts into the door with your siblings. You see fear, confusion, worriness in everyones eyes. She explains how one of the gaurds just started spaz, dropped to the ground, and then brutally pumbel the other guard to death. Now your father is fighting and he told us to run and hide. You can tell she is nervious for his saftey."
tree_3_1_1 = tree_2_1_1.add_child(node_3_1_1)

node_3_1_2 = Node("You run outside with the extra money to bribe the guards.", gold = 200)
node_3_1_2.audio_file_text = "Your mind is racing with thoughts of what could have happened and you think a way to gaurantee you and your families saftey, a bribe. You run to your personal stash of coins on the other side of your hut and grab it all. As you are running back, you hear a blood curdaling scream of fear, that turns to pain, and fades off. You reach outside to only see an atrocity. Both guards, hunched over you entire family, souless and primitive eyes with the faintest of pupil. You see the faintest of movements of all your family membets, so you know they are alive, so you have to do something. These things that were once human see you and rush after you."
tree_3_1_2 = tree_2_1_1.add_child(node_3_1_2)

node_3_2_3 = Node("You run join the fight with your father", enemies = [Corrupt_Guard])
node_3_2_3.audio_file_text = "You rush out into the heat of the conflict. You understand that your father shouldn't have to do it alone. Your father sees you out of the corner of your eye as he starts to engage. "
tree_3_2_3 = tree_2_1_2.add_child(node_3_2_3)

node_3_2_4 = Node("You think your father has it under control and don't want to get in his way")
node_3_2_4.audio_file_text = "You understand the gravity of the situation and you don't want to add another thing to your fathers plate due to him already undestanding the situation due to the stance he is taking. He starts by bending his knees as he tries to engage it. A vicious fight occurs between your father and this beast while you watch, not knowing what to do. Eventually your father comes out on top, beating it with only his fists, but not without bites, scratches, and bruisses all over his body. He decides to just lay down, eyes open, as if he is still isn't comprehending the situation."
tree_3_2_4 = tree_2_1_2.add_child(node_3_2_4)

#Height 4
node_4_1_1 = Node("You escort your mother and siblings to a hiding place")
node_4_1_1.audio_file_text = "You decide to ensure your mother and siblings safety because that is what your father would have wanted and you can not be sure you can arrive in time to save him anyways. You run with the group to find a good hiding spot. You eventually decide to put everyone excluding yourself behind your massive food storage containers that are used to store excess food. You do not know where your father is, he could be dead for all you know."
tree_4_1_1 = tree_3_1_1.add_child(node_4_1_1)
#You find a hiding spot for your mother/siblings and you scout the area to protect them. You look outside and see that your father is on the ground and both the gaurds are missing, but you see the trails of blood that lead to the right side of your hut. You follow the blood and see that the gaurds are sparatic and twitching while mindlessly walking, only following a scent. They still look and act alive but something is off about them, you only see an occasional twitch of their head and their feet dragging. You see one run like a switch has been turned on towards the hiding spot your family is in.

node_4_1_2 = Node("Run towards your father to help")
node_4_1_2.audio_file_text = "You decide to attack the problem head on and help your father. Your mother seems alieved but worried at the same time. You tell her to hide and only come out when you hear your own or father voice. You turn and hear the everyone run inside. As you get outside, you hear the deadening silence and smell ageing blood and death in the air. You see your father and two bloodied guards. One of the guards has been bitten and clawed with blood all over his body while the other has been punched and stabbed by a sword with blood in the face and mouth. As you look back to your father you see movement from his end. You rush over and see a bite on his shoulder and claw marks all over his body and shirt. He lays there unconciously, but still breathing heavily as you approach. You reach over and help him up and try to get him inside to get some treatment for the injuries. As are walking back to your house, the other mangeld guard with scratches and bites begins to move."
tree_4_1_2= tree_3_1_1.add_child(node_4_1_2)

node_4_2_3 = Node("You engage knowing you only have your fists and gold", enemies= [Corrupt_Guard])
node_4_2_3.audio_file_text = "Dialogue 1"
tree_4_2_3 = tree_3_1_2.add_child(node_4_2_3)

node_4_2_4 = Node("You retreat to gather your equipment")
node_4_2_4.audio_file_text = "Dialogue 2"
tree_4_2_4 = tree_3_1_2.add_child(node_4_2_4)

node_4_3_5 = Node("You beat the guard")
tree_4_3_5 = tree_3_2_3.add_child(node_4_3_5)

node_4_3_6 = Node("You loose to the guard")
tree_4_3_6 =  tree_3_2_3.add_child(node_4_3_6)

node_4_4_7 = Node("Check on your father to see how he is doing")
node_4_4_7.audio_file_text = "You go run and check on your father. "
tree_4_4_7 = tree_3_2_4.add_child(node_4_4_7)
#this can lead to the other one turning with your back behind, your father sacrifces himself to defeat the beast, you have a chance to behead your father cause he might turn

node_4_4_8 = Node("Check the lifeless corpse of the diseased guard")
node_4_4_8.audio_file_text = "Action 2 text file"
tree_4_4_8 = tree_3_2_4.add_child(node_4_4_8)
#As you walk over, you feel something inticing you to explore what this creature is. You see something buldging and squirming on its wrist.

node_4_4_9 = Node("Check on the non-diseased guard")
node_4_4_9.audio_file_text = "Action 2 text file"
tree_4_4_9 = tree_3_2_4.add_child(node_4_4_9)
#this is where you git bitten, the sheer pain and discomfort makes you pass out. But you wake up and it seems only minutes have went by, see fathers bloodied trail, the guard that bitten you gone, and the intial infected guards corpse just laying there.See you have enhanced physical feets. Meet your father that is converted and hunting the rest of your familyy.Neither guard or father is hostile, sees you as one of them. Can fight them or accept your powers. If yight them off, save family, family sees bloodshot eyes, then you can talk to them about what happened or leave to not frighten your family. You loot the corpses and see that this was a hit from someone inside the capital. Then act 2 starts where you can find a cure, you can accept your fate as this hybrid

#Height 5
node_5_1_1 = Node("You be the look out to protect the rest of your family and fight any danger, if there is any")
tree_5_1_1 = tree_4_1_1.add_child(node_5_1_1)

node_5_1_2 = Node("You check outside to see if there is any updates, which looses sight of your family")
tree_5_1_2 = tree_4_1_1.add_child(node_5_1_2)

node_5_2_3 = Node("You ignore the guard")
tree_5_2_3 = tree_4_1_2.add_child(node_5_2_3)

node_5_2_4 = Node("You set your father down and go check out the other guard")
tree_5_2_4 = tree_4_1_2.add_child(node_5_2_4)
#the other guard is tranfoming and wispers kill me in his final breaths


node_5_3_5 = Node("You beat the guard")
tree_5_3_5 = tree_4_2_3.add_child(node_5_3_5)

node_5_3_6 = Node("You loose to the guard")
tree_5_3_6 =  tree_4_2_3.add_child(node_5_3_6)