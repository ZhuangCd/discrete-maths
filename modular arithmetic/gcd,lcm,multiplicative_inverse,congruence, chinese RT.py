import math
from functools import reduce

# REMEBER TO PIPINSTALL THE ABOVE PACKAGES #

from sympy.ntheory.modular import crt, solve_congruence

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
    
    # Extended Euclidean Algorithm to find gcd and the inverses
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0  # GCD(a, b) = a, and the coefficients are 1 and 0
    else:
        g, x1, y1 = extended_gcd(b, a % b)  # Recursively call for b and a mod b
        x = y1
        y = x1 - (a // b) * y1  # Update the coefficients
        return g, x, y



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

# For example find the multiplicative inverse of modulo 12

def find_multiplicative_inverses(modulo):
    # Find numbers with multiplicative inverses modulo `modulo`
    numbers_with_inverse = []
    for a in range(1, modulo):  # 0 is not considered for inverse
        if math.gcd(a, modulo) == 1:
            numbers_with_inverse.append(a)
    return numbers_with_inverse


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

print("Mul inv is", mul_inv(5,17))

# Modified: Chinese Remainder Theorem to handle non-coprime moduli
def chinese_remainder_theorem(a, m):
    """
    Solves a system of congruences using a generalized CRT that supports non-coprime moduli.

    Args:
    a (list): List of remainders a_1, a_2, ..., a_n.
    m (list): List of moduli m_1, m_2, ..., m_n.

    Returns:
    int: The smallest non-negative solution to the system.
    """
    # Ensure the lists a and m are of the same length
    assert len(a) == len(m), "Remainders and moduli lists must be of the same length."

    # Start with the first congruence
    x = a[0]
    mod = m[0]
    
    for i in range(1, len(a)):
        ai = a[i]
        mi = m[i]

        # Solve the congruence x ≡ a[i] (mod m[i])
        gcd, inverse, _ = extended_gcd(mod, mi)

        # Check if the system is consistent
        if (ai - x) % gcd != 0:
            raise ValueError(f"The system of congruences is inconsistent at moduli {mod} and {mi}.")

        # Adjust moduli and remainders for the solution
        lcm = (mod // gcd) * mi  # Least common multiple of mod and mi
        x = (x + (ai - x) // gcd * inverse * (mod // gcd)) % lcm  # Update x modulo lcm
        mod = lcm  # Update mod to the lcm of the previous and current moduli

    # Return the smallest non-negative solution
    return x % mod

# Example usage of Chinese Remainder Theorem:
a = [1,2,3]  # Remainders
m = [2,4,6]  # Moduli
#result = chinese_remainder_theorem(a, m)

#print(f"The solution to the CRT system is: {result}")


def is_congruent(a, b, n):
    """
    Checks if a ≡ b (mod n).
    """
    return a % n == b % n

# Check 35 ≡ 1 (mod 17)

print("Is congurent:", is_congruent(21, 56**2, 5)) #If we divide 35 by 17, the remainder will be 1.

# Solves congurences when they are not relative primes
def solve_modular_system(congruences):
   
    solution = solve_congruence(*congruences)
    if solution:
        x, modulus = solution
        return f"x ≡ {x} (mod {modulus})"
    else:
        return "No solution exists"

# Example usage
congruences = [(3, 4), (1, 6)]
result = solve_modular_system(congruences)
#print(result)











#print("lcm is",lcm(12,49))
print(f"gcd is {gcd(6,3)}")
#print(multiplicative_inverse(5, 7), "And everything result + mod")
#print(congruence_system(1, 43, 23))

 
#modulo = 12
#print(find_multiplicative_inverses(modulo), f"And plus {modulo} to each result also")
