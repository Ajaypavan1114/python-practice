#WAP to descending
list = [23, 45, 12, 90, 55, 33]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]<list[j]:
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
print("Desending List is :",list)