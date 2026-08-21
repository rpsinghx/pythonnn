#printing bytes data type with indexing and fundamentals
x = [10,20,30,40,50]
y = bytes(x)
print(type(y))
print(y[0])
print(y[1])
print(y[2])
print(y[3])
print(y[4])
#printing the byte data type values using for loop 
for a in y:
    print(a)

#range data type in python:
a=range(5)
print(a)
for x in a:
    print(x)
b = range(7)
print(b)
for x in b:
    print(x)

c = range(2,10,3)
print(c)
for x in c:
    print(x)