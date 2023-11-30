# Write a program to accept a string from the user and display characters that are present at an even index number.

# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.


st = input("Enter a word/sentence: ")
print("Original String:", st)
x = list(st)
for i in x[0::2]:
    print(i)
