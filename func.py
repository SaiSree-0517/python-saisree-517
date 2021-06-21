"""
defining function
def function_name(parameters):
    statement(s)
"""
def test():#without parameters
    print("Hello!I am function")
    print("hi!!!!!!!")
#calling function-->function_name()
test()

#function with parameters
def show(x):
    print("Function show with parameters")
    print(x)
    print(type(x))
#calling show function
show("python")#passing string
show(17)#passing integer
show(10.990909)#passing  float
set1={123,457,5678}
show(set1)#passing set
list1=["Python","Flat","CO","DAA","IOT"]
show(list1)#with list
dict1={5:"CSE",12:"IT",3:"ECE"}
show(dict1)#with dictionary
tuple1=(1,2,3,5)
show(tuple1)#with tuple
show(tuple((1,2,3.4)))

"""
Hello!I am function
hi!!!!!!!
Function show with parameters
python
<class 'str'>
Function show with parameters
17
<class 'int'>
Function show with parameters
10.990909
<class 'float'>
Function show with parameters
{457, 123, 5678}
<class 'set'>
Function show with parameters
['Python', 'Flat', 'CO', 'DAA', 'IOT']
<class 'list'>
Function show with parameters
{5: 'CSE', 12: 'IT', 3: 'ECE'}
<class 'dict'>
Function show with parameters
(1, 2, 3, 5)
<class 'tuple'>
Function show with parameters
(1, 2, 3.4)
<class 'tuple'>
"""

