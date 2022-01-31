#25. WAP to print following patten.
#10 11 12 13 14
#90 89 88 87 86 
#15 16 17 18 19
#85 84 83 82 81
#20 21 22 23 24

count1=10
count2=90
for i in range(5):
    for j in range(5):
        if i%2==0:
            print(count1,end=" ")
            count1=count1+1
        else:
            print(count2,end=" ")
            count2=count2+1
    print()
