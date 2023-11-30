# Take the following as input.
# A number (N1)
# A number (N2)
#/// Write a function which returns the GCD of N1 and N2. Print the value returned.///

# Explanation
# ///The largest number that divides both N1 and N2 is called the GCD of N1 and N2.///


def gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1
N1 = int(input("Enter 1st number: "))
N2 = int(input("Enter 2nd number: "))
result = gcd(N1, N2)
print(result)





