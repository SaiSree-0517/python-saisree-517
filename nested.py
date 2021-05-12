n=int(input('enter a number'))
sum=0
t=1
while t:
    while n:
        sum+=n%10
        n=n//10
    print('sum=',sum)
    n=sum
    sum=0
    t=n>9
    
