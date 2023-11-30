# take a 'n' user given number as input 
# Display numbers divisible by n from a list
# Iterate the given list of numbers and print only those numbers which are divisible n

# Expected Output:

# Example list is  [10, 20, 33, 46, 55]       //let user give 5
# Divisible by 5
# 10
# 20
# 55



lst=list(map(int, input("Enter list elements: ").split()))
n=int(input("Enter a number: "))
for i in lst:
    if (i%n==0):
        print(i)
