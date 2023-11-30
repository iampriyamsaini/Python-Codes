#Greatest in Three numbers by taking three variables in one line
a,b,c=list(map(int, input().split()))
if a>=b and a>=c:
    print(a)
elif  b>=a and b>=c:
    print(b)
else:
    print(c)
