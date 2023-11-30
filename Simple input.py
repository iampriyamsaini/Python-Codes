# Given a list of numbers, stop processing input after the cumulative sum of all the input becomes negative.

a=0
while(True):
    n=int(input(''))
    a+=n
    if(a>=0):
        print(n)
    else:
        break
