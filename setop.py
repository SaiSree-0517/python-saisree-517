#set operations
#union()-->All the elements,returns the union as a new set
set1={1,2,3,4,5,10,12,13}
set2={10,11,12,13,14,15,17,19,1}
u=set1.union(set2)
print("union",u)
#union and update
"""
in update union of elements will be
updated to set1 and union method
returns a new set
"""
set1.update(set2)
print("update",set1)

#intersection and intersection_update
s1={1,2,3,4,5,10,12,13}
s2={10,11,12,13,14,15,17,19,1}
inter=s1.intersection(s2)
print("intersection=",inter)
s1.intersection_update(s2)
print("intersection_update=",s1)
#difference() and difference_update()
a={1,2,3,4,5,10,12,13}
b={10,11,12,13,14,15,17,19,1}
c=b.difference(a)
print("difference",c)
b.difference_update(a)
print("difference_update",b)

"""
issuperset()-->Set X is said to be the superset of set Y if all elements of Y are in X.
The issuperset() method returns True if a set has every elements of another set (passed as an argument).
If not, it returns False.
"""

A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
C = {1, 2, 3}
print("A is superset of B or B is subset of A:",A.issuperset(B))#checks A is superset of B or not and returns True or False 
print(B.issuperset(A))#checks B is superset of A or not and returns True or False  
print(C.issuperset(B))#checks C is superset of B or not and returns True or False
"""
issubset()-->The issubset() method returns True if all elements of a set A
are present in another set B which is passed as an argument and returns false if all elements not present.
a set X is a subset of a set Y if all elements of X are also elements of Y.
"""
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}
print(A.issubset(B))#Returns True , A is subset of B
print(B.issubset(A))# Returns False, B is not subset of A
print(A.issubset(C))#Returns False, A is not subset of C
print(C.issubset(B))#Returns True , C is subset of B
#output
union {1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 17, 19}
update {1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 17, 19}
intersection= {1, 10, 12, 13}
intersection_update= {1, 10, 12, 13}
difference {11, 14, 15, 17, 19}
difference_update {11, 14, 15, 17, 19}
A is superset of B or B is subset of A: True
False
True
True
False
False
True

