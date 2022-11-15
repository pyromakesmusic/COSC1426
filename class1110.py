vowels = set("aeiou")

vowels.add("y")

print(vowels)

letter = input("Enter a letter: ")
letter = letter.lower()

if letter in vowels:
    print("You entered a vowel!")