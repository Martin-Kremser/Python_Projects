field = ["",
         "1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

active_player = "X"
run = True


def print_field():
    print(field[1] + "|" + field[2] + "|" + field[3])
    print(field[4] + "|" + field[5] + "|" + field[6])
    print(field[7] + "|" + field[8] + "|" + field[9])


def game_move():
    global run
    while True:
        player_move = input("Enter your field: ").upper()
        if player_move == "QUIT" or player_move == "Q":
            run = False
            return
        player_move = int(player_move)
        if 1 <= player_move <= 9:
            if field[player_move] == "X" or field[player_move] == "O":
                print("This field is already occupied. Please choose a free field.")
            else:
                return player_move
        else:
            print("Invalid Entry, please try again!")


def change_player():
    global active_player
    if active_player == "X":
        active_player = "O"
    else:
        active_player = "X"


def win_check():
    # Check Zeilen
    if field[1] == field[2] == field[3]:
        return field[1]
    if field[4] == field[5] == field[6]:
        return field[4]
    if field[7] == field[8] == field[9]:
        return field[7]
    # Check Spalten
    if field[1] == field[4] == field[7]:
        return field[1]
    if field[2] == field[5] == field[8]:
        return field[2]
    if field[3] == field[6] == field[9]:
        return field[3]
    # Check Diagonal
    if field[1] == field[5] == field[9]:
        return field[1]
    if field[3] == field[5] == field[7]:
        return field[3]


def draw_check():
    if field[1] != "1" and field[2] != "2" and field[3] != "3" and field[4] != "4" \
            and field[5] != "5" and field[6] != "6" and field[7] != "7" \
            and field[8] != "8" and field[9] != "9":
        return True


while run:
    print_field()
    next_move = game_move()
    if next_move is not None:
        field[next_move] = active_player
        winner = win_check()
        if winner:
            print(f"Spieler {winner} hat gewonnen!")
            run = False
        if draw_check():
            print("Unentschieden")
            run = False
        change_player()
