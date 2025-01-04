# Define the sets
A = {1, 2, 3}
B = {3, 4, 5}

# Union u
union_set = A | B
print(f"Union of A and B: {union_set}")

# Intersection n
intersection_set = A & B
print(f"Intersection of A and B: {intersection_set}")

# Difference (A - B)
difference_set = A - B
print(f"Difference of A and B (A - B): {difference_set}")

# Symmetric Difference
symmetric_difference_set = A ^ B
print(f"Symmetric Difference of A and B: {symmetric_difference_set}")

# Subset
is_subset = A <= B
print(f"A is a subset of B: {is_subset}")

# Superset
is_superset = A >= B
print(f"A is a superset of B: {is_superset}")

# Proper Subset
is_proper_subset = A < B
print(f"A is a proper subset of B: {is_proper_subset}")

# Proper Superset
is_proper_superset = A > B
print(f"A is a proper superset of B: {is_proper_superset}")
