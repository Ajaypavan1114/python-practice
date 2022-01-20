bill=0
if units<=50:
     bill=units*0.75;
elif units<=150:
     bill=(50*0.75)+(units-150)*2.10
elif units<=250:
     bill =(50*0.75)+(150*2.10)+(units-250)*2.50
else:
     bill =(50*0.75)+(150*2.10)+(250*2.50)+(units-250)*2.80