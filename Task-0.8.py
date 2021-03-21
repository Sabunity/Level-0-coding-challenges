def time_converter(num):

    hours = int(num/60)
    minutes = num % 60

    if hours>1 and minutes>1:
        print("{} hours,".format(hours), "{} minutes".format(minutes))
    elif hours<2 and minutes>1:
        print("{} hour,".format(hours), "{} minutes".format(minutes))
    elif hours>1 and minutes<2:
        print("{} hours,".format(hours), "{} minute".format(minutes))
    else:
        print("{} hour,".format(hours), "{} minute".format(minutes))

time_converter(71)
