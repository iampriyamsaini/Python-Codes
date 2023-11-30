n=int(input("enter a number: "))
while(n>0):
    lastdigit=n%10
    print(lastdigit,end='')
    n=n//10