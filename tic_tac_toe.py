import random
import time


def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    return [[' . ', ' . ', ' . '], [' . ', ' . ', ' . '], [' . ', ' . ', ' . ']]


def get_move(board, player):
    row, col = 0, 0

    board_filed = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3']]
    flat_board_filed = board_filed[0] + board_filed[1] + board_filed[2]
    flat_board = board[0] + board[1] + board[2]

    x = 0
    y = 0
    found = False
    
    while not found:
        while x == 0 or y == 0:
            pos = []
            text_position = input(f"Please provide a {change_player_mark(player)} position on the board: ").upper()
            while len(text_position) != 2:
                text_position = input(f"Please provide a {change_player_mark(player)} position on the board: ").upper()
            row = text_position[0]
            col = text_position[1]
           
            if row == "A" or row == "B" or row == "C":
                x = 1
                pos.insert(0, row)
            else:
                x = 0
    
            if col == "1" or col == "2" or col == "3":
                y = 1
                pos.insert(1, col)
            else:
                y = 0    

        row = pos[0]
        col = pos[1]

        if row == "A":
            row = 0
        elif row == "B":
            row = 1
        elif row == "C":
            row = 2
                 
        if col == "1":
            col = 0 
        elif col == "2":
            col = 1
        elif col == "3":
            col = 2    
        
        position = ''.join(pos)
        index = flat_board_filed.index(position)
            
        if flat_board[index] == ' . ':
            found = True
        else:
            print("You have already selected this item.")
            x = 0
            y = 0
            pos = []

    return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    if is_full(board):
        return None
    moves = []
    for row in range(len(board)):
        for cell in range(len(board[row])):
            if board[row][cell] == " . ":
                moves.append((row, cell))
    return random.choice(moves)


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    players = [' O ', ' X ']
    board[row][col] = players[player]


def has_won(board, player):
    """Returns True if player has won the game."""
    player_won = change_player_mark(player)

    if board[0][0] == board[0][1] == board[0][2] == player_won:
        return True
    if board[1][0] == board[1][1] == board[1][2] == player_won:
        return True
    if board[2][0] == board[2][1] == board[2][2] == player_won:
        return True        
    if board[0][0] == board[1][0] == board[2][0] == player_won:
        return True
    if board[0][1] == board[1][1] == board[2][1] == player_won:
        return True
    if board[0][2] == board[1][2] == board[2][2] == player_won:
        return True
    if board[0][0] == board[1][1] == board[2][2] == player_won:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player_won:
        return True
    return False


def is_full(board):
    """Returns True if board is full."""
    for row in board:
        if " . " in row:
            return False
    return True


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    print('   1   2   3')
    letters = ["A", "B", "C"]
    for row in range(len(letters)):
        print(letters[row] + " ", end="")
        for col in range(len(letters)):
            print(board[row][col], end="")
            if col < 2:
                print("|", end="")
        print()
        if row < 2:
            print('  ---+---+---')
    print()


