# Given coefficients of a quadratic equation , you need to print the nature of the roots (Real and Distinct , Real and Equal or Imaginary) and the roots.
# If Real and Distinct , print the roots in increasing order.
# If Real and Equal , print the same repeating root twice
# If Imaginary , no need to print the roots.

# Note : Print only the integer part of the roots.

# Input Format
# First line contains three integer coefficients a,b,c for the equation ax^2 + bx + c = 0.

# Constraints
# -100 <= a, b, c <= 100

# Output Format
# Output contains one/two lines. First line contains nature of the roots .The next line contains roots(in non-decreasing order) separated by a space if they exist. 
# If roots are imaginary do not print the roots. Output the integer values for the roots.

# Sample Input
# 1 -11 28
# Sample Output
# Real and Distinct
# 4 7
# Explanation
# The input corresponds to equation ax^2 + bx + c = 0. Roots = (-b + sqrt(b^2 - 4ac))/2a , (-b - sqrt(b^2 - 4ac))/2a




import math

# Input reading
a, b, c = map(int, input().split())

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check the nature of the roots
if discriminant > 0:
    # Real and Distinct Roots
    root1 = int((-b + math.sqrt(discriminant)) // (2*a))
    root2 = int((-b - math.sqrt(discriminant)) // (2*a))
    print("Real and Distinct")
    print(root2, root1)
elif discriminant == 0:
    # Real and Equal Roots
    root = int(-b // (2*a))
    print("Real and Equal")
    print(root, root)
else:
    # Imaginary Roots
    print("Imaginary")




