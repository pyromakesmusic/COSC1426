# Tayo Castro
# COSC 1423 TTh
# Assignment 09

import json

def get_dicts(file):
    martian_to_english_dict = {}
    for x in range(26):
        line = file.readline().rstrip()
        chars = line.split()
        martian_to_english_dict[chars[0]] = chars[1]
    print(json.dumps(martian_to_english_dict, indent=4))

    english_to_martian_dict = {}
    for x in range(26):
        line = file.readline().rstrip()
        chars = line.split()
        english_to_martian_dict[chars[0]] = chars[1]
    print(json.dumps(english_to_martian_dict, indent=4))
    return martian_to_english_dict, english_to_martian_dict

def reverse_dict(dict):
    output_dict = {}
    for key in dict:
        output_dict[dict[key]] = key
    return output_dict

def main():
    filename = input("Martian decryption file: ")
    file = open(filename, "r")
    m2e_dict, e2m_dict = get_dicts(file)
    language = input("Original language: ")
    translation_file = input("File to translate: ")

    translation_obj = open(translation_file, "r")
    output_file = open(("translation_" + translation_file), "w")
    if language == "Martian":
        for line in translation_obj:
            for char in line:
                if char.isalpha():
                    char = char.lower()
                    try:
                        output_file.write(m2e_dict[char])
                    except KeyError:
                        output_file.write("")

    elif language == "English":
        for line in translation_obj:
            for char in line:
                if char.isalpha():
                    char = char.lower()
                    try:
                        output_file.write(e2m_dict[char])
                    except KeyError:
                        output_file.write("")


    file.close()
    translation_obj.close()
    output_file.close()

    read_obj = open("translation_" + filename, "r")

    print(read_obj.read())

    return

main()


"""
DESIGN DOC QUESTIONS
====================
● How long did this assignment take you?
About three or four hours.
● Did you complete the extension?
I did not.

"""