#methods in dictionary
dic={1:"CSE",2:"IT",3:"PT",4:"AGRI",5:"ECE"}
#get the value of key 4
print(dic[4])
#get()
print(dic.get(4))
#items()-->Return a new object of the dictionary's items in (key, value) format
print(dic.items())
#keys()--->returns list containing dictionary keys
print(dic.keys())
#popitem()--->Removes and returns an arbitrary item (key, value). Raises KeyError if the dictionary is empty.
print(dic.popitem())
#pop()
print(dic.pop(4))
print(dic.pop(4,["not found"]))
"""
AGRI
AGRI
dict_items([(1, 'CSE'), (2, 'IT'), (3, 'PT'), (4, 'AGRI'), (5, 'ECE')])
dict_keys([1, 2, 3, 4, 5])
(5, 'ECE')
AGRI
['not found']
"""
