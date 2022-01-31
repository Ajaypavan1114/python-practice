#17. WAP to accept string from user and find following
#a. Number of alphabets
#b.  Number of digits
#c. Number of special characters
#d. Number of words

str=input("Enter string :") # Password@123
acount=0
dcount=0
wcount=1
scount=0
for ch in str:
    if ch>='A' and ch<='Z' or ch>='a' and ch<='z':
        acount=acount+1
    elif ch>='0' and ch<='9':
        dcount=dcount+1
    elif ch!=' ':
        scount=scount+1
    else:
        wcount=wcount+1
print("Number of words: ",wcount)
print("Number of Alphabets: ",acount)
print("Number of digits: ",dcount)
print("Number of special characters: ",scount)
