#Write a program in Python to swap between two numbers without using a third variable.
#Input:
#a = 4
#b = 6

#Expected Output After swapping:
# a is 6 and b is 4


a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
print(f"\na is {a} b is {b}")
a = a + b
b = a - b
a = a - b
print("\nafter swapping")
print(f"a is {a} b is {b}")