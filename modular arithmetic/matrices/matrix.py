import numpy as np


# Implementing the Boolean product function
def boolean_product(A, B):
    """
    Calculate the Boolean product of two matrices A and B.
    Args:
        A (list of list): First matrix (binary).
        B (list of list): Second matrix (binary).
    Returns:
        list of list: Resultant matrix after Boolean product.
    """
    # Ensure A and B are compatible for multiplication
    assert len(A[0]) == len(B), "Matrices A and B are not compatible for multiplication"
    
    # Initialize the result matrix
    n = len(A)
    m = len(B[0])
    result = [[0] * m for _ in range(n)]
    
    # Compute the Boolean product
    for i in range(n):
        for j in range(m):
            result[i][j] = 0
            for k in range(len(B)):
                result[i][j] |= (A[i][k] and B[k][j])
    return result

# Input matrices
A = [
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
]
B = [
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
]

# Compute the Boolean product
C = boolean_product(A, B)

print("Boolean Product of A and B:")
for row in C:
    print(row)
    

def transpose(matrix):
    """
    Transpose a given matrix.
    Args:
        matrix (list of list): The input matrix.
    Returns:
        list of list: Transposed matrix.
    """
    # Using list comprehension to transpose
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Input matrix
A = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]

# Compute the transpose
A_transpose = transpose(A)

# Print the result in matrix form
print("Transpose of A:")
for row in A_transpose:
    print(row)
