#tupes in python 
# single value tuple
name =("Sushanth")
print(name)
print(type(name))

name1 =("Sushanth",)
print(name1)
print(type(name1))


#mathematical operators 
#concatenation in tuple 
t1=(10,20,30)
t2=(40,50,60)
t3=t1+t2
print(t3)

#multiplication
t5 = (10,20,30)
t6 = t5*3
print(t6)


#built in function in python 
#len() method
t=(10,20,30,40)
print(len(t))

#count() method
tt=(10,10,10,20)
print(t.count(10))

#index() method
tt1=(10,20,10,10,20)
print(tt1.index(10))

#sorted() method
tt2=(40,20,30,10)
tt3=sorted(tt2)
print(tt2)
print(tt3)
tt4 = sorted(tt2,reverse=True)
print(tt4)

#min() and max() function
print(min(tt2))
print(max(tt2))


#tuple packing
roll = 100
name = "Rpsingh"
email="rpsingh@gmail.com"
phone=64726482648
ttt=roll,name,email,phone
print(ttt)

l=[]
for x in range(3):
    roll = 100
    name = "Rpsingh"
    email="rpsingh@gmail.com"
    phone=64726482648
    ttt1=roll,name,email,phone
    l.append(ttt1)
for r,n,e,p in l:
    print("%5d %-15s %-20s %10s"%(r,n,e,p))


#tuple comprehension
tt7= (x**2 for x in range (1,6))
print(type(tt7))
for x in tt7:
    print(x)
      
