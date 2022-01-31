#12.WAP to accept units from user and find the bill.
 # for first 50 units the charges are: 0.75p/u
  #next 100 units the charges are: 2.10p/u
  #next 100 units the charges are : 2.50p/u
  #above 250 units the charges are: 2.80p/u
  
units=float(input("Enter units"))
if units<50:
    charges=(0.75*units)
    print(charges)
      
      
elif units<150:
    charges=(2.10*units)
    print(charges)  
      
elif units<250:
    charges=(2.50*units)
    print(charges)  
elif units>250:
    charges=(2.80*units)
    print(charges)  
