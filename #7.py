#Find Number of words in a given string
string=input("Enter string :")
total=1
for i in range(len(string)):
    if string[i]==" ":
        total=total+1
print("Number of words are :",total)