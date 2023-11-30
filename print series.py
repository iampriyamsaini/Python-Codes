#Take the following as input.
#A number (N1)
#A number (N2)
#Write a function which prints first N1 terms of the series 3n + 2 which are not multiples of N2.

n1=int(input(''))
n2=int(input(''))
count=0
n=1
while(count<n1):
    x=3*n+2
    if(x%n2!=0):
        print(x)
        count=count+1
    n=n+1
