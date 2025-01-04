from itertools import product

def generate_membership_table(variables, operations):
    """
    Generate a membership table for given sets and operations.

    :param variables: List of variable names, e.g., ['A', 'B', 'C']
    :param operations: Dictionary of operations to evaluate.
    :return: None
    """
    # Generate all combinations of membership values (True/False)
    rows = list(product([True, False], repeat=len(variables)))
    
    # Print the header
    header = variables + list(operations.keys())
    print("\t".join(header))
    print("=" * (len(header) * 8))
    
    # Evaluate each row
    for row in rows:
        membership_values = list(row)
        results = [operation(*membership_values) for operation in operations.values()]
        print("\t".join(str(val) for val in membership_values + results))

# Variables (sets)
variables = ['A', 'B', 'C']

# Define various set operations
operations = {
    "A and not(B or C)": lambda A, B, C: A and (B or C),
    "A and not B) or (A and not C)": lambda A, B, C: (A and B) or (A and C), 
}
"""
    "A union B": lambda A, B, C: A or B, # A u B
    A intersection B": lambda A, B, C: A and B, # A n B
    "A difference B": lambda A, B, C: A and not B, # A-B
    "complement of A: lambda A, B, C: A and not A 
    "A symmetric difference B": lambda A, B, C: A != B, 
    "A is a subset of B": lambda A, B, C: not A or B,
    "A is a superset of B": lambda A, B, C: not B or A,
    "A is equal to B": lambda A, B, C: A == B,
    "A is not equal to B": lambda A, B, C: A != B,
    "A is a proper subset of B": lambda A, B, C: not A or (B and not A),
    "A is a proper superset of B": lambda A, B, C: not B or (A and not B)"""
# Generate and display the membership table
generate_membership_table(variables, operations)

