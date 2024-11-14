def ackermann(m, n):
    # Base case for m = 0
    if m == 0:
        return n + 1
    # Case where m > 0 and n = 0
    elif n == 0:
        return ackermann(m - 1, 1)
    # General recursive case
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

# Set your values for m and n here
m = 2  
n = 3  

# Calculate the result
result = ackermann(m, n)

print(f"Ackermann result for A({m}, {n}): {result}")
