num1=eval(input("Enter 1st number: "))
num2=eval(input("Enter 2nd number: "))
num3=eval(input("Enter 3rd number: ")) 
if(num1>=num2 and num1>=num3):   
    print(num1,"is largest number")
elif(num2>=num1 and num2>=num3):
    print(num2,"is largest number")
else:
    print(num3,"is largest number")
