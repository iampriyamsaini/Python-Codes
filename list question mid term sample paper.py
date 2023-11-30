# You are given a list of integers. Write a Python program that squares each element of the list and 
# then filters out the even squared numbers. Finally, 
# print the resulting squared and filtered list in a single line.

# Example:

# Sample Input 1
# 1 2 3 4 5
# Sample Output 1
# 1 9 25

# sample Input 2
# 2 4 6 8 10
# Sample Output 2
# None

lst=list(map(int, input("Enter a list: ").split()))
new_lst=[]
for i in (lst):
    if i*i % 2!=0:
        print(i*i,end=' ')
        new_lst.append(i*i)
if len(new_lst)==0:
        print("None")
# else:
#     print(new_lst)





