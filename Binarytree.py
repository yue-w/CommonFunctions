# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 17:52:10 2020

@author: wyue

Pypi Documentation: https://pypi.org/project/binarytree/
"""

from binarytree import Node
r1 = Node(1)
r2 = Node(2)
r1.left = Node(3)
r1.right = Node(4)
r2.left = Node(5)
r2.right = Node(6)
root = Node(0)
root.left = r1
root.right = r2
print(r1)
print(r2)
print(root)
print("Max leaf depth",root.max_leaf_depth)
print("Min leaf depth",root.min_leaf_depth)