"""Define a function is_palindrome() that recognizes palindromes (i.e.
words that look the same written backwards). For example, is_palindrome("radar")
should return True."""

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

