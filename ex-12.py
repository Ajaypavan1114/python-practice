amount=int(input("Enter withdraw amount"))
a=0
b=0
c=0
if amount>=500:
        a=amount//500
        amount=amount-(500*a)
        print("500 rupees notes are ;",a)
if amount>=200:
        b=amount//200
        amount=amount-(200*b)
        print("200 rupees notes are ;",b)
if amount>=100:
        c=amount//100
        amount=amount-(100*c)
        print("100 rupees notes are ;",c)        