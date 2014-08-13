"""Define a function reverse() that computes the reversal of a string. For
example, reverse("I am testing") should return the string "gnitset ma I"."""

def reverse():
    phrase = input("Enter the phrase you want to reverse: ")
    new_phrase = ""
    length = int(len(phrase))

    for x in range(0, length):
        new_phrase += phrase[-x-1]
    print("The string in reverse is: ", new_phrase)

reverse()
