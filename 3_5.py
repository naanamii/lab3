def get_rank(matrix):
    if not matrix:
        return 0, 0
    n, m = len(matrix), len(matrix[0])

    rank = m
    row_idx = 0
    used = [False] * n

    for col_idx in range(m):
        pivot_found = False
        for row_idx in range(n):
            if used[row_idx]:
                continue
            if matrix[row_idx][col_idx] != 0:
                pivot_found = True
                break

        if pivot_found:
            used[row_idx] = True
            rank -= 1
            for i in range(n):
                if not used[i] and matrix[i][col_idx] != 0:
                    coef = matrix[i][col_idx] / matrix[row_idx][col_idx]
                    for j in range(m):
                        matrix[i][j] -= coef * matrix[row_idx][j]
    return rank

def check_linear_independence(matrix):
    num_cols = len(matrix[0])
    rank = get_rank(matrix)

    if rank == num_cols:
        return "Matrix columns are linearly independent."
    else:
        return "The columns of the matrix are linearly dependent."
mat = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 80]
]

print(check_linear_independence(mat))
print(mat)
