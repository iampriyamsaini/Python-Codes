#reverse a list by without using any inbuilt function
lst=list(map(int, input("Enter the elements of list: ").split()))
print(lst[-1::-1])
