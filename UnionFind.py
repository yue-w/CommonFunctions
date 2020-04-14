# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 17:05:21 2020

@author: wyue
"""

from disjoint_set import DisjointSet

class A():
    def __init__(self,a):
        A.v = a
        
ds = DisjointSet()

ds.find(1)
ds.find(2)
ds.find(3)
ds.find(4)
print(ds.connected(1,2))
ds.union(1,2)

print(ds.connected(1,2))

####print all unique sets
allsets = list(ds.itersets())
print(allsets)
print("Num of sets:",len(allsets))
