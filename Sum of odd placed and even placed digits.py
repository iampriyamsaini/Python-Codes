# Take N as input. Print the sum of its odd placed digits and sum of its even placed digits.

# Input Format:
# Constraints
# 0 < N <= 1000000000

# Output Format:

# Sample Input:
# 2635

# Sample Output:
# 11
# 5

# Explanation:
# 5 is present at 1st position, 3 is present at 2nd position, 6 is present at 3rd position and 2 is present at 4th position.
# Sum of odd placed digits on first line. 5 and 6 are placed at odd position. Hence odd place sum is 5+6=11
# Sum of even placed digits on second line. 3 and 2 are placed at even position. Hence even place sum is 3+2=5



def sum_odd_even_digits(N):
    num_str = str(N)
    odd_sum = 0
    even_sum = 0
    for i in range(1, len(num_str) + 1):
        digit = int(num_str[i - 1])

        if i % 2 == 1:
            odd_sum += digit
        else:
            even_sum += digit

    print(odd_sum)
    print(even_sum)

N = int(input('Enter a number: '))

if 0 < N <= 1000000000:
    sum_odd_even_digits(N)
else:
    print("Invalid input")
