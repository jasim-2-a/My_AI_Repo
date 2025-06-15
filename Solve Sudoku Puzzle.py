def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, pos):
    row, col = pos

    if any(board[row][i] == num for i in range(9)):
        return False
    if any(board[i][col] == num for i in range(9)):
        return False

    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num:
                return False
    return True

def solve(board):
    empty = find_empty(board)
    if not empty:
        return True

    row, col = empty
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0
    return False

def get_user_board():
    print("Enter your Sudoku board row by row.")
    print("Use space-separated numbers and use 0 for empty cells.")
    board = []
    for i in range(9):
        while True:
            try:
                row = input(f"Row {i+1}: ").strip().split()
                if len(row) != 9 or not all(n.isdigit() and 0 <= int(n) <= 9 for n in row):
                    raise ValueError
                board.append([int(n) for n in row])
                break
            except ValueError:
                print("Invalid input. Enter 9 numbers between 0–9 separated by spaces.")
    return board

if __name__ == "__main__":
    user_board = get_user_board()

    print("\nOriginal Board:")
    print_board(user_board)

    if solve(user_board):
        print("\nSolved Board:")
        print_board(user_board)
    else:
        print("\nNo solution exists.")
