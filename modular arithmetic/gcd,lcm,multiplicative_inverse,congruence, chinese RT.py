import math
from sympy.ntheory.modular import crt


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


# calculate the inverse:
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

# Test the function


# for the chinese reminder theorem 
def extended_gcd(a, b):
    """Extended Euclidean Algorithm to find gcd and the coefficients (x, y) of Bézout's identity."""
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y


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
a = [1,1,1,1]  # Remainders
m = [2,3,4,5]  # Moduli
result = chinese_remainder_theorem(a, m)
print(f"The solution to the CRT system is: {result}")


def is_congruent(a, b, n):
    """
    Checks if a ≡ b (mod n).
    """
    return a % n == b % n

# Check 35 ≡ 1 (mod 17)

print("Is congurent:", is_congruent(35, 1, 17)) #If we divide 35 by 17, the remainder will be 1.













#print("lcm is",lcm(15,24))
#print(f"gcd is {gcd(15,28)}")
#print(multiplicative_inverse(5, 7), "And everything result + mod")
#print(congruence_system(1, 43, 23))

 
#modulo = 12
#print(find_multiplicative_inverses(modulo), f"And plus {modulo} to each result also")
