n = int(input("Enter a number:" ))
original = n 
reverse = 0
while (n>0):
  lastdigit=n%10
  reverse = reverse*10+lastdigit
  n = n//10
print("reverse number = ",reverse)
print("original number = ",original)
if (reverse>original):
  print("reverse is greater than original number.")
else:
  print("original is greater than reverse number.")
