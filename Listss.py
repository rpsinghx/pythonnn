#accessing list by using indexing in python
names = ["Prabhas", "Prashanth", "Prakash"]
print(names)
print(names[0])
print(names[1])
print(names[2])
print(type(names))
print(type(names[0]))
print(type(names[1]))
print(type(names[2]))


#slicing in list
u = [1, 2, 3, 4, 5, 6]
print(u)
print(u[2:5:2])
print(u[4::2])
print(u[3:5])


#len() in list
c = [1, 2, 3, 4, 5]
print(len(c))


#count in list
p = [1, 2, 3, 4, 5, 5, 5, 3]
print(p.count(5))
print(p.count(3))
print(p.count(2))


#append in list
k=[] #empty list
k.append("Ramesh")
k.append("Suresh")
k.append("Naresh")
print(k)


#insert in list
l=[10, 20, 30, 40]
print(l) 
l.insert(1, 111)
print(l) 
l.insert(-1, 222)


#extend in list
l1 = [1,2,3]
l2 = ['Rahul', 'Rakesh', 'Regina']
print('Before extend l1 is:', l1)
print('Before extend l2 is:', l2)
l2.extend(l1)
print('After extend l1 is:', l1)
print('After extend l2 is:', l2)


#remove method in list
a=[1, 2, 3]
a.remove(1)
print(a)


#pop method in list
n=[1,2,3,4,5]
print(n.pop(1))
print(n)
print(n.pop())
print(n)


#reverse in list
o=[1, 2, 3, 4, 'two']
print(n)
o.reverse()
print(o)


#sort in list
d=[1, 4, 5, 2, 3]
d.sort()
print(n)
s=['Suresh', 'Ramesh', 'Arjun']
s.sort()
print(s)


#list aliasing and cloning in python:
#cloning in list python 
x=[10, 20, 30]
y=x[:]
print(x)
print(y)
print(id(x))
print(id(y))
x[1] = 99
print(x)
print(y)
print(id(x))
print(id(y))

 
#cloning using copy method 
v=[10, 20, 30]
b=v.copy()
print(v)
print(b)
print(id(v))
print(id(b))


#concatenation opeartor (+) in list
a1= [1, 2, 3]
b1= [4, 5, 6]
c1 = a1 + b1
print(c1)


#mulyiplicatio operator(*) in list 
a2 = [1,2,3]
print(a2)
print(2*a2)


#comparision operators in list
print([1, 2, 3] < [2, 2, 3])
print([1, 2, 3] < [1, 2, 3])
print([1, 2, 3] <= [1, 2, 3])
print([1, 2, 3] < [1, 2, 4])
print([1, 2, 3] < [0, 2, 3])
print([1, 2, 3] == [1, 3, 4])


#comparision of string lists in python 
x1 =["abc", "def", "ghi"]
y1 =["abc", "def", "ghi"]
z1 =["ABC", "DEF", "GHI"]
a3 =["abc", "def", "ghi", "jkl"]
print(x1==y1)
print(x1==z1)
print(x1==a3)


#membership operators in list 
x2=[10, 20, 30, 40, 50]
print(20 in x2)
print(20 not in x2)
print(90 in x2) 
print(90 not in x2)


#nested list in python 
a4 = [80, 90]
b4 = [10, 20, 30, a4]
print(b4[0])
print(b4[1])
print(b4[2])
print(b4[3][1])


#lambda expression
abcd = lambda x,y,z:(x+y)-z
print(abcd(3,7,5))


# filter method in list in python 
l2 = [1,2,3,4,5,56,78,2,56]
f = filter(lambda e:e>=10 and e<100,l2)
l3 = list(f)
print(l3)


#map method in list in python 
li = [100 , 200 , 300 , 400]
q = map(lambda t:t+170 , li)
w = list(q)
print(li)
print(w)


#reduce in list in python 
from functools import reduce
each_items_costs = [111, 222, 333, 444]
total_cost = reduce(lambda x, y: x+y, each_items_costs)
print(total_cost)

from functools import reduce 
f2 = reduce(lambda x5,y5:x5 if x5>y5 else y5 ,li)
print(f2)

