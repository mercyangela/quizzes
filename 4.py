"""Write a function that takes a character (i.e. a string of length 1
and returns True if it is a vowel, False otherwise."""

def xters():
    character = input("Insert a character here: ").lower()
    if (character == 'a' or character == 'e' or character == 'i' or
        character == 'o' or character == 'u'):
        print("True. It is a vowel.")
    else:
        print("False. It is not a vowel.")
xters()
