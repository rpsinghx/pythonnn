str1="ranjeev's diary"
str2='hi i am a great "artist"'
print(str1)
print(str2)

c=bool("") + 34-4
print(c)
d=bool("hi") + 34-4
print(d)

#string slicing
a="python"
print(a[0])
print(a[len(a)-1])
print(a[-1])
print(a[-len(a)])
for i in range(len(a)):
    print(a[i])
for i in range(-len(a),0,-1):
    print(a[i])

#slicing in python
x="python in GLA CL2"
print(x)
print(x[::])
print(x[2:6:2])
print(x[10:13])
print(x[-5:-8:-1])
print(x[12:9:-1])

#operators in python
print("python"+" in GLA CL2")
print("python"*5)
print(3*"python")

print('b' not in 'apple')

#loop in string
s1='abcdefg'
s2='abcd'
print(s1==s2)
if(s1==s2):
    print('both are same')
else:
    print("not same")

#built in functions in string
#method to remove spaces
s=" Amit Singh "
print(len(s.strip()))

t1= "python is a programming language. Python is easy to learn. Python is used in "
print(t1.find("Python")) # if you are not sure the value is in there use find function
print(t1.index("Python",35)) # if you need definitive or you are sure that the string is there use index
# print(t1.rfind("Zython"))
# print(t1.index("Zython",35))

output= "Yes" if t1.find("Python")!=-1 else "No"
print(output)
output = "Yes" if "Python" in t1 else "No"
print(output)

print(id(t1))
t2=t1.count("Python")
print(id(t1))
print(t2)
for i in t1:
    print(i,t1.count(i)) if t1.count(i)>2 else None
    print(i,t1.count(i)) if t1.count(i)>15 else None


t3="Rajesh,Suresh,Fazal,Kumar"
t4=t3.split(',')
print(t3 , type(t3))
print(t4 , type(t4))
for item in t4:
    print(item, t3.count(item))

dob=input("enter the date of birth (DD/MM/YYYY)")
year=dob.split("/")
print(year[2])

l1=["22","11","2022"]
d1='-'.join(l1)
print(d1)
print(type(s1))

f1="Amit Kumar"
print(f1)
print(f1.upper())
print(f1.lower())
print(f1.title())
print(f1.capitalize())
print(f1.swapcase())

print(f1.isupper())
print(f1.islower())
print(f1.isalpha())
print(f1.isalnum())
print(f1.isdigit())
print(f1.isnumeric())
print(f1.isidentifier())
print(f1.isprintable())
val=input("enter any value:")
a=eval(val) if val.isnumeric() else val
print(a)

#formatting strings
name="Rakesh"
salary=101
age=16
place="jammu"
print("{}'s salary is {} and his age is {}".format(name,salary,age))
f1=f"{name} is a good boy. He studies in {place}"
print(f1)
