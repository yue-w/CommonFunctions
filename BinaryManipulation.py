# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 22:42:03 2020

@author: wyue
"""

#### Integer to binary
a = bin(10)
print(type(a))
print("a=",a)

#### Represent binary numbers, from string to binary number
b = "0b1000"
print('b=',int(b,2))


#### x<<y Shift the binary number x towards telf for y digits (add y zeros to the right)
### This is the same as multiplying x by 2**y
mask = 1 << 4
print(bin(mask))

#### Bitwse or
x = 0b10
y = 0b01
print(x|y)

#### Bitwse and
x = 0b10
y = 0b01
print(x&y)

####Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.
x = 0b1111
print(~x)

####Flip a bit of a number 
def flip_bit(bits,n,p): 
    #bits is the number of the bits (used for zero padding)
    #n is the number in binary form (starts with '0b'), p is the position to be flipped
    mask = 1 << p 
    rst = int(n,2)^mask
    fmt = '#0'+str(bits+2)+'b'
    rst = format(rst,fmt)#Zero padding
    return rst
print(flip_bit(8,bin(10),2))