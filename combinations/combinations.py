from math import factorial

# Function for permutations
def permutation(n, r):
    return factorial(n) // factorial(n - r)

# Function for combinations
def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

print("P(n,r) Permutation:", permutation(6, 3))  
print("C(n,r) Combination:", combination(37, 17))  
