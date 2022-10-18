# Tayo Castro
# COSC 1423 TTh
# Assignment 06
def input_to_flag(print_input):
    if print_input == "yes":
        print_bool = True
    else:
        print_bool = False
    return print_bool

def init():
    print_input = input_to_flag(input("Would you like to print X, Y, or Zee? [yes/no] "))
    return print_input
    # "What would you like to print? [letter/character]"
    # "What letter? [x/y] "
    # "What symbol would you like to use? "
    # print the thing



def main():
    print_input = input_to_flag(input("Print again? [yes/no] "))

main()


"""
DESIGN DOC QUESTIONS
====================


"""