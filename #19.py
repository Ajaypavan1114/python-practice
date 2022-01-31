#19. WAP to accept  string and find longest word in a given string. 
str=input("Enter string") # hi hello welcome to bitLabs
words=str.split(" ")
max=0
result=''
for word in words:
    if max<len(word):
        max=len(word)
        result=word
print(result)