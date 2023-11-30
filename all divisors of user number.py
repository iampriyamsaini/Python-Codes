# write a pp to display 
# all the divisors of the given number
n=int(input("Enter a number: "))
for i in range(1,n+1):
    if n%i==0:
        print(i)