"""
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
List comprehensions provide a concise way to create lists

"""

#### Example 1
data = [(1,2,3),(4,5,6),(7,8,9),(10,11,12),(13,14,15)]
R = [pixel[0] for pixel in data]
G = [pixel[1] for pixel in data]
B = [pixel[2] for pixel in data]

####Example 2

combine = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]