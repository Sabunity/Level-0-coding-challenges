def celsius_to_fahrenheit(celsius_temp):
    answer = (float(celsius_temp) * 9/5) + 32
    return round(answer, 2)

def fahrenheit_to_celsius(fahrenheit_temp):
    answer2 = (float(fahrenheit_temp) - 32) * 5/9
    return round(answer2, 2)

celsius_to_fahrenheit(100)
fahrenheit_to_celsius(212)