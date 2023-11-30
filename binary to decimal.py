#Take any number in binary format. Write a function that converts it to decimal format and Print the value returned
binary_input = (input())
try:
    decimal_result = int(binary_input, 2)
    print(decimal_result)
except ValueError:
    print("Invalid binary number")
