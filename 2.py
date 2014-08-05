'''Define a function max_of_three() that takes three numbers as arguments and +\
returns the largest of them. '''

def max_of_three():
    uno = int(input("UNO: "))
    dos = int(input("DOS: "))
    tres = int(input("TRES: "))
    if uno > tres:
        if uno > dos:
            return uno
        else:
            return dos
    else:
        if tres > dos:
            return tres
        else:
            return dos
print("The max of the 3 numbers is", max_of_three())
