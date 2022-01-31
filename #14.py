#14. WAP to accept project marks, external marks, internal marks from student,
 #  --> check if student got pass in project, internal and externals. 
  #  Note: pass mark is : 50
   #--> if student got pass in project, internal and external then find total score.
#     total_score= 70% from project+ 20% from external + 10% internal 
#  --> print grades based on total_score
#        total_score >=90    --> A grade
#		75--90      --> B grade
#                50- 75      --> C grade
#   ---> print failed subject name along with the score.





project_marks=int(input("Enter project marks"))
internal_marks=int(input("Enter internal_marks"))
external_marks=int(input("Enter external marks"))
total=0

if project_marks<=50:
    print("Failed in project :",project_marks)
if internal_marks<=50:
    print("Failed in internal :",internal_marks)
if external_marks<=50:
    print("Failed in external :",external_marks)
    
if project_marks>=50 and internal_marks>=50 and external_marks>=50:
    total=(70*project_marks)/100+(20*external_marks)/100+(10*internal_marks)/100
    print("The totalmarks is :",total)
    
if total>=90:
    print("A grade :",total)
if (total>=75 and total<90):
    print("B grade :",total)
if (total>=50 and total<75):
    print("C grade :",total)