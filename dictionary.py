#dictionary to store branchcode ->name
dict_ds={5:"CSE",12:"IT",3:"ECE",4:"MECH"}
print(dict_ds)
#type of dict_ds
print(type(dict_ds))
res=dict_ds[12]
print("at key 12 the value is {}".format(res))
dict_ds1={5:"CSE-A",5:"CSE-C","Name":"Priya","Fname":"Priya"}
print(dict_ds1)
#modify the values
dict_ds1["Fname"]="devi"
print(dict_ds1)
#add new keys
dict_ds1["Department"]="CSE"
print("new dict after adding new keyvalue",dict_ds1)
"""
{5: 'CSE', 12: 'IT', 3: 'ECE', 4: 'MECH'}
<class 'dict'>
at key 12 the value is IT
{5: 'CSE-C', 'Name': 'Priya', 'Fname': 'Priya'}
{5: 'CSE-C', 'Name': 'Priya', 'Fname': 'devi'}
new dict after adding new keyvalue {5: 'CSE-C', 'Name': 'Priya', 'Fname': 'devi', 'Department': 'CSE'}
"""
