name = input("enter the name :")
eng = int(input("enter english marks"))
hin = int(input("enter hindi marks"))
math = int(input("enter maths marks"))
sci = int(input("enter science marks"))
geo = int(input("enter geography marks"))
his = int(input("enter history marks"))

sum = eng + hin + math + sci + geo + his
print("Sum of all subjects marks is" , sum)

avg = (sum/6)
print("The average of marks of all subjects is" , avg)

if 100>= avg >= 90 :
    print("Grade is A+")
if 89 >= avg >= 80:
    print("Grade is A")
if 79 >= avg >= 70:
    print("Grade is B+")
if 69>= avg >= 60:
    print("Grade is B")
if 59>= avg >= 45:
    print("Grade is C")
if 44>= avg >= 33:
    print("Grade is D")
if 32>= avg >=0:
    print("Fail")

result = avg
if result >32:
    print(name.upper() , "has PASSED")
else:
    print(name.upper() , "has FAILED")

