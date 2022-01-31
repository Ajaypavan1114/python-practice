#24. WAP to print following patten.
#10 11 12 13 14
#15 16 17 18 19
#20 21 22 23 24 
#25 26 27 28 29
count=10
for i in range(4):       
    for j in range(5):
        print(count,end=" ")
        count=count+1
    print()