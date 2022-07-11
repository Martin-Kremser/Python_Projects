def display_board(board):
    board = [
        ['.', ".", "."],
        ['.', ".", "."],
        ['.', ".", "."]
    ]

    line = "   ---+---+---"

    print("\n    1   2   3\n")
    print(f"A   {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(line)
    print(f"B   {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(line)
    print(f"C   {board[2][0]} | {board[2][1]} | {board[2][2]}")
    print(line, "\n")


def get_menu_option():
    game_mode = input(
        "Choose your Game Mode\n1. Human vs Human\n2. Random AI vs Random AI\n3. Human vs Random AI\n4. "
        "Human vs Unbeatable AI\nYour choice is: ")
    if game_mode == 1:
        print("Your choice: Human vs Human")
        return 1
    elif game_mode == 2:
        print("Your choice: Random AI vs Random AI")
        return 2
    elif game_mode == 3:
        print("Human vs Random AI")
        return 3
    elif game_mode == 4:
        print("Human vs Unbeatable AI")
        return 4


def is_board_full(board):
    pass


run = True


def game_move():
    global run
    while True:
        player_move = input("Enter your field: ").upper()
        if player_move == "QUIT" or player_move == "Q":
            run = False
            return
        player_move = int(player_move)
        if 1 <= player_move <= 9:
            if display_board("X") or display_board("O"):
                print("This field is already occupied. Please choose a free field.")
            else:
                return player_move
        else:
            print("Invalid Entry, please try again!")


def draw_check():
    if display_board([0][0]) != "." and display_board([0][1]) != "." and display_board([0][2]) != "." \
            and display_board([1][0]) != "." and display_board([1][1]) != "." and display_board([1][2]) != "." \
            and display_board([2][0]) != "." and display_board([2][1]) != "." and display_board([2][2]) != ".":
        return True


def get_winning_player(board):
    for row in board:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != ["."]:
            print(f"Player {row[0]} is the Winner!")
    for col in range(len(board)):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"Player {check[0]} is the Winner!")
    diags = []
    for col, row in enumerate(reversed(range(len(board)))):
        print(col, row)
        diags.append(board[row][col])
    if diags.count(row[0]) == len(row) and row[0] != ["."]:
        print(f"Player {diags[0]} is the Winner!")
    diags = []
    for index in range(len(board)):
        diags.append(board[index][index])
    if diags.count(row[0]) == len(row) and row[0] != ["."]:
        print(f"Player {diags[0]} is the Winner!")


def compMove():
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    ai_input(bot, bestMove)
    return


def minimax(board, depth, isMaximizing):
    if get_winning_player(bot):
        return 1
    elif get_winning_player(player):
        return -1
    elif draw_check():
        return 0

    if isMaximizing:
        bestScore = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


"""def win_check():
    # Check Zeilen
    if display_board([0][0]) == display_board([0][1]) == display_board([0][2]):
        return display_board([0][0])
    if display_board([1][0]) == display_board([1][1]) == display_board([1][2]):
        return display_board([1][0])
    if display_board([2][0]) == display_board([2][1]) == display_board([2][2]):
        return display_board([2][0])
    # Check Spalten
    if display_board([0][0]) == display_board([1][0]) == display_board([2][0]):
        return display_board([0][0])
    if display_board([0][1]) == display_board([1][1]) == display_board([2][1]):
        return display_board([0][1])
    if display_board([0][2]) == display_board([1][2]) == display_board([2][2]):
        return display_board([0][2])
    # Check Diagonal
    if display_board([0][0]) == display_board([1][1]) == display_board([2][2]):
        return display_board([0][0])
    if display_board([0][2]) == display_board([1][1]) == display_board([2][0]):
        return display_board([0][2])"""
