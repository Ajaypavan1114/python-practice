#23.  WAP to print following patten. 
#1 1 1 1 1
#0 0 0 0 0
#1 1 1 1 1
#0 0 0 0 0
#1 1 1 1 1
for i in range(5):
    for j in range(5):
        if i%2==0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()