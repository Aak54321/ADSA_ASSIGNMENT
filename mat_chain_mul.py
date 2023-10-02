import sys

def matrix_chain_multiplication(matrices):
    n = len(matrices)
    
    # Initialize the tables
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]
    
    # Fill the m table
    for length in range(2, n):
        for i in range(n - length + 1):
            j = i + length - 1
            m[i][j] = sys.maxsize  # Initialize to infinity
            
            for k in range(i, j):
                cost = m[i][k] + m[k+1][j] + matrices[i][0] * matrices[k][1] * matrices[j][1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k  # Update partition point

    return m, s

def print_optimal_parenthesization(s, i, j):
    if i == j:
        print(f"Matrix {i}", end='')
    else:
        print("(", end='')
        print_optimal_parenthesization(s, i, s[i][j])
        print_optimal_parenthesization(s, s[i][j] + 1, j)
        print(")", end='')

# Input: List of matrices with dimensions (rows, columns)
def get_matrix_dimensions():
    matrices = []
    num_matrices = int(input("Enter the number of matrices: "))
    for i in range(num_matrices):
        rows, cols = map(int, input(f"Enter dimensions for matrix {i+1} (rows columns): ").split())
        matrices.append((rows, cols))
    return matrices

# Get matrix dimensions from the user
matrices = get_matrix_dimensions()

# Solve the matrix chain multiplication problem
m, s = matrix_chain_multiplication(matrices)

# Print the optimal parenthesization
print("Optimal Parenthesization:", end=' ')
print_optimal_parenthesization(s, 0, len(matrices) - 1)
print()

# Print the minimum number of scalar multiplications
print("Minimum Scalar Multiplications:", m[0][len(matrices) - 1])


print("""
### Matrix Multiplication:

**Time Complexity:**
- Naive Matrix Multiplication: O(n^3) (for n x n matrices)
- Strassen's Algorithm: O(n^2.81) (asymptotically faster than naive)

**Space Complexity:**
- Naive Matrix Multiplication: O(1) auxiliary space
- Strassen's Algorithm: O(n) auxiliary space (due to recursion)

**Preferred Scenarios:**
- Naive Matrix Multiplication:
  - Simple to implement and understand.
  - Practical for small matrix sizes.
- Strassen's Algorithm:
  - More efficient for very large matrices (asymptotically faster than naive).
  - Trade-off between time and space complexity.
  - Practical for extremely large matrices in specific applications.

### Matrix Chain Multiplication (Dynamic Programming):

**Time Complexity:**
- Time Complexity: O(n^2) (where n is the number of matrices)

**Space Complexity:**
- Space Complexity: O(n^2)

**Preferred Scenarios:**
- Efficiently finds optimal parenthesization for matrix chain multiplication.
- Suitable for any size of matrix chain.
- Practical for problems where minimizing scalar multiplications is critical.

""")
