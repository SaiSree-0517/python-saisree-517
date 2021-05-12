n=int(input('enter the number'))#1234567
sum=n
while sum>9:
    n=sum
    sum=0
    while n>0:
        rem=n%10
        sum+=rem
        n=n//10
print(sum)
