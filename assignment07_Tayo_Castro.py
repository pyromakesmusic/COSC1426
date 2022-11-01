# Tayo Castro
# COSC 1423 TTh
# Assignment 07

def get_operation(): # Grabs and validates user input on the operation
    op = input("What operation would you like to perform [split/append]? ")
    while op != "split" and op != "append":
        op = input("Sorry, not an option. Try again: ")
    return op

def try_to_open(filename): # Holds the exception logic
    try:
        file_obj = open(filename, "r")
    except FileNotFoundError:
        return FileNotFoundError
    return(file_obj)
def split_file():
    filename = input("Name of file to split: ")
    file_obj = try_to_open(filename)
    while file_obj == FileNotFoundError:
        filename = input("Whoops! File doesn't exist. Try again: ")
        file_obj = try_to_open(filename)
    output_1 = input("First output file: ")
    output_2 = input("Second output file: ")
    first_obj = open(output_1, "w")
    second_obj = open(output_2, "w")
    i = 0
    line = file_obj.readline()
    while line != "":

        if i % 2 == 0:
            first_obj.write(line)
        else:
            second_obj.write(line)
        i = i + 1
        line = file_obj.readline()
    first_obj.close()
    second_obj.close()
    print("Congrats! Enjoy your new files.")
    return

# See write up for implementation details
def append_files():
    filename = input("Name of file to write into: ")
    file_obj = open(filename, "w")
    file_append = "File to append: "
    while file_append != "":
        try:
            append_obj = open(file_append, "r")
            filename.write(append_obj.read())
            file_append = input("File to append: ")
        except FileNotFoundError:
            print("Oops! That file doesn't exist. Better try again next time.")
            return
    file_obj.close()
    print("File append successful.")
    return


def main():
    operation = get_operation()
    if operation == "split":
        split_file()
    elif operation == "append":
        append_files()
    else:
        get_operation(True)
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