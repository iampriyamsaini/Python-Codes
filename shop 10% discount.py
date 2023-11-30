unit=eval(input("enter units you purchased,1 unit=100rs: "))
cost=unit*100
if cost>=1000:
   cost=cost-0.1*cost
   print("cost is",cost)
   
else:
    print("cost is",cost)   
   
    
    
    