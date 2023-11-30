# Take N as input. Print Nth Fibonacci Number, given that the first two numbers in the Fibonacci Series are 0 and 1.

# Input Format
# Constraints
# 0 <= N <= 1000

# Output Format
# Sample Input
# 10
# Sample Output
# 55
# Explanation
# The 0th fibonnaci is 0 and 1st fibonnaci is 1.



def nth_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b
N = int(input("Enter a number: "))
result = nth_fibonacci(N)
print(result)

