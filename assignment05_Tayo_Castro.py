# -*- coding: utf-8 -*-
"""
Tayo Castro
COSC 1426 TTh
Assignment 05
"""
def running_total(iterations, limit, highest_item, highest_price):
    total = 0
    for i in range(iterations):
        item_name = input("Item name: ")
        item_price = float(input("Item price: "))
        total += item_price
        # This part keeps track of the highest priced item and its price
        if item_price > highest_price:
            highest_item = item_name
            highest_price = item_price
        else:
            pass
        # Next this part determines if user went over budget
        if total > limit:
            print("You went over budget!")
            print("Next time try spending less on " + highest_item + " it cost you " + highest_price)
        else:
            print("You stayed under budget! Congratulations!")
        
    return

def main():
    print("Welcome!")
    expenditures = int(input("How many expenditures? "))
    budget = float(input("What was your budget last month?"))
    expensive_item = "NA"
    expensive_price = 0
    running_total(expenditures, budget, expensive_item, expensive_price)    
    return

main()

"""
DESIGN DOC QUESTIONS
====================


"""