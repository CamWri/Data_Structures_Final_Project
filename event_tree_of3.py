from collections import *
import math


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.mid = None
        self.right = None
        self.index = 0


class Tree:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            if self.head.left is None:
                self.head.left = Node(value)
                self.head.left.index += 1
            elif self.head.mid is None:
                self.head.mid = Node(value)
                self.head.mid.index = self.head.left.index + 1
            elif self.head.right is None:
                self.head.right = Node(value)
                self.head.right.index = self.head.mid.index + 1
            elif self.head.left is not None:
                self.recusrion_add_leftnode(self.head, value)
            elif self.head.mid is not None:
                self.recusrion_add_midnode(self.head, value)
            else:
                self.recursion_add_rightnode(self.head, value)

    def recusrion_add_leftnode(self, node, value):
        if node.left is None:
            node.left = Node(value)

            """Temporary solution for the issue of creating left but needing right and the right being None for pointint to 2 values
            if node.left.value == 3:
                node.left.index = node.index + 2
            else:
                node.left.index = node.index + 1"""

            node.left.index = node.index + 1

        else:
            self.recusrion_add_leftnode(node.left, value)

    def recusrion_add_midnode(self, node, value):
        if node.mid is None:
            node.mid = Node(value)
            node.mid.index = node.left + 1
        else:
            self.recusrion_add_midnode(node.right, value)

    def recursion_add_rightnode(self, node, value):
        if node.right is None:
            node.right = Node(value)
            node.right.index = node.mid + 1
        else:
            self.recursion_add_rightnode(node.right, value)

    def print_tree(self):
        if self.head is not None:
            print(self.head.value)
            self.print_tree_recurssion(self.head)
        else:
            print("There are no values")



    def print_tree_recurssion(self, node):
        list = [1, 10, 37, 118]
        if node is not None:
            if node.index in list:
                print()
        if node.left is not None:
            print(node.left.value, end=" ")
        if node.mid is not None:
            print(node.mid.value, end=" ")
        if node.right is not None:
            print(node.right.value, end=" ")
        if node.left is not None:
            self.print_tree_recurssion(node.left)
        if node.mid is not None:
            self.print_tree_recurssion(node.mid)
        if node.right is not None:
            self.print_tree_recurssion(node.right)

tree = Tree()

for i in range(0, 200, 2):
    tree.add_node(i)

tree.print_tree()

