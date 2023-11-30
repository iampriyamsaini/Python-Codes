sal = eval(input("Enter your salary: "))
years = eval(input("Enter your service years: "))
if years>=5:
   sal = sal + 0.05*sal
   print(f"your salary is: {sal}")
   
else:
    print(f"your salary is: {sal}") 
   