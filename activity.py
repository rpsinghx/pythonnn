S = str(input("enter the string :"))
a = S.count("#")
b = S.count("*")

if a == b:
    print("0")
if a>b:
    print("-1")
if b>a:
    print("1")

    