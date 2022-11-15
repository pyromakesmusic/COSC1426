# Tayo Castro
# COSC 1423 TTh
# Lab09

import json

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def least_frequency(alpha):
    # Counts the least frequent key in a dictionary
    bar = 99999
    least_frequent = None
    for key in alpha:
        if alpha[key] < bar:
            bar = alpha[key]
            least_frequent = key
    return least_frequent, bar

def most_frequency(alpha):
    # Counts the most frequent key in a dictionary
    bar = 0
    most_frequent = None
    for key in alpha:
        if alpha[key] > bar:
            bar = alpha[key]
            most_frequent = key
    return most_frequent, bar

def main():
    letters = {}
    filename = input("Name of file to open: ")
    try:
        file = open(filename, "r", encoding="utf-8")
    except FileNotFoundError:
        print("Error: File doesn't exist. Exiting program.")
        return

    for line in file:
        words = line.rstrip().split()
        for word in words:
            lower_word = word.lower()
            for char in lower_word:
                if (char in letters) and char.isalpha():
                    letters[char] += 1
                elif char.isalpha():
                    letters[char] = 1
                else:
                    continue

    most_frequent, most_count = most_frequency(letters)
    least_frequent, least_count = least_frequency(letters)

    print("Most frequent letter: ", most_frequent)
    print("Occurences: ", most_count)
    print("Least frequent letter: ", least_frequent)
    print("Occurences: ", least_count)

    print("All frequencies: ")

    pretty_dict = json.dumps(letters, indent=4)
    print(pretty_dict)

    return

main()


"""
DESIGN DOC QUESTIONS
====================
Design Doc Questions (5 pts):
● How long did this lab take you?
About twenty minutes
● Did you do the extension?
No

"""