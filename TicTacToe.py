L = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
who_plays = True  # True - player1, False - player2


def show_field():
    for i in range(3):
        print("---------------")
        for j in range(3):
            print(" | ", end=L[i][j])

        print(" |")
    print("---------------")


def move(who):
    if who:
        print("Player1 (X): ")
    else:
        print("Player2 (O): ")

    while True:
        try:
            x = int(input("Which row? (1, 2, 3): \n"))
            y = int(input("Which column? (1, 2, 3): \n"))
            if L[x - 1][y - 1] != " ":
                print("It's claimed, try again!")
            else:
                break
        except (IndexError, ValueError):
            print("Invalid move! Choose a row and column between 1 and 3.")

    if who:
        L[x - 1][y - 1] = "X"
    else:
        L[x - 1][y - 1] = "O"


def win_check():
    is_game_on = True
    for i in range(3):
        count_x_row = 0
        count_o_row = 0
        count_x_column = 0
        count_o_column = 0
        for j in range(3):
            if L[i][j] == "X":
                count_x_row += 1
            elif L[i][j] == "O":
                count_o_row += 1

            if L[j][i] == "X":
                count_x_column += 1
            elif L[j][i] == "O":
                count_o_column += 1

            if count_x_row == 3 or count_x_column == 3 or (L[0][0] == "X" and L[1][1] == "X" and L[2][2] == "X") or (
                    L[0][2] == "X" and L[1][1] == "X" and L[2][0] == "X"):
                print("Player 1 (X) won!")
                is_game_on = False
                break

            if count_o_row == 3 or count_o_column == 3 or (L[0][0] == "O" and L[1][1] == "O" and L[2][2] == "O") or (
                    L[0][2] == "O" and L[1][1] == "O" and L[2][0] == "O"):
                print("Player 2 (O) won!")
                is_game_on = False
                break

        else:
            continue
        break

    return is_game_on


show_field()

while True:
    move(who_plays)
    show_field()

    if not win_check():
        break

    who_plays = not who_plays
