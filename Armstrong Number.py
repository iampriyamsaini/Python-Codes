# Write a function which returns True if the number is an armstrong number and False otherwise, where Armstrong number is defined as follows.
# A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if, abcd… = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ….  1634 is an Armstrong number 
# 634 is an Armstrong number as 1634 = 1^4 + 6^4 + 3^4 + 4^4            and            371 is an Armstrong number as 371 = 3^3 + 7^3 + 1^3

# Explanation:
# Use functions. Write a function to get check if the number is armstrong number or not. Numbers are armstrong if it is equal to sum of each digit raised to the power of number of digits.



def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == number
number = int(input("Enter a number: "))
if 0 < number < 1000000000:
    print(is_armstrong_number(number))
else:
    print("Invalid input")
