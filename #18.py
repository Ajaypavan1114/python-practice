#18. WAP to accept string from user and find following
#a. Number of alphabets in each word.
#b.  Number of vowels  and number of consonant's in each word.
#c.  Number of digits in each word

acount=0
vcount=0
ccount=0
dcount=0
str=input("Enter string")  #  Hai hello 123hi @#bitLabs
words=str.split(" ")
for word in words:
    for ch in word:
         if ch>='A' and ch<='Z' or ch>='a' and ch<='z':
             acount=acount+1
             if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
                 vcount=vcount+1
             else:
                 ccount=ccount+1
         elif ch>='0' and ch<='9':
            dcount=dcount+1
             
    print("Alphabets in ",word," is : ",acount)
    print("vowels in ",word," is: ",vcount)
    print("Consonents in ",word," is: ",ccount)
    print("Digits in ",word," is: ",dcount)
    acount=0
    vcount=0
    dcount=0
    ccount=0