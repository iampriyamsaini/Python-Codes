h = 10
r = 5
f = 15
t = eval(input("Enter the time: "))
vwtr = f*t
vtank = 3.14*r**2*h 
if (vwtr == vtank):
    print("Tank full.")
elif(vtank>vwtr):
    print("Underflow Condition.")
    ht = vwtr/(3.14*r**2)
    hr = h-ht
    print("Filled height",ht)
    print("Remaning height",hr)
else:
    print("Overflow Condition")
    print("Volume",vwtr-vtank)
