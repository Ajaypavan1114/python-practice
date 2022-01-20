n1 =int(input("enter n1="))
n2 =int(input("enter n2="))

print("Prime numbers betweenare: ")

for num in range(n1, n2 + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
           
           
