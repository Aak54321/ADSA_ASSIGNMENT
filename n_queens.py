def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens_util(board, row, n, results):
    if row == n:
        results.append([''.join(row) for row in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            solve_n_queens_util(board, row + 1, n, results)
            board[row][col] = '.'

def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    results = []
    solve_n_queens_util(board, 0, n, results)
    return results

def print_solutions(results):
    for i, solution in enumerate(results, start=1):
        print(f"Solution {i}:")
        for row in solution:
            print(' '.join(row))
        print()

# Example usage for N = 4 and N = 8
N_values = [4, 8]

for N in N_values:
    print(f"Solutions for N = {N}:")
    solutions = solve_n_queens(N)
    print_solutions(solutions)


print("""
### N-Queens Backtracking Algorithm:

**Time Complexity:**
- The time complexity of the backtracking algorithm to solve the N-Queens problem is \(O(N!)\), where \(N\) is the size of the chessboard and the number of queens to be placed.
- In the worst-case scenario, the algorithm needs to explore \(N!\) possible configurations of placing queens on the board.

**Space Complexity:**
- The space complexity is \(O(N^2)\) due to the space required for the chessboard.

### Efficiency for Larger \(N\) Values:

- The time complexity grows rapidly with \(N\) due to the factorial nature of the number of possible configurations (\(N!\)).
- As \(N\) increases, the number of possibilities increases exponentially, making the algorithm less efficient for larger \(N\) values.
- For small to moderate \(N\) values, the algorithm works efficiently and provides solutions quickly. However, for larger \(N\), the time taken grows significantly, making it less practical for very large \(N\) values.

This algorithm is suitable for solving the N-Queens problem for reasonable \(N\) values where \(N!\) computations can be handled within an acceptable time frame. However, it may become impractical for very large \(N\) values due to its exponential time complexity.

""")