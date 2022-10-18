# Tayo Castro
# COSC 1423 TTh
# Assignment 06

import random

def input_to_flag(print_input):
    """
    Takes a string and gives a boolean sentinel
    :param print_input:
    :return:
    """
    if print_input == "yes":
        print_bool = True
    else:
        print_bool = False
    return print_bool

def init():
    """
    Gets the first printing flag
    :return:
    """
    print_input = input_to_flag(input("Would you like to print X, Y, or Zee? [yes/no] "))
    return print_input
def top_triangle(size, symbol):
    for row in range(0, size + 1, 2):
        for x in range(row):
            print(" ", end="")
        for col in range(size - row):
            print("* ", end = "")
        print()
    return

def bottom_triangle(size, symbol):
    return

def leg(size, symbol):
    return

def print_x(size, symbol="o"):
    for row in range(0, ((2 * size) + 1)):
        print(symbol, end="")
        for col in range(row, size + 2):
            print(" ", end="")
        print()
        print(symbol)

    return

def print_y(size):
    return

def print_face(face):
    return

def print_loop(letter_or_character, letter, face, size, symbol=""):
    """
    Main logic for the printing of the characters
    :param item:
    :param symbol:
    :param size:
    :return:
    """
    print(f"Printing {letter_or_character} of size {size}")
    if letter_or_character == "letter":
        print_x(size, symbol)
    elif letter_or_character == "character":
        pass
    return

def char_print():
    """
    This contains most of the logic of getting user input and converting it into the form needed for the print function
    :return:
    """
    l_or_c = input("What would you like to print? [letter/character] ")
    symbol = ""
    letter = ""
    face = ""

    while l_or_c != "letter" and l_or_c != "character":
        l_or_c = input("Sorry, I can't print that, try again: ")
    if l_or_c == "letter":
        letter = input("What letter? [x/y] ")
        while letter != "x" and letter != "y":
            letter = input("Sorry, I don't know how to print that letter, try again: ")
        symbol = input("What symbol would you like to use? ")
        while symbol == "":
            symbol = input("Oops, you didn't enter anything, try again: ")
    elif l_or_c == "character":
        face = input("What face would you like to use? [cute/meh/wow/neutral]")
        while face != "cute" and face != "meh" and face != "wow" and face!= "neutral":
            face = input("That isn't a valid face, try again: ")

    size = random.randint(1,5)

    print_loop(l_or_c, letter, face, size, symbol)
    return

def main():
    print_flag = init()
    while print_flag == True:
        char_print()
        print_flag = input_to_flag(input("Print again? [yes/no] "))

# main()

top_triangle(9, "0")

"""
DESIGN DOC QUESTIONS
====================


"""