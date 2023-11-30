per1=eval(input("Enter your age: ")) 
per2=eval(input("Enter your age: ")) 
per3=eval(input("Enter your age: "))

if (per1>per2 and per1>3):
    print(per1, "is oldest")
    
if (per2>per1 and per2>per3):
    print(per2, "is oldest")  
    
if (per3>per1 and per3>per2):
    print(per3, "is oldest")  
    
if (per1<per2 and per1<3):
    print(per1, "is younger")
    
if (per2<per1 and per2<per3):
    print(per2, "is younger")  
    
if (per3<per1 and per3<per2):
    print(per3, "is younger")       
    
    