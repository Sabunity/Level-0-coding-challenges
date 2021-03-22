"""
Definitions of "common", show that common does not imply the same for all charectoristics.
Hence for this code, I converted all the strings to lower cases
"""

def common_charecters():

    first_String= (input("Enter the first string: ")).lower()
    second_String= (input("Enter the second string: ")).lower()

    common = []

    for charecter in first_String:
        if charecter in second_String:
            common.append(charecter)
        else:
            None

    print("Common letters: {}".format(common))

common_charecters()

