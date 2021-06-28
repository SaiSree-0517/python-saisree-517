#variable length arguments
"""
an argument that can accept variable number of values.
1.To indicate that the function can take variable number
of argument you write a variable argument using a ‘*’, for example *args.
2.Variable arguments help where the exact number of arguments are not known in the beginning, it also
helps to make your function more flexible.
3.variable name can be any variable name for example *numbers, *names.....etc,,.
4.Using variable length argument you can pass zero or more arguments to a function.
5.Values pass to *args are stored in a tuple.
6.Before variable args you can have a formal argument but not after a variable args.
After variable argument you can have keyword arguments.
"""
#example1:function to add two numbers
def add_num(num1, num2):
    return num1 + num2
result = add_num(5,6)
print('Sum is', result)#Sum is 11

#the above function can take only two values 
"""
result = add_num(5,6,7)#passing more than 2 values to the function 
print('Sum is', result)#TypeError: add_num() takes 2 positional arguments but 3 were given
"""
"""
to avoid the above error we can replace the variable as variable length argument using*
which can accept variable values(i.e any number of values) and the function can now add n values.
"""
def add_num(*args):#here *args represents variable length argument
  sum = 0
  for num in args:
      sum += num
  return sum

result = add_num(5, 6, 7)
print('Sum is', result)#Sum is 18

result = add_num(5, 6, 7, 8)
print('Sum is', result)#Sum is 26

result = add_num(5, 6, 7, 8, 9)
print('Sum is', result)#Sum is 35
#to check the type of variable length arguments
def add_n(*args):
  sum = 0
  print(type(args))#<class 'tuple'>
  for num in args:
      sum += num
  return sum

result = add_n(5, 6, 7)
print('Sum is', result)#Sum is 18
