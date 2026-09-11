sample1=input("Enter")
a=""
a = a + sample1[::2]
print(a)


sample2=input("Enter the sample input")
print(sample2.count("fox"))


sample3=input("enter:")
b=""
for i in sample3:
    if sample3.count(i)>1:
        b = i + str(sample3.count(i))
print(b.strip())    