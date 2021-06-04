#tuple creation
b=("CSE","IT","Mech","ECE","CSE","AGRI","PT")
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
#slicing
print(b[1])
#fetch elements from index2 to 5-1
print(b[2:5])
#0to(5-1)
print(b[:5])
#start index 3 to end
print(b[3:])
#start to end+1
print(b[:])
#step count 2 and 3
print(b[::2])
print(b[::3])
print(b[1:6:3])
print(b[::-2])
print(b[::-3])
print(b[1:6:1])
print(b[::1])
print(b[::-1])
#negative index fetching
print(b[-5:-2])
"""
methods in tuples
1.count
2.index
"""
print(b.index("CSE"))
#output
('CSE', 'IT', 'Mech', 'ECE', 'CSE', 'AGRI', 'PT')
<class 'tuple'>
7
('apple', 'mango', 'goa')
<class 'tuple'>
size of tuple is: 3
max element is PT
min element is AGRI
CSE is repeated 2 times
CSE
IT
Mech
ECE
CSE
AGRI
PT
CSE IT Mech ECE CSE AGRI PT
IT
('Mech', 'ECE', 'CSE')
('CSE', 'IT', 'Mech', 'ECE', 'CSE')
('ECE', 'CSE', 'AGRI', 'PT')
('CSE', 'IT', 'Mech', 'ECE', 'CSE', 'AGRI', 'PT')
('CSE', 'Mech', 'CSE', 'PT')
('CSE', 'ECE', 'PT')
('IT', 'CSE')
('PT', 'CSE', 'Mech', 'CSE')
('PT', 'ECE', 'CSE')
('IT', 'Mech', 'ECE', 'CSE', 'AGRI')
('CSE', 'IT', 'Mech', 'ECE', 'CSE', 'AGRI', 'PT')
('PT', 'AGRI', 'CSE', 'ECE', 'Mech', 'IT', 'CSE')
('Mech', 'ECE', 'CSE')
0
