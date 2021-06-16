le=[]
n=int(input())
for i in range(1,n+1):
    if i%2==0:
        le.append(i)
print("even list without using list comprehension",le)
#using comprehension
n=int(input())
le=[i for i in range(1,n+1) if i%2==0]
print("even list using list comprehension",le)
"""
10
even list without using list comprehension [2, 4, 6, 8, 10]
10
even list using list comprehension [2, 4, 6, 8, 10]
"""
