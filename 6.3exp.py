"""
6.3 sort the two lists
L1=[45,63,23,12,78]
L2=[12,90,72,-1]
combine L1 and L2 as a single list
and display elements in the sorted order
"""
l1=[]
l2=[]
n1=int(input("Enter number of elements:"))
for i in range(1,n1+1):
    b=int(input("Enter element:"))
    l1.append(b)
n2=int(input("Enter number of elements:"))
for i in range(1,n2+1):
    d=int(input("Enter element:"))
    l2.append(d)
new=l1+l2
new.sort()
print("Sorted list is:",new)

#output
Enter number of elements:5
Enter element:10
Enter element:15
Enter element:11
Enter element:17
Enter element:12
Enter number of elements:2
Enter element:1
Enter element:2
Sorted list is: [1, 2, 10, 11, 12, 15, 17]
