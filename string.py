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
