ROWS = 6
COLS = 7


def create_board(rows, cols):
    # TODO (Name): return a 6x7 grid of empty spaces
     board = []
     for row in range(rows):
         board.append([])
         for col in range(cols):
          board[row].append(0)
     return board

def drop_piece(board, col, piece):
    # TODO (Name): put piece in the lowest empty row of col
    pass

def is_valid_move(board, col):
    # TODO (Name): return True if col isn't full
    pass

def check_win(board, piece):
    # TODO (Name): return True if piece has 4 in a row
    pass

def print_board(board):
    # TODO (Name): show the board in the terminal
    for row in board:
        print(row)


new_board = create_board(ROWS, COLS)
print_board(new_board)