amount=int(input("Enter withdraw amount"))
if amount>=200:
        a=amount//200
        amount=amount-(200*a)
        print("200 rupees notes are ;",a)
if amount>=100:
        b=amount//100
        amount=amount-(100*b)
        print("100 rupees notes are ;",b)
if amount>=50:
        c=amount//50
        amount=amount-(50*c)
        print("50 rupees notes are ;",c)  
if amount>=20:
        d=amount//20
        amount=amount-(20*d)
        print("20 rupees notes are ;",d)
if amount>=10:
        e=amount//10
        amount=amount-(10*e)
        print("10 rupees notes are ;",e)        