#inout and output practice
name = input("enter the name")
print("you entered name as:",name)


a = int(input("enter the number"))
b = int(input("enter the number"))
c=a+b
print(c)

x = float(input("enter"))
y = float(input("enter"))
z = x + y
print(z)

#eval() function in python 
a = eval(input("enter the value"))
b = eval(input("enter the value"))
c=a+b
print(c)
print(type(a))

from sys import argv
a=eval(argv[1])
b=eval(argv[2])
c=a+b
print(c)