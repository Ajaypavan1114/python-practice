basic_salary=float(input("Enter salary"))

if basic_salary>10000:
             HRA=(70*basic_salary)/100
             DA=(65*basic_salary)/100

             gross_salary=basic_salary+HRA+DA

             print("gross_salary",gross_salary)

elif basic_salary<20000:
    

             HRA=(75*basic_salary)/100
             DA=(73*basic_salary)/100

             gross_salary=basic_salary+HRA+DA

             print("gross_salary",gross_salary)

elif basic_salary>20000:    
    
             HRA=(80*basic_salary)/100
             DA=(76*basic_salary)/100

             gross_salary=basic_salary+HRA+DA

             print("gross_salary",gross_salary)
