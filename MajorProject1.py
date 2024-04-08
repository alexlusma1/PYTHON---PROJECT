Your task is create a Connect 4 game in Python. Once you've got the rules down, your assignment should be fairly straightforward. 
You'll want to draw the board, and allow two players to take turns placing their pieces on the board 
(but as you learned above, they can only do so by choosing a column, not a row). The first player to get 4 across or diagonal should win!
Normally the pieces would be red and black.


ROW_COUNT = 6
COLUMN_COUNT = 7
EMPTY = 0
PLAYER_1_PIECE = 1
PLAYER_2_PIECE = 2

def create_board():
    board = []
    for _ in range(ROW_COUNT):
        row = [EMPTY] * COLUMN_COUNT
        board.append(row)
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == EMPTY

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == EMPTY:
            return r

def winning_move(board, piece):
    # Check horizontal locations
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    # Check vertical locations
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True

def print_board(board):
    for row in board:
        print(row)

def main():
    board = create_board()
    game_over = False
    turn = 0

    while not game_over:
        # Player 1 input
        if turn == 0:
            col = int(input("Player 1 make your selection (0-6):"))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, PLAYER_1_PIECE)

                if winning_move(board, PLAYER_1_PIECE):
                    print("Player 1 wins!")
                    game_over = True
            else:
                print("Invalid move. Please try again.")
                continue

        # Player 2 input
        else:
            col = int(input("Player 2 make your selection (0-6):"))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, PLAYER_2_PIECE)

                if winning_move(board, PLAYER_2_PIECE):
                    print("Player 2 wins!")
                    game_over = True
            else:
                print("Invalid move. Please try again.")
                continue

        print_board(board)
        turn += 1
        turn %= 2

if __name__ == "__main__":
    main()
