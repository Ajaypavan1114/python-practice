#13. WAP to accept withdraw amount and print number of notes. consider we have 500, 200 and 100 rupees notes.


amount=int(input("Enter withdraw amount"))

a=0
b=0
c=0

if amount>=500:
    a=amount//500
    amount=amount-(500*a)
    print("The number of 500 Notes are :",a)
    
if amount>=200:
    b=amount//200
    amount=amount-(200*b)
    print("The number of 200 notes are :",b)
    
if amount>=100:
    c=amount//100
    amount=amount-(100*c)
    print("the number of 100 notes are :",c)
