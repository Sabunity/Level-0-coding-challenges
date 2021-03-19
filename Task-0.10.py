""" Sabelo Mbatha's Task 0.10 """

# Definitions of "common", show that common does not imply the same for all charectoristics.
# Hence for this code, I converted all the strings to lower cases

def commonCharecters():

    first_String= (input("Enter the first string: ")).lower()
    second_String= (input("Enter the second string: ")).lower()

    common = []

    for charecter in first_String:
        if charecter in second_String:
            common.append(charecter)
        else:
            None

    print("""
Common character(s) are: {}""".format(common))

commonCharecters()
