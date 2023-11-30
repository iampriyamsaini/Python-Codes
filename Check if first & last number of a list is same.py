# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

# Example:

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]
# Expected Output:

# Given list: [10, 20, 30, 40, 10]
# result is True

# numbers_y = [75, 65, 35, 75, 30]
# result is False


lst=list(map(int, input("Enter list elements: ").split()))
if(lst[0]==lst[-1]):
    print("True")
else:
    print("False")
