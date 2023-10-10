from pathlib import *
import gtts
import playsound
from species import *

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.children_value = []
        self.dialogue = ""
        self.action = None

    def add_child(self, node):
        self.children.append(node)
        self.children_value.append(node.value)
        return node

    def establish_dialogue(self, dialogue):
        self.dialogue = dialogue

    def establish_action(self, action):
        self.action = action


class Tree:
    def __init__(self):
        self.head = None

    def add_child(self, value):
        self.head = Node(value)
        return self.head


    def print_tree(self):
        if self.head is not None:
            print(f'This is the head/root value')
            print(f'\t{self.head.value} \n')
            return self.rec_print_tree(self.head)
        else:
            print("There is no values in the tree")

    def rec_print_tree(self, node):
        if len(node.children_value) > 0:
            print(f'This is all the children values for the parent value is: \"{node.value}\"')
            for i in node.children_value:
                print(f'\tA child value is: {i}')
            print()
            for i in node.children_value:
                self.rec_print_tree(node.children[node.children_value.index(i)])

    def get_all_children(self, parent_value):
        if self.head is None:
            print("There is no values in the tree")
        else:
            self.rec_get_all_children(self.head, parent_value)

    def rec_get_all_children(self, current_node, parent_value):
        if current_node.value == parent_value:
            print(f'The list of children from the {current_node.value} node is:')
            for i in current_node.children_value:
                print(f'\t{i}')
        else:
            for i in current_node.children_value:
                self.rec_get_all_children(current_node.children[current_node.children_value.index(i)], parent_value)


tree = Tree()

root = tree.add_child("Create your character")
root.establish_dialogue("With the presence of good in life, there will always comes the evil. "
                    "So, even in the most prosperous of times, evil still exists. Sometimes it is just harder to see. "
                    "Evil lingers, grows, and evolves during prosperity, eventually overtaking the good. "
                    "Today is one of those times with a curse spreading all across the lands,  corrupting life itself. "
                    "The once living things are accursed with rage, anger, and vengeance with no mental power or free will. "
                    "Some say its an act of a higher deity, others say its from the mountains. "
                    "Some even say it was created by the living, but no one knows for sure. "
                    "Depending on your actions, you can be the savior of the lands, or lead the curse for domination. "
                    "So, with the fate of the lands in your hands, who will you be?")




node_you_1_1 = Node("You go to the house to pick up the money")
you_1_1 = root.add_child(node_you_1_1)

node_fam_1_2 = Node("Your family member goes to the house to pick up the money")
fam_1_2 = root.add_child(node_fam_1_2)

tree.print_tree()