# Tayo Castro
# COSC 1423 TTh
# Lab 07

# Takes in a file object, reads from it, and writes to
# a new file as directed from the given file's contents
# (See writeup for expected structure)
def write_single_file(file_object):
    file = open(file_object, "r")
    num_files = int(file.readline().rstrip())

    for x in range(num_files):
        new_filename = file.readline().rstrip()
        print("Creating", new_filename)
        new_fileobj = open(new_filename, "a")
        num_items = int(file.readline().rstrip())
        for y in range(num_items):
            item = file.readline().rstrip()
            new_fileobj.write(item)
        new_fileobj.close()
    print("Write successful.")
    file.close()

# Takes in file name and returns a file opened for reading.
# If file name is not valid returns None
def get_file_object(file_name):
    try:
        file_obj = open(file_name)
    except FileNotFoundError:
        return None
    else:
        return file_obj

def main():
    filename = input("File to open? ")
    file_object = get_file_object(filename)
    while file_object == None:
        filename = input("Oops, that file doesn't exist! Try again: ")
        file_object = get_file_object(filename)

    write_single_file(filename)

    return

main()

"""
DESIGN DOC QUESTIONS
====================


"""