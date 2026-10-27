def display():
    print("welcome to function")
display()
display()
display()


def sum(a,b):
    print("sum of numbers :",(a+b))
sum(20,30)

val = print("Yes") if 12>45 else print("No")
print(val)

def add(a,b):
    c = a+b
    return c
x=add(1,2)
print("sum of numbers:",x)

def m1():
    print("This function is returning nothing")
m1()
x=m1()
print(x)

#show to return multiple values from a function in python


def n1(a,b):
    c = a + b 
    d = a - b
    return c,d
x,y = n1(10,5)
print("sum of numbers:",x)
print("dif of numbers:",y)

def fun():
    print("we assigned function to variable")
sum=fun
sum()

def message(text):
    print("hello",text)
def printmessage(a,b,x):
    print("sum is:",(a+b))
    x("john")
printmessage(10,20,message)

def outer():
    print("Outer-function")
    def inner():
        print("Inner-function")
    inner()
outer()

# a funtion can return a another funtion 
def outer():
    print("Outer-function")
    def inner():
        print("Inner-function")
    return inner
func1 = outer()
func1()


def createafunction():
    def add(p,q):
        return p+q
    def sub(p,q):
        return p-q
    return add,sub
func1,func2=createafunction()
print(func1(12,34))
print(func2(12,34))



#scope = lifetime is a duration btw variable memory allocation and memory deallocation perform by pvm(python vitual machine)
# scope is defined as the duration where the variable is accessible


# local variable in python
# def m():
#     a=11
#     print(a)
# m()

# def m1():
#     a=11
#     print(a)
# def n():
#     print(a) # name error print statement
# m()
# n()


# global variable in python 

a1 = 11
b1 = 12
def m2():
    print("a1 from function m2():",a1)
    print("b1 from function m2():",b1)
def n2():
    print("a1 from function n2():",a1)
    print("b1 from function n2():",b1)
m2()
n2()

# global and local variable having same name in python

t = 1
def t1():
    t=2
    print("a value from t1() function:",t)
def t2():
    print("a value from t2() function:",t)
t1()
t2()


t1 = 1
def t():
    global t1 # if you want to use global variable use the global key 
    t1 = 2
    print("t1 value from t() function:",t1)
def t3():
    print("t1 value from t() function:",t1)
t()
t3()

# globals() built in function in python 

s = 1 
def s1():
    s=2
    print(s)
    print(globals()["s"])
s1()