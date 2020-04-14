# -*- coding: utf-8 -*-
"""
Two ways to sort a dictionary by value
"""

dic = {'C':1,'A':3,'D':5,'B':2}

dic_sorted_bykey = sorted(dic.items())
print('Dic sorted by key',dic_sorted_bykey)

def f(item):
    return item[1]
dic_sorted_byvalue_function = sorted(dic.items(), key = f)
print('Dic sorted by value, using function',dic_sorted_byvalue_function)

dic_sorted_byvalue_lambda = sorted(dic.items(), key=lambda item: item[1])
print('Dic sorted by value, using lambda',dic_sorted_byvalue_lambda)

