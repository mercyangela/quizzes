"""Write a function translate() that will translate a text into "rövarspråket"+\
(Swedish for "robber's language"). That is, double every consonant and place +\
an occurrence of "o" in between. For example, translate("this is fun") should +\
return the string "tothohisos isos fofunon""""

def translate():
	phrase = input("Insert phrase you want to translate: ").lower()
	new_phrase = ""
	for character in phrase:
		if (character == "a" or character == "e" or character == "i" or character == "o" or character == "u" or character == " "):
			new_phrase += str(character)
		elif:
			new_phrase += str(character) + o" + str(character)
	print("The phrase in rövarspråket is", new_phrase)
translate()
