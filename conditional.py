#checking number is positive or negative using if-else statement 
x=int(input("enter the number"))
if x<0:
    print("The number is negative")
else:
    print("The number is positive")

#validating the name entered with username we have 
user_name="rahul"
y=input("enter the name:")
if user_name == y:
    print("the name is valid")
else:
    print("the name is invalid")

# finding the biggest number among entered two numbers 
a=int(input("enter first number:"))
b=int(input("enter second number:"))
if a>b:
    print("biggest number is :" , a)
else:
    print("biggest number is :" , b)

# finding the biiggest number among entered teree numbers 
e =  int(input("enter first number:"))
f = int(input("enter second number:"))
g = int(input("enter third number:"))
if e>f and e>g:
    print("The biggest number is" , e)
elif f>g:
    print("the biggest number is:" , f)
else:
    print("the biggest number is:" , g)
