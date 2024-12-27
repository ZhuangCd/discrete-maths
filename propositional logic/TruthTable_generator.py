from itertools import product

def generate_truth_table(variables, expressions):
    """
    Generate a truth table for given variables and logical expressions.

    :param variables: List of variable names, e.g., ['p', 'q', 'r']
    :param expressions: List of lambda functions for logical expressions.
                        Each function should accept the same number of arguments as variables.
    :return: None
    """
    # Generate all combinations of truth values
    rows = list(product([True, False], repeat=len(variables)))
    
    # Print the header
    header = variables + [f"Expr {i+1}" for i in range(len(expressions))]
    print("\t".join(header))
    print("=" * (len(header) * 8))
    
    # Evaluate each row
    for row in rows:
        truth_values = list(row)
        results = [expr(*truth_values) for expr in expressions]
        print("\t".join(str(val) for val in truth_values + results))

# Variables
variables = ['p', 'q', 'r']

# Logical expressions (maximum 2 appearances per variable)
expressions = [
    lambda p, q, r: p and q,                 # AND
    lambda p, q, r: p or q,                  # OR
    lambda p, q, r: not p,                   # NOT
    lambda p, q, r: p != q,                  # XOR
    lambda p, q, r: p == q,                  # BICONDITIONAL
    lambda p, q, r: not (p and q),           # NOT (AND)
    lambda p, q, r: not (p or q),            # NOT (OR)
    lambda p, q, r: not p or q,              # IMPLICATION (p -> q)
    lambda p, q, r: not q or p,              # REVERSE IMPLICATION (q -> p)
    lambda p, q, r: p and not q,             # p AND NOT q
    lambda p, q, r: q and not p,             # q AND NOT p
    lambda p, q, r: (p or r) and (not q),    # Mixed example
]

# Generate and display the truth table
generate_truth_table(variables, expressions)
