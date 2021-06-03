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
y.sort()
print(y)
y.sort(reverse=True)
print(y)
y.remove("banana")#banana will be removed
print(y)
y.append("namgo")
y.append("namgo")
print(y.count("namgo"))
y.reverse()
print(y)

output:
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
