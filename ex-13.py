project_marks=int(input("Enter project_marks value"))
external_marks=int(input("Enter external_marks value"))
internal_marks=int(input("Enter internal_marks value"))
total=0
if (project_marks<=50):
         print("fail in project :",project_marks)
if (external_marks<=50):
         print("fail in external :",external_marks)
if (internal_marks<=50):
         print("fail in internal :",internal_marks)
if (project_marks>=50 and external_marks>=50 and internal_marks>=50):
         total=((70*project_marks)/100+(20*external_marks)/100+(10*internal_marks)/100)
         print("pass")
if (total>=90):
         print("A grade:",total)
if (total>=75):
         print("B grade:",total)
if (total>=50 and total<75):
         print("C grade:",total)

    