S=str(input("Enter the string"))
RS=S[::-1]
print(RS)
if RS==S:
    print("This is a palindrome")
else:
    print("This is not palindrome")