def print_result(board, winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    print_board(board)
    if winner == "DRAW":
        print("DRAW")
    else:
        print(f"WINNER PLAYER: {change_player_mark(winner)}")
    time.sleep(1)


def change_player_mark(player):
    if player == 1:
        return " X "
    else:
        return " O "


def player_move(board, player, move_function):
    """Player move."""
    print_board(board)
    row, col = move_function(board, player)
    mark(board, player, row, col)
    if has_won(board, player):
        return player
    elif is_full(board):
        return "DRAW"
    else:
        return None


def main_game_mode(board, method_for_O, method_for_X):
    """Main game loop."""
    while True:
        winner = player_move(board, 0, method_for_O)
        if winner is not None:
            break
        winner = player_move(board, 1, method_for_X)
        if winner is not None:
            break
    print_result(board, winner)


def human_human_mode():
    """Game mode for player vs player."""
    board = init_board()
    main_game_mode(board, get_move, get_move)


def ai_human_mode():
    """Game mode for computer vs player."""
    board = init_board()
    main_game_mode(board, get_smart_ai_move, get_move)


def human_ai_mode():
    """Game mode for player vs computer."""
    board = init_board()
    main_game_mode(board, get_move, get_smart_ai_move)


def ai_ai_mode():
    """Game mode for computer vs computer."""
    board = init_board()
    main_game_mode(board, get_smart_ai_move, get_smart_ai_move)


def tictactoe_game(mode='HUMAN-HUMAN'):
    """Choose game mode and run it."""
    if mode == "HUMAN-HUMAN":
        human_human_mode()
    if mode == "AI-HUMAN":
        ai_human_mode()
    if mode == "HUMAN-AI":
        human_ai_mode()
    if mode == "AI-AI":
        ai_ai_mode()


def get_menu_option():
    """Choose game option."""
    while True:
        game_option = input("""
    1. HUMAN-HUMAN
    2. AI-HUMAN
    3. HUMAN-AI
    4. AI-AI
    5. EXIT
    """)
        if game_option in ("1", "2", "3", "4", "5"):
            return game_option
        else:
            print("WRONG OPTION")
            time.sleep(1)


def main_menu():
    """Game main menu."""
    while True:
        game_option = get_menu_option()
        if game_option == "1":
            tictactoe_game('HUMAN-HUMAN')
        elif game_option == "2":
            tictactoe_game('AI-HUMAN')
        elif game_option == "3":
            tictactoe_game('HUMAN-AI')
        elif game_option == "4":
            tictactoe_game('AI-AI')
        elif game_option == "5":
            print("GOOD BYE")
            break


def check_horizontal(board, player):
    """Check if player can win horizontally."""
    for x in range(3):
        if board[x][0] == player and board[x][1] == player and board[x][2] == " . ":
            return x, 2

    for x in range(3):
        if board[x][0] == player and board[x][1] == " . " and board[x][2] == player:
            return x, 1

    for x in range(3):
        if board[x][0] == " . " and board[x][1] == player and board[x][2] == player:
            return x, 0

    return False


def check_vertical(board, player):
    """Check if player can win vertically."""
    for x in range(3):
        if board[0][x] == player and board[1][x] == player and board[2][x] == " . ":
            return 2, x

    for x in range(3):
        if board[0][x] == player and board[1][x] == " . " and board[2][x] == player:
            return 1, x

    for x in range(3):
        if board[0][x] == " . " and board[1][x] == player and board[2][x] == player:
            return 0, x

    return False


def check_diagonal(board, player): #j
    """Check if player can win diagonally."""
    if board[0][0] == player and board[1][1] == player and board[2][2] == " . ":
        return 2, 2
    elif board[0][0] == player and board[1][1] == " . " and board[2][2] == player:
        return 1, 1
    elif board[0][0] == " . " and board[1][1] == player and board[2][2] == player:
        return 0, 0

    elif board[0][2] == player and board[1][1] == player and board[2][0] == " . ":
        return 2, 0
    elif board[0][2] == player and board[1][1] == " . " and board[2][0] == player:
        return 1, 1
    elif board[0][2] == " . " and board[1][1] == player and board[2][0] == player:
        return 0, 2

    return False


def smart_ai_move(board, player):
    """Check if player can win."""
    player = change_player_mark(player)
    check_move = check_horizontal(board, player)
    if not check_move:
        check_move = check_vertical(board, player)
    if not check_move:
        check_move = check_diagonal(board, player)
    if check_move:
        return check_move
    else:
        return False


def get_opposite_player(player):
    """Change player."""
    if player == 1:
        return 0
    return 1


def get_smart_ai_move(board, player):
    """Check if player can win. If not check if enemy can win and block him.
    Else do random move."""
    move = smart_ai_move(board, player)

    if not move:
        my_player = get_opposite_player(player)
        move = smart_ai_move(board, my_player)

    if not move:
        move = get_ai_move(board, player)

    return move


if __name__ == '__main__':
    main_menu()
