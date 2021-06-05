"""
Implement a Python script to rotate list of elements towards right up to given number of times. Example: Input: [23,34,9,45,19] and 2 (Hint: 2 indicates No. of times to rotate) Output: [45,19,23,34,9]
"""
n1=int(input("Enter how many list of values"))
list_number=[]
n=int(input("enter the no of rotations"))
#read list of values from user
for i in range(n1):
    num=int(input())
    #append number to list data structure
    list_number.append(num)
print(list_number)
list_number = (list_number[-n:] + list_number[:-n])
print(list_number)

#output
Enter how many list of values5
enter the no of rotations2
14
15
75
10
25
[14, 15, 75, 10, 25]
[10, 25, 14, 15, 75]
