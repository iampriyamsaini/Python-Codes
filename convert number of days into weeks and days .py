#convert number of days into weeks and days 
days=int(input("enter the number of days: "))
weeks=days//7
days=days%7
print("total number of weeks =", weeks)
print("total number of days =", days)