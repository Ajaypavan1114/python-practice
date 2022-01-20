x=0
num=int(input("Enter a num=:"))
y=num
if(num):
    i=1
    f=1
    r=num%10
    if(i<=r):
        f=f*i
        i=i+1
    x=x+f
    num=num//10
if(x==y):
    print("The number is a strong number")
else:
    print("The number is not a strong number")