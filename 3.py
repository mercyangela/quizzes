""""Define a function that computes the length of a given list or string."""

def list_length():
    length = 0
    enter = str(input("Enter the string whose length you want to compute: "))
    for x in enter:
        length += 1
    print("The length of the string is:", length)

list_length()
