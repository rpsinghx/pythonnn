def printdata(x):
    if x==11:
        return
    else:
        printdata(x+1)
        print(x)
printdata(1)

# to find the factorial of 3 by reccursion and with function 

def factorial(a):
    if a==0:
        return 1
    else:
        return a*factorial(a-1)
print(factorial(5))

#to find the power of the number using reccursion
def power(r,t):
    if t==0:
        return 1
    else:
        return r*power(r,t-1)
print(power(2,3))