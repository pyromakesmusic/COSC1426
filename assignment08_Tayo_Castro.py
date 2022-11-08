# Tayo Castro
# COSC 1423 TTh
# Assignment 08

SLOT = "_"
MONSTER1 = "X"
MONSTER2= "O"

def win_condition_checker(board):
    win = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == board[i][j] == board[i][j]:
                print("You Won!")
                win = True
            else:
                win = False
    return win

def row_and_column_getter():
    row = int(input("Row:"))
    while row < 0 or row > 2:
        row = int(input("Oops, out of range, try again: "))
    column = int(input("Column:"))
    while column < 0 or column > 2:
        column = int(input("Oops, out of range, try again: "))
    return row, column

def place_checker_and_player(board, parity):
    row, column = row_and_column_getter()
    while board[row][column] != SLOT:
        print("Sorry, that space is taken! Try again.")
        row, column = row_and_column_getter()


    if win_condition_checker(board):
        print("Player", parity + 1, "Won!")
        return
    else:
        if parity == 0:
            board[row][column] = MONSTER1
        else:
            board[row][column] = MONSTER2
        return


def game_loop():
    board = [
        [SLOT,SLOT,SLOT],
        [SLOT,SLOT,SLOT],
        [SLOT,SLOT,SLOT]
    ]
    win = False
    parity = 0

    while win = False:
        place_checker_and_player(board, parity)
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

main()


"""
DESIGN DOC QUESTIONS
====================


"""