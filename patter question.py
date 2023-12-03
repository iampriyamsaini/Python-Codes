#Write a program in Python to display a below-given pattern.

#Input: 6
#Expected Output:
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5
#6 6 6 6 6 6

n = int(input("Enter number: "))
for i in range(n+1):
    for j in range(i):
        print(i, end=" ")
    print("\n")