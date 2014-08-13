import re
#re is a preinstalled class for regular expressions
#(will be used too strip them out)
def main():
    if is_palindrome() == True:
        print("The phrase you entered is a palindrome.")
    else:
        print("The string you entered is NOT a palindrome.")

def is_palindrome():
    print("Enter the phrase you'd like to check if palindrome or not: ")
    phrase = input()
    phrase = re.sub('\W', '', phrase)
    reversed_phrase = phrase[::-1]
    if phrase.lower() == reversed_phrase.lower():
        return True
    else:
        return False
main()

