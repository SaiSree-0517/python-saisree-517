"""
Write a python program to read the contents of file
and count the size of file then count how many times
“CSE” is existed in the file.
"""
import os
f1=open("sample.txt","r")
data=f1.read()
print("CONTENTS OF FILE: ",data)
size = os.path.getsize('sample.txt') #using os.path.getsize("text file name")
print('Size of file using method 1: ', size, 'bytes')
s=os.stat("sample.txt")#using os.stat("filename"),object.st_size
print("Size of file using method 2: ",s.st_size,"bytes")
f1.seek(0,os.SEEK_END)#by moving the cursor reading the file 
print("Size of file using method 3:",f1.tell(),"bytes")#object.tell()-->returns the size of file
occurrences=data.count("CSE")
print("Number of occurrences of CSE= ",occurrences)
"""
CONTENTS OF FILE:  Computer Science & Engineering (CSE) is an academic program at many universities which 
comprises scientific and engineering aspects of computing. CSE is also a term often used in 
Europe to translate the name of engineering informatics academic programs.
Size of file using method 1:  257 bytes
Size of file using method 2:  257 bytes
Size of file using method 3: 257 bytes
Number of occurrences of CSE=  2
"""
