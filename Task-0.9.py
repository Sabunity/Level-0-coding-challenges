def vowel_extractor():

    word1 = input("Enter a string: ")

    # Spliting the word
    vowels = []
    word = word1.lower()
    newWord = list(word)

    #Extracting the vowels
    for alphabet in newWord:
        if alphabet in "a" and "a" not in vowels:
            vowels.append("a")
        elif alphabet in "e" and "e" not in vowels:
            vowels.append("e")
        elif alphabet in "i" and "i" not in vowels:
            vowels.append("i")
        elif alphabet in "o" and "o" not in vowels:
            vowels.append("o")
        elif alphabet in "u" and "u" not in vowels:
            vowels.append("u")
        else:
            None

    print("Vowels: {}".format(vowels))

vowel_extractor()
