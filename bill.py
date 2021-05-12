pa=int(input('enter the bill amount:'))
if pa>=1000:
    d=0.1*pa
    print('discount=',d)
else:
    d=0.05*pa
    print('discount=',d)
a=pa-d
print(a)
