import math

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

def chinese_remainder_theorem(a, m):
    
    
    """Solves the system of congruences using the Chinese Remainder Theorem.
    
    Args:
    a (list): List of remainders a_1, a_2, ..., a_n.
    m (list): List of moduli m_1, m_2, ..., m_n.
    
    Returns:
    int: The smallest non-negative solution to the system.
    """
    # Ensure the lists a and m are of the same length
    assert len(a) == len(m), "Remainders and moduli lists must be of the same length."
    
    # Initial values
    total = 0
    prod = 1
    for mi in m:
        prod *= mi
    
    # Iterate through each congruence
    for ai, mi in zip(a, m):
        # Compute the partial product of all moduli except the current one
        p = prod // mi
        
        # Use the extended Euclidean algorithm to find the inverse of p modulo mi
        gcd, inverse, _ = extended_gcd(p, mi)
        
        # Ensure that p and mi are coprime (gcd should be 1)
        if gcd != 1:
            raise ValueError(f"Moduli {mi} and {p} are not coprime, cannot apply CRT.")
        
        # Add the contribution of this congruence to the solution
        total += ai * inverse * p
    
    # The solution is total modulo the product of all moduli
    return total % prod

# Example usage of chinese reminder theorem :
a = [1,1,1,1]  # Remainders
m = [20, 44]  # Moduli
result = chinese_remainder_theorem(a, m)
print(f"The solution to the system is: {result}")


#print("lcm is",lcm(50,15))
#print(f"gcd is {gcd(15,50)}")
#print(multiplicative_inverse(9,10))
#check_if_inverse(9,23,10)
#congruence_system(89, 2, 232)