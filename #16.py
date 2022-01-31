#16. WAP to check given string is palindrome string or not without using predefined functions.
string=input("Enter string :")#malayalam
count=0
i=0
j=len(string)-1
while i!=j:
    if string[i]==string[j]:
        count=count+1
        i=i+1
        j=j-1
    else:
        break
if count==len(string)//2:
    print(string," IS A Palindrome")
else:
    print(string,"IS Not a palindrome")