def common_charecters(string1, string2):
    """
    Definitions of "common", show that common does not imply the same for all charectoristics.
    Hence for this code, I converted all the strings to lower cases
    """

    first_String= string1.lower()
    second_String= string2.lower()

    common = []

    for charecter in first_String:
        if charecter in second_String:
            common.append(charecter)
        else:
            None

    print("Common letters: {}".format(common))
 
common_charecters("house", "computers")