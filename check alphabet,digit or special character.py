inp = input("Enter anything : ")
if inp >= "a" and inp <= "z" or inp >= "A" and inp <= "Z":
   print("input is alphabet")
elif inp>="0":
   print("input is number")
else:
   print("special character")