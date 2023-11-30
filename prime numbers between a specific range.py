#prime numbers between a specific range
lower=int(input("enter 1st number: "))
upper=int(input("enter last number: "))
for n in range(lower, upper+1):
    flag=True
    for i in range (2,n):
        if(n%i==0):
            flag=False
            break
    if(flag==True):
            print(n)