#staircase pattern code with nested loops 
# for x in range(1,6):
#     for y in range(x):
#         print(y,end=" ")
#     print()


#staircase pattern code with reverse pattern nested loops
for x in range(5,0,-1):
    for y in range(x):
        if y%2==0:
            print("#",end=" ")
        else:
            print("*",end=" ")
    print()

#break statemnent 

group=[1,2,3,4]
search=int(input("enter the element in search:"))
for element in group:
    if search == element:
        print("element found in group")
        break
    else:
        print("element not found")

#continue statement

cart=[10,20,500,700,50,60]
for item in cart:
    if item>=500:
        continue
    print("item:",item)


for i in range(1,501):
    if i%5 !=0 and i%3 !=0:
        continue
    print(i)

#while statements

num=1
while num<10:
    print("hi")
    num+=1
    if num==3:
        break
else:
    print("hello")




