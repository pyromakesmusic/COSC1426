# Tayo Castro
# COSC 1423 TTh
# Assignment 08

SLOT = "_"
MONSTER1 = "X"
MONSTER2= "O"

def pretty_print_board(board):
    for row in board:
        for column in row:
            print(column, end=" ")
        print()
    return

def win_condition_checker(board):
    win = None
    print(type(board))
    wins_horizontally = board[0][0] == board[0][1] == board[0][2] or board[1][0] == board[1][1] == board[1][2] or \
                        board[2][0] == board[2][1] == board[2][2]

    wins_vertically = board[0][0] == board[1][0] == board[2][0] or board[0][1] == board[1][1] == board[2][1] or \
                        board[0][2] == board[1][2] == board[2][2]

    wins_diagonally = board[0][0] == board[1][1] == board[2][2] or board[2][0] == board[1][1] == board[0][2]

    if wins_horizontally:
        win = "horizontally"
    elif wins_vertically:
        win = "vertically"
    elif wins_diagonally:
        win = "diagonally"
    else:
        win = False
    return win

def row_and_column_getter():
    row = int(input("Row: "))
    while row < 0 or row > 2:
        row = int(input("Oops, out of range, try again: "))
    column = int(input("Column: "))
    while column < 0 or column > 2:
        column = int(input("Oops, out of range, try again: "))

    print(row, column)
    return row, column

def place_checker_and_player(board, parity):
    print("Player", parity + 1, "Turn: ")
    row, column = row_and_column_getter()
    while board[row][column] != SLOT:
        print("Sorry, that space is taken! Try again.")
        row, column = row_and_column_getter()


    if win_condition_checker(board) == "horizontally" or win_condition_checker(board) == "vertically" \
            or win_condition_checker(board) == "diagonally":
        print("Player", parity + 1, "Won!")
        return
    else:
        if parity == 0:
            board[row][column] = MONSTER1
        else:
            board[row][column] = MONSTER2
        return board


def game_loop():
    board = [
        [SLOT,SLOT,SLOT],
        [SLOT,SLOT,SLOT],
        [SLOT,SLOT,SLOT]
    ]
    print(type(board[0][1]))
    win = False
    parity = 0

    while win == False:
        print("Board: ")
        print(board)
        board = place_checker_and_player(board, parity)
        print("Board:")
        print(board)
        #pretty_print_board(board)
        win = win_condition_checker(board)
        parity = (parity + 1) % 2

    return

def grid_monsters():
    print("Welcome! Let's play Grid Monsters!")
    print("Available slot: _")
    print("Monster 1:", MONSTER1)
    print("Monster 2:", MONSTER2)

    game_loop()

    return


def main():
    grid_monsters()

    return



"""
DESIGN DOC QUESTIONS
====================
● How long did this assignment take you?
2 or 3 hours.
● Did you complete the extension?
No.
● Explain your logic behind keeping track of the board information.
I tried to pass the list through as a variable. This does not seem to have worked for some reason. I even messed around 
with the nonlocal keyword and couldn't get it to run. Stumped.
● Explain the code for checking for a winner.
It was supposed to check for all the different types of win condition.

"""