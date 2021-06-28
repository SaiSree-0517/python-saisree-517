#keyword argument **args,**number....
def myfun(**kargs):
    for key,value in kargs.items():
        print(key,value)
    print(type(kargs))#<class 'dict'>
myfun(name='Saisree',subject='maths',surname='G')
"""
syntax:def function_name(n1,n2,n3,*args,**keywordargs)
"""

def add_n(b,c,*a,**key):
    s=0
    for i in a:
       s+=i
    for k,v in key.items():
        print(k,v)
    return s+b+c
print(add_n(5,6,7,8,name="xyz"))
print(add_n(5,6,7,4))
"""
name Saisree
subject maths
surname G
<class 'dict'>
name xyz
26
22
"""
