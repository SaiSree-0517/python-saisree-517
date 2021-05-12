ba=int(input('enter bill ammount'))
if ba<1000:
    d=0.05*ba
    print('discount=',d)
elif ba<3000:
    d=0.1*ba
    print('discount=',d)
elif ba<5000:
    d=0.2*ba
    print('discount=',d)
else:
    d=0.3*ba
    print('discount=',d)
a=ba-d
print(a)
