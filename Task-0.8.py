""" Sabelo Mbatha's Task 0.8 """

def timeConverter():

    # Extracting the time
    num = int(input("Enter any number: "))
    a = int(num/60)
    b = num % 60

    # Printing the correct time label
    if a>1 and b>1:
        print("{} hours,".format(a), "{} minutes".format(b))
    elif a<2 and b>1:
        print("{} hour,".format(a), "{} minutes".format(b))
    elif a>1 and b<2:
        print("{} hours,".format(a), "{} minute".format(b))
    else:
        print("{} hour,".format(a), "{} minute".format(b))

timeConverter()
