# Tayo Castro
# COSC 1423 TTh
# Assignment 09

import json

def get_dict(file):
    dict = {}
    for line in file:
        chars = line.split()
        dict[chars[0]] = chars[1]
    print(json.dumps(dict, indent=4))
    return dict

def reverse_dict(dict):
    output_dict = {}
    for key in dict:
        output_dict[dict[key]] = key
    return output_dict

def main():
    filename = input("Martian decryption file: ")
    file = open(filename, "r")
    dict = get_dict(file)
    language = input("Original language: ")
    translation_file = input("File to translate: ")

    translation_obj = open(translation_file, "r")
    output_file = open(("translation_" + filename), "w")
    for line in translation_obj:
        for char in line:
            if char.isalpha():
                char = char.lower()
                output_file.write(dict[char])

    read_obj = open("translation" + filename, "r")

    print(read_obj.read())

    return

main()


"""
DESIGN DOC QUESTIONS
====================


"""