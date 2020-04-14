# -*- coding: utf-8 -*-
"""
Sort 2D array by column
"""

a = [[1,4],[2,3],[3,2],[4,1]]
print(a)
b = sorted(a, key=lambda x : x[1])#Return a another list
print(b)
a.sort(key=lambda x : x[1])#Inline
print(a)

##Sort two arrays using zip
c = [['a','b'],['c','d'],['e','f'],['g','h']]
d = [4,2,1,5]
lst = list(zip(c,d))
print(lst)
stlst = sorted(lst,key=lambda x:x[1])
print(stlst)