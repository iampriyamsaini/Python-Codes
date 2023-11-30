#sum of all numbers upto n that are divisible by both 2 & 3
num = int(input("Enter a number: "))
sum_ = 0 
for i in range(0,num+1):
    if (i%2==0 and i%3==0):
        sum_+=i
print(sum_)
