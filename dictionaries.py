#creating a empty dictionaries

d3={}
d3[1] = "ramesh"
d3[2] = "suresh"
d3[3] = "mahesh"
print(d3)


#accesing dictionaries in python
d1 = {1:"ram",2:"sita",3:"lakshman"}
print(d1[1])
print(d1[2])
print(d1[3])


#how to handle the key error in dictornaries
d2 = {1: 'Ramesh', 2: 'Suresh', 3: 'Mahesh'}
if 400 in d2:
 print(d2[400])
else:
 print("key not found")


 #working with dictionary
 d={}
n=int(input("Enter number of employees: "))
i=1
while i <=n:
 name=input("Enter Employee Name: ")
 salary=input("Enter Employee salary: ")
 d[name]=salary
 i=i+1
for x in d:
 print("The name is: ", x ," and his salary is: ", d[x])


 #updating dictionary in python 

 d5 = {1:"23" , 2:"24"}
 d5[10] = "45"
 print(d5)


 
