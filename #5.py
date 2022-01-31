#5 WAP to accept project marks, internal marks and external marks and find total marks.
#total_marks= 70% from project+ 20% from external +10% from internal

project_marks=int(input("Enter project marks"))
internal_marks=int(input("Enter internal_marks"))
external_marks=int(input("Enter external marks"))


total=(70*project_marks)/100+(20*external_marks)/100+(10*internal_marks)/100

print("The totalmarks is :",total)