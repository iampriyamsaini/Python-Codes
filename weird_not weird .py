# Write a program for given an integer n, perform the following conditional actions:


# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird




n=float(input("Enter any number: "))
if (n%2!=0):
 print("weird")
for n in range(n<=5):
    if(n%2==0):
        print("not weird")
for n in range(n>6 and n<=20):
    if(n%2==0):
        print("weird")        

for n in range(n>20):
    if(n%2==0):
        print("not weird")          
        
