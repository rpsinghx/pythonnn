a=10 
b=20
c=-5
d=(a if a>c else c) if a>b else (b if b>c else c)
print(d)

# arithmetic operators
# + addition a+b 
# - subbraction a-b
# * multiplication a*b
# / division a/b
# % remainder a%b
# ** exponent power a**b
# // integer division a//b
x = 10
y = 3
print(x-y)
print(x+y)
print(x*y)
print(x%y)
print(x**y)
print(x//y) 

# relational operators
# > , < , >= , <= , != , ==

#logical operators 
# and - if both are true then true otherwise false 
# or - if one of the numbers is true then it is true 
# nor - if both of the numbers is false then it is true 

c = (-34 and 5)+9
print(c)

d = (-34 or 5)+9
print(d)

#assignment operators 
# =   --  x = a + b 
# +=  --  a +=5
# -=  --  a -=5

i = 13 
o = 5
i +=5
o-=5
print(i)
print(o)

# unary operators 
a = 10 
print(a)
print(-a)

# membership operators
text = "welcome to python programming"
print("welcome" in text)
print("Welcome" in text)
print("nireekshan" in text)
print("Han" not in text)

a = 15
b = 15 
print(id(a))
print(id(b))

a = 25 
b = 30
print( a is b )
print(id(a))
print(id(b))

