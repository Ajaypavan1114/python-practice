#8 WAP to accept number and check it is Even or odd or Zero

num=int(input("Enter a Number"))

if num==0:
    print("The given number is ZERO :",num)
elif num%2==0:
    print("The given number is EVEN :",num)
else:
    print("The given number is ODD :",num)
        