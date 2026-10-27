L= "which of the following is the best to remove a element from the list /n" \
"A. list.pop()" \
"B. list.remove()" \
"C. list.delete()" \
"D.None of the above "
print(L)
lis = ["A","B","C","D"]
x = input("enter your answer:")
x1 = lis[0]
for i in lis:
    if x == x1:
        print("Congo right answer")
        print("+5 points have fun!!")
    elif x != x1:
        print("woooo , Wrong answer ! /n" \
        "-2 points")
    else:
        print("Question PASSED to the next team")
    break