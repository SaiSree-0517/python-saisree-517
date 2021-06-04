#tuple creation
b=("CSE","IT","Mech","ECE")
print(b)
print(type(b))
print(len(b))#size of tuple
#creation of tuple
a=tuple(("apple","mango","goa"))
print(a)
print(type(a))
print("size of tuple is: {}".format(len(a)))
#max element
print("max element is %s" %max(b))#maximum element in tuple
print("min element is %s" %min(b))#minimum element in tuple
print("CSE is repeated %s times" %(b.count("CSE")))#counting the elements in the tuple
for i in b:#printing element by element
    print(i)
print(*b)
#output
('CSE', 'IT', 'Mech', 'ECE')
<class 'tuple'>
4
('apple', 'mango', 'goa')
<class 'tuple'>
size of tuple is: 3
max element is Mech
min element is CSE
CSE is repeated 1 times
CSE
IT
Mech
ECE
CSE IT Mech ECE
