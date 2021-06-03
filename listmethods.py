b=list(("banana","kiwi"))
print(b)
b.append("jiwi")#jiwi will be added at last position
print(b)
x=b.copy()#elements in b copied to x
print(x)
x.clear()#empty x
print(x)
y=b.copy()#b elements copied to y
print(*y)
y.sort()#sorting in ascending order
print(y)
y.sort(reverse=True)#sorting in descending order
print(y)
y.remove("banana")#deleting banana from the list
print(y)
y.append("namgo")
y.append("namgo")#adding namgo at the last of the list
print(y.count("namgo"))#count the frequency of namgo
y.reverse()#reversing the list of elements
print(y)
y.pop(1)#popping or removing or deleting element at the given index
print(y)
y.insert(3,"apple")#inserting element at the index 
print(y)

#output
['banana', 'kiwi']
['banana', 'kiwi', 'jiwi']
['banana', 'kiwi', 'jiwi']
[]
banana kiwi jiwi
['banana', 'jiwi', 'kiwi']
['kiwi', 'jiwi', 'banana']
['kiwi', 'jiwi']
2
['namgo', 'namgo', 'jiwi', 'kiwi']
['namgo', 'jiwi', 'kiwi']
['namgo', 'jiwi', 'kiwi', 'apple']
