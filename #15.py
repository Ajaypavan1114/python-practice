#15. WAP to accept two numbers and print prime numbers between them.
#Sample input: 
#Enter start number : 10
#Enter stop number:  100


n1=int(input("Enter n1 value"))
n2=int(input("Enter n2 value"))
count=0
for i in range(n1,n2+1):
    for j in range(1,i//2+1):
        if i%j==0:
            count=count+1
    if count==1:
        print(i,end=" ")
    count=0