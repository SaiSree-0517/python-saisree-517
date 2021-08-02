"""
1. Write a python program to read the contents of file
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
f1.close()
"""
CONTENTS OF FILE:  Computer Science & Engineering (CSE) is an academic program at many universities which 
comprises scientific and engineering aspects of computing. CSE is also a term often used in 
Europe to translate the name of engineering informatics academic programs.
Size of file using method 1:  257 bytes
Size of file using method 2:  257 bytes
Size of file using method 3: 257 bytes
Number of occurrences of CSE=  2
"""
"""
2.Develop a python code to read the contents of file and find how many upper case letters,
lower cas letters and digits are existed in the file?
contents in text.txt:
AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz  
1 2 3 4 5 6 7 8 9 1
"""
f2=open("text.txt","r")
data=f2.read()
uc=0
lc=0
dig=0
for ch in data:
    if ch.isupper():
        uc+=1
    elif ch.islower():
        lc+= 1
    elif ch.isdigit():
        dig+=1
print("UPPER CASE LETTERS=",uc,"LOWER CASE LETTERS=",lc,"DIGITS=",dig)
f2.close()
"""
UPPER CASE LETTERS= 26 LOWER CASE LETTERS= 26 DIGITS= 10
"""

"""
3. Create a file and insert the records in the following format(Read the records from the user)
SNo      Name      Game
1	 Rahul	  Cricket
2.       David 	  Chess
3.       Ram 	  Volly Ball
"""
fp=open("GamesRecord.txt","w")
t=["SNo\t","Name\t","Game\n"]
fp.writelines(t)
n=int(input("Enter number of rows: "))
for i in range(n):
    fp.writelines([input(),"\t",input(),"\t",input()])
    fp.write("\n")
fp.close()
fp1=open("GamesRecord.txt","r")
data=fp1.read()
print(data)
fp1.close()
"""
Enter number of rows: 3
1.
Rahul
Cricket
2.
David
Chess
3.
Ram
VollyBall
SNo	Name	Game
1.	Rahul	Cricket
2.	David	Chess
3.	Ram	VollyBall
"""

"""
4.Consider any real time application like banking, college automation, stock market etc.,
and make use of user defined exceptions according to application and raise that exception
"""
class Insufficient_balance_Exception(Exception):
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value
    # __str__ is to print() the value
    def __str__(self):
        return(repr(self.value))
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
  
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
  
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        try:
            if self.balance>=amount:
                self.balance-=amount
                print("\n You Withdrew:", amount)
            else:
                raise Insufficient_balance_Exception(amount)
        except Insufficient_balance_Exception as e:
            print("Insufficient_balance_Exception ",e.value,"is greater than the amount in account......!")
            
    def display(self):
        print("\n Net Available Balance=",self.balance)
  
# Driver code
   
# creating an object of class
s = Bank_Account()
   
# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()
"""
Hello!!! Welcome to the Deposit & Withdrawal Machine
Enter amount to be Deposited: 5000

 Amount Deposited: 5000.0
Enter amount to be Withdrawn: 6000
Insufficient_balance_Exception  6000.0 is greater than the amount in account......!

 Net Available Balance= 5000.0
"""

