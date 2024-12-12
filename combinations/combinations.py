from math import factorial

# Function for permutations (order matters) arrange r object from n objects
def permutation(n, r):
    return factorial(n) // factorial(n - r)

# Function for combinations (order doesn't matter)
def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

print("P(n,r) Permutation:", permutation(6, 3))  
print("C(n,r) Combination:", combination(37, 17))  
