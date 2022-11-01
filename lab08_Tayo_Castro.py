# Tayo Castro
# COSC 1423 T Th
# Lab 08

import list_module as lm

def main():
    choice = input("Would you like to run functions over a list? [yes/no] ")
    input_list = []
    while choice == "yes":
        try:
            num = int(input("Number of items in list: "))
        except ValueError:
            print("Oops, not a number! Goodbye.")
            return
        try:
            for i in range(num):
                print("Item #" + str(i + 1) + ":")
                item = float(input())
                input_list.append(item)
        except ValueError:
            print("Oops, not a number! Goodbye.")
            return
        print("List in descending order: ")
        lm.pretty_print_list(input_list)
        print()
        print("Average of list's numbers: ")
        y = lm.get_list_average(input_list)
        print(y)
        print()
        print("List minus even numbers: ")
        z = lm.get_list_minus_evens(input_list)
        lm.pretty_print_list(z)
        print()
        print("List with extremes removed: ")
        w = lm.remove_extremes(input_list)
        lm.pretty_print_list(w)
        print()

        choice = input("Test again? [yes/no] ")
main()

"""
Design Document Questions
=========================
● How long did this lab take you?
About 50 minutes.
● Which function was the most challenging?
The sorting one, because I didn't remember the sort function edits in place and doesn't return anything.
● Explain you get_list_minus_evens implementation.
It's a list comprehension with a modulo to handle the parity condition.
"""