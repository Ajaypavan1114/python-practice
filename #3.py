#3.  WAP to accept salary and 3 shopping bills from user and find 
  #1. total shopping amount
  # 2. find how much % of amount he/she spent on shopping on his salary.


salary=float(input("Enter salary amount"))
bill1=float(input("Enter bill1 amount"))
bill2=float(input("Enter bill2 amount"))
bill3=float(input("Enter bill3 amount"))

total=bill1+bill2+bill3
print("Total bill amount :",total)
percentage=(total/salary)*100
print("% of amount on shopping is :",percentage)