#21. WAP to accept a positive number N and calculate M= 2N (2 raised to power N). and calculate the sum of digits of M till we gets single digit number.
#Sample input:
#Enter N value:  6
#Expected output: 1
#3Explanation:  
#If N=6 then M= 26  ==> 64
#Here 64 is not a single digit, so we need to do sum:  6+4==> 10  ==>  1+0===> 1,M=1

num=int(input("Enter number")) # 6 ==>  64

s=2**num
result=s
while result>9:
    s=result  # 10
    result=0  # 1
    while s!=0:
        result=result+(s%10)
        s=s//10
print(result)