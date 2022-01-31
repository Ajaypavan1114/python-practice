#4 WAP to accept basic salary and find gross salary.
 #Gross_salary= basic+HRA+DA
 #DA is 80% on basic
 #HRA is 76% on basic
 
basic_sal=float(input("Enter basic salary"))
DA=(80*basic_sal)/100
HRA=(76*basic_sal)/100
 
gross_salary=basic_sal+DA+HRA
print("The Gross salary is :",gross_salary)
