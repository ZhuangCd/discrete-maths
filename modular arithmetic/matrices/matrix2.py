import numpy as np

def transpose_matrix(matrix):
    """Return the transpose of the given matrix."""
    return matrix.T

def inverse_matrix(matrix):
    """Return the inverse of the given square matrix."""
    return np.linalg.inv(matrix)

def multiply_matrices(matrix1, matrix2):
    """Return the product of two matrices."""
    return np.dot(matrix1, matrix2)

def power_matrix(matrix, exponent):
    """Return the matrix raised to the specified power."""
    return np.linalg.matrix_power(matrix, exponent)

def boolean_product(matrix1, matrix2):
    """
    Return the Boolean product of two matrices.
    In Boolean algebra, the multiplication is replaced by logical AND,
    and addition is replaced by logical OR.
    """
    product = np.dot(matrix1, matrix2)
    return (product > 0).astype(int)

# Example usage:
if __name__ == "__main__":
    A = np.array([[1, 2,3], 
                  [1, 2,3],
                  [1, 2,3]])
    B = np.array([[5, 6], [7, 8]])

    print("Matrix A:\n", A)
    print("Matrix B:\n", B)

    print("\nTranspose of A:\n", transpose_matrix(A))
    #print("\nInverse of A:\n", inverse_matrix(A))
    print("\nA multiplied by A:\n", multiply_matrices(A, A))
    print("\nA raised to the power of 2:\n", power_matrix(A, 2))
    print("\nBoolean product of A and B:\n", boolean_product(A, B))
