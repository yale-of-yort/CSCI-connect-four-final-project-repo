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
    col_slot = col - 1
    row = ROWS - 1
    piece_codenum = 0
    if piece == 'red':
        piece_codenum = 2
    if piece == 'yellow':
        piece_codenum = 3
    if board[row][col_slot] != 0:
         row -= 1
    board[row][col_slot] = piece_codenum
    return board


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
# print_board(new_board)

updated_board = drop_piece(new_board, 3, 'yellow')
updated_board = drop_piece(new_board, 3, 'red')
updated_board = drop_piece(new_board, 3, 'yellow')
updated_board = drop_piece(new_board, 6, 'yellow')

print_board(updated_board)