# positional arguements 

def add(a, b):
    return a + b

# 5 goes to a, 10 goes to b
print(add(5, 10))

# keyword arguements

def details(name,age):
    print("Name is :",name)
    print("Age is :",age)
details("Amit", 12)
details(age=12 , name="Amit")
#here we are passing the arguements in different order but is will work because we are using keyword arguemnets


#default arguements 

def details(name, age = 12):
    print("Name is:",name)
    print("age is :",age)

details(name="Amit") # age = 12
details(name="Amit",age=15)

# variable length arguements 
def add(a,*b): # here b is tuple
    print(type(a))
    print(type(b))

    sum=0
    for i in b:
        sum+=i
    return sum+a

print(add(12,34,54,14,15,42))
print(add(12,34,14,15,18,75,79,74,65,84,35,45))
print(add(12,))
print(add(12))

#keyword variable-length arguemnet 


