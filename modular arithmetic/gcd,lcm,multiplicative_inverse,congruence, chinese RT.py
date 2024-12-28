import math
from functools import reduce

# REMEBER TO PIPINSTALL THE ABOVE PACKAGES #

def lcm(x, y):
    # Calculate the LCM using the formula LCM(x, y) = abs(x * y) // GCD(x, y)
    return abs(x * y) // math.gcd(x, y)

# calculate gcd
def gcd(y, n):
    # Ensure that y >= n
    if y >= n:
        while n != 0:
            # y % n give the reminder
            y, n = n, y % n
        return y
    # works no matter the order of the numbers in the gcd
    else:
        while y != 0:
            n,y = y, n % y
        return n


# calculate the first inverse:
# y mod n
def multiplicative_inverse(y,n):
    if gcd(y,n) == 1:
        for i in range(n):
            if (y*i)%n == 1:
                print(f"The inverse of {y} mod {n} is {i}")
                return i
    else:
        print("has no inverse")
        return False 
# check if they are congurent
# We say that a ≡ b (mod m) is a congruence

def is_congurent(a,b,m):
    if (a-b)%m == 0:
        print(f"{a} ≡ {b} mod {m} is a congruence")
    else:
        print(f"{a} ≡ {b} mod {m} is NOT a congruence")

# check if the number is an inverse
# Form y * x = 1 mod n 
def check_if_inverse(y,x,n):
    # has an inverse if gcd = 1
    if gcd(y,n) == 1:
            if (y*x)%n == 1:
                print(f"{x} is an inverse to {y} mod {n}")
                return x
            else:
                print(f"{x} is NOT an inverse to {y} mod {n}")
                return False
    else:
        print(f"{y} mod {n} has no inverse")
        return False

# Solve congruence system on the form yx ≡ b (mod n)
def congruence_system(y, b, n):
    multi_in = multiplicative_inverse(y, n)
    if multi_in is not False:
        # Calculate x and take modulo n
        x = (multi_in * b) % n
        print(f"The solution to {y}x ≡ {b} (mod {n}) is x ≡ {x} (mod {n})")
        return x
    else:
        print("No solution exists")
        return None



def chinese_remainder(m, a):
    sum = 0
    prod = reduce(lambda acc, b: acc*b, m)
    for n_i, a_i in zip(m, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 
 
 
if __name__ == '__main__':
    # x = a mod m 
    m= [2,3,5]
    a = [1,0,3]
    print(chinese_remainder(m, a))


#print("lcm is",lcm(9,6))
#print(f"gcd is {gcd(15,28)}")
#print(multiplicative_inverse(5,17))
#check_if_inverse(9,23,10)
#congruence_system(89, 2, 232)#
#is_congurent(27,70,7)

