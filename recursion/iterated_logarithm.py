import math

def log_star(n):
    # Base case: if n is already <= 1
    if n <= 1:
        return 0
    # Recursive case: apply log and increment the count
    else:
        return 1 + log_star(math.log2(n))

# Set your value for n here
n = 2**2048

result = log_star(n)

print(f"log*({n}) = {result}")
