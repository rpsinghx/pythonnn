S=str(input("enter the email:"))
f=S.index("@")
print("Username:" , S[0:f])
print("Domain:" , S[f+1::])

