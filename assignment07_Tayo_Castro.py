# Tayo Castro
# COSC 1423 TTh
# Assignment 07



def split_file():
    filename = input("Name of file to split: ")
    try:
        file_obj = open(filename, "r")
    except FileNotFoundError:
        filename = input("Whoops! File doesn't exist. Try again: ")
        file_obj = open(filename, "r")
	pass

# See write up for implementation details
def append_files():
    filename = input("Name of file to write into: ")
    file_obj = open(filename, "w")
    print("File append successful.")
	pass


def main():
    return

main()

"""
DESIGN DOC QUESTIONS
====================
● How long did you spend on the assignment?
● Did you do the extension?
● What would you have changed given more time/knowledge?
● Explain your splitting implementation.
● Explain your appending implementation.

"""