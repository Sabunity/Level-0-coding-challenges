""" Sabelo Mbatha's Task 0.7 """

def To_Fahrenheit():
    cel = input("Input temperature: ")
    answer = (float(cel) * 9/5) + 32
    print("{} Degrees Fahrenheit".format(round(answer, 2)))

def To_Celsius():
    fah = input("Input temperature: ")
    answer2 = (float(fah) - 32) * 5/9
    print("{} Degrees Celsius".format(round(answer2, 2)))

def options():
    print(""" Welcome to the temperature degrees conversion zone
          [1] - Convert from Celsius to Fahrenheit
          [2] - Convert from Fahrenheit to Celsius
          """)

    action = input("What would you like to do today? (Enter a number): ")

    if action == "1":
        To_Fahrenheit()
    elif action == "2":
        To_Celsius()
    else:
        print("No valid choice was given, try again!")

options()
