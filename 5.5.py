"""Write a function translate() that will translate a text into "rövarspråket"+\
(Swedish for "robber's language"). That is, double every consonant and place +\
an occurrence of "o" in between. For example, translate("this is fun") should +\
return the string "tothohisos isos fofunon""""

def translate():
    phrase = input("Insert phrase you want to translate: ").lower()
    new_phrase = ""
    for x in phrase:
        if (x == "a" or x == "e" or x == "i" or x == "o" or
            x == "u" or x == " "):
            new_phrase += str(x)
        else:
            new_phrase += str(x) + "o" + str(x)
    print("The new phrase in rövarspråket is", new_phrase)
translate()
