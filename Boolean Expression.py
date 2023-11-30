# Write a program for given three integers a, b, and x, display a if x is 1 and b if x is 0, using only mathematical or bitwise operations. Assume x can only be 1 or 0.

# Note: flow control statements not allowed (if-else and loops not allowed)

# Input Format

# three integers in separate lines

# 1. first integer value of a
# 2. second integer value of b
# 3. third integer value of x


a=int(input())
b=int(input())
x=int(input())
print(a*x + b*(1-x))
