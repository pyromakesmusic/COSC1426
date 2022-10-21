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

def face_from_name(face):
    if face == "cute":
        print("^.^", end="")
    elif face == "meh":
        print(".-.", end="")
    elif face == "wow":
        print("@~@", end="")
    elif face == "neutral":
        print("*_*", end="")

def make_face(face_name, size):
    for col in range(size):
        print(" ", end="")
    face_from_name(face_name)
    for col in range(size):
        print(" ", end ="")
    print()
    return

def top_triangle(size, symbol):
    for row in range(size):
        for col in range((2 * row) - 1):
            print(" ", end="")
        print(f"{symbol}", end="")
        for col in range((3 * size) - (3 * row)):
            print(" ", end="")
        print(f"{symbol}", end="")
        print()
    return

def bottom_triangle(size, symbol):
    for row in range(size):
        for col in range(((2 * size) - 1) - (2 * row)):
            print(" ", end="")
        print(f"{symbol}", end="")
        for col in range((2 * row) - 1):
            print("  ", end="")
        print(f"{symbol}", end="")
        print()
    return

def leg(size, symbol):
    for row in range(size):
        for col in range((2 * size) - 1):
            print(" ", end="")
        print(f"{symbol}")
        print()
    return

def print_x(size, symbol="o"):
    top_triangle(size, symbol)
    bottom_triangle(size,symbol)

    return

def print_y(size, symbol):
    top_triangle(size, symbol)
    leg(size, symbol)
    return

def print_zee(face, size):
    make_face(face, size)
    top_triangle(size, "o")
    bottom_triangle(size, "o")

def print_chevron(size, symbol):
    top_triangle(size, symbol)
    top_triangle(size, symbol)

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
        if letter == "x":
            print_x(size, symbol)
        elif letter == "y":
            print_y(size, symbol)
    elif letter_or_character == "character":
        print_zee(face, size)
    elif letter_or_character == "chevron":
        print_chevron(size,symbol)
    return

def char_print():
    """
    This contains most of the logic of getting user input and converting it into the form needed for the print function
    :return:
    """
    l_or_c = input("What would you like to print? [letter/character/chevron] ")
    symbol = ""
    letter = ""
    face = ""

    while l_or_c != "letter" and l_or_c != "character" and l_or_c != "chevron":
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
    elif l_or_c == "chevron":
        symbol = input("What symbol would you like to use? ")
        while symbol == "":
            symbol = input("Oops, you didn't enter anything, try again: ")

    size = random.randint(1,5)

    print_loop(l_or_c, letter, face, size, symbol)
    return

def main():
    print_flag = init()
    while print_flag == True:
        char_print()
        print_flag = input_to_flag(input("Print again? [yes/no] "))

main()



"""
DESIGN DOC QUESTIONS
====================
● How long did you spend on this assignment?
Maybe 8-10 hours, and then 2 minutes on the extension.
● Is there anything you would change/improve about your assignment?
The algorithms for the whitespace characters are incorrect.
● How did you figure out how to print the letters?
I broke the letters up into pieces; they share some parts.
● Explain the process of putting Zee together.
It was an X, plus a face input.

"""