""" Sabelo Mbatha's Task 0.9 """

def VowelExtractor():

    word = input("Enter a string: ")

    # Spliting the word
    vowels = []
    newWord = list(word)

    #Extracting the vowels
    for alphabet in newWord:
        if alphabet == "a":
            vowels.append("a")
        elif alphabet == "A":
            vowels.append("A")
        elif alphabet == "e":
            vowels.append("e")
        elif alphabet == "E":
            vowels.append("E")
        elif alphabet == "i":
            vowels.append("i")
        elif alphabet == "I":
            vowels.append("I")
        elif alphabet == "o":
            vowels.append("o")
        elif alphabet == "O":
            vowels.append("O")
        elif alphabet == "u":
            vowels.append("u")
        elif alphabet == "U":
            vowels.append("U")
        else:
            None

    print("""
The string has the following Vowels: {}""".format(vowels))

VowelExtractor()
