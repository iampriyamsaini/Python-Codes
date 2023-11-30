# Given a integer as a input and replace all the '0' with '5' in the integer

# Explanation
# Check each digit , if it is nonzero, then no change required but if it is zero then replace it by 5.


def replace_zero_with_five(n):
    num_str = str(n)
    modified_str = num_str.replace('0', '5')
    modified_num = int(modified_str)
    return modified_num

n = int(input("Enter an integer: "))
result = replace_zero_with_five(n)
print(result)
