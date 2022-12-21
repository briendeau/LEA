board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def display_board(board):
    for row in board:
        print('|'.join(row))

def handle_turn(player):
    print(f"{player}'s turn")
    row = int(input("Enter a row (0, 1, 2): "))
    col = int(input("Enter a column (0, 1, 2): "))
    if board[row][col] != ' ':
        print("That space is already occupied! Please try again.")
        handle_turn(player)
    else:
        board[row][col] = player

def check_game_over():
    # check rows
    for row in board:
        if row[0] != ' ' and row[0] == row[1] == row[2]:
            return True, row[0]
    # check columns
    for col in range(3):
        if board[0][col] != ' ' and board[0][col] == board[1][col] == board[2][col]:
            return True, board[0][col]
    # check diagonals
    if board[0][0] != ' ' and board[0][0] == board[1][1] == board[2][2]:
        return True, board[0][0]
    if board[0][2] != ' ' and board[0][2] == board[1][1] == board[2][0]:
        return True, board[0][2]
    # check for draw
    for row in board:
        if ' ' in row:
            return False, None
    return True, None

def tic_tac_toe():
    current_player = 'X'
    game_over = False
    winner = None
    while not game_over:
        display_board(board)
        handle_turn(current_player)
        game_over, winner = check_game_over()
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
    display_board(board)
    if winner:
        print(f"{winner} won")

tic_tac_toe()