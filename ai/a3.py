N = 3


def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve(board, col):
    if col >= N:
        return True

    for i in range(N):
        print(f"Checking row {i}, col{col}")
        if is_safe(board, i, col):
            print(f"Placing queen at ({i},{col})")
            board[i][col] = 1

            if solve(board, col + 1):
                return True

            print(f"Backtracking from ({i},{col})")
            board[i][col] = 0

    return False


board = [[0] * N for _ in range(N)]
if solve(board, 0):
    print("\nFinal board\n")
    for row in board:
        print(row)
else:
    print("NOT SOLVABLE")
