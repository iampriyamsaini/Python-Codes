# Due to an immense rise in Pollution, Kejriwal is back with the Odd and Even Rule in Delhi. The scheme is as follows, each car will be allowed to run on Sunday 
#if the sum of digits which are even is divisible by 4 or sum of digits which are odd in that number is divisible by 3. 
#However to check every car for the above criteria can't be done by the Delhi Police. You need to help Delhi Police by finding out if a car numbered N will be allowed to run on Sunday?

# Explanation
# 1 + 3 + 5 = 9 which is divisible by 3
# 1 + 1 + 3 = 5 which is NOT divisible by 3 and 2+4 = 6 which is not divisble by 4.


a=int(input(''))
i=0
while(i<a):
    b=input('')
    i=i+1
    out=0
    add=0
    for y in b:
        j=int(y)
        if(j%2!=0):
            add=add+j
        else:
            out=out+j
    if (out%4==0 or add%3==0):
        print("Yes")
    else:
        print("No")
