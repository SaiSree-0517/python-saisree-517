#set operations
set1={1,2,3,4,5,10,12,13}
set2={10,11,12,13,14,15,17,19,1}
s1={1,2,3,4,5,10,12,13}
s2={10,11,12,13,14,15,17,19,1}
a={1,2,3,4,5,10,12,13}
b={10,11,12,13,14,15,17,19,1}
#union()-->All the elements,returns the union as a new set 
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
inter=s1.intersection(s2)
print("intersection=",inter)
s1.intersection_update(s2)
print("intersection_update=",s1)
#difference() and difference_update()
c=b.difference(a)
print("difference",c)
b.difference_update(a)
print("difference_update",b)

#output
union {1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 17, 19}
update {1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 17, 19}
intersection= {1, 10, 12, 13}
intersection_update= {1, 10, 12, 13}
difference {11, 14, 15, 17, 19}
difference_update {11, 14, 15, 17, 19}
