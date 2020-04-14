"""
See Python Doc for more details. https://docs.python.org/3/howto/sorting.html
__eq__, __ne__, __lt__, __le__,__gt__,__ge__
"""
class A(object):
    def __init__(self, value):
        self.value = value
        
#    def __cmp__(self, otherA):
#        return self.cmp(self.value, otherA.value)
    
    def __lt__(self,other):
        selfPriority = self.value
        otherPriority = other.value
        return selfPriority < otherPriority

"""    
    def __eq__(self,other):
        selfPriority = self.value
        otherPriority = other.value
        return selfPriority == otherPriority

"""

obj_list = []
a1 = A(4)
a2 = A(5)    
a3 = A(1)
a4 = A(9)
a5 = A(5)
obj_list.append(a1)
obj_list.append(a2)
obj_list.append(a3)
obj_list.append(a4)
obj_list.append(a5)

print("Before Sorting")
for i in obj_list:
    print(i.value)
    
sorted_obj = sorted(obj_list)
print("After Sorting")    
for i in sorted_obj:
    print(i.value)

###### Put objects in to a heap   
import heapq
aa1 = A(7)
aa2 = A(4)
aa3 = A(4)
aa4 = A(6)
obj_list2 = []
obj_list2.append(aa1)
obj_list2.append(aa2)
obj_list2.append(aa3)
obj_list2.append(aa4)
heapq.heapify(obj_list2)
obj_minv = heapq.heappop(obj_list2)
print("Object with min value:", obj_minv.value)