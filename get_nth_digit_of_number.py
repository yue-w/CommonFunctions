# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 23:32:46 2020

@author: wyue
"""

def get_digit(number, n):
    return number // 10**n % 10

print(get_digit(987654321, 1))