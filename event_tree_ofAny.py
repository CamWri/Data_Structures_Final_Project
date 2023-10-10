from pathlib import *
import gtts
import playsound
from species import *

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.children_value = []
        self.narration = ""

class Tree:
    def __init__(self):
        self.head = None

    def add_child(self, value, parent_value):
        if self.head is None:
            self.head = Node(value)
        else:
            self.rec_add_child(value, parent_value, self.head)

    def rec_add_child(self, value, parent_value, node):
        if parent_value == node.value:
            new_node = Node(value)
            node.children.append(new_node)
            node.children_value.append(new_node.value)
        else:
            for i in node.children_value:
                self.rec_add_child(value, parent_value, node.children[node.children_value.index(i)])

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



disease = Tree()

root = disease.add_child("Create Character", None)

disease.add_child("Go to your families hut to fetch the money", "Create Character")
disease.add_child("Ask your older brother to fetch the money in the hut", "Create Character")
