""" Sabelo Mbatha's Task 0.5 """

def area_of_triangle():

    s1 = float(input("Enter length of 1st side: "))
    s2 = float(input("Enter length of 2nd side: "))
    s3 = float(input("Enter length of 3rd side: "))

    # Calculating the semi-perimeter (s)
    p = s1 + s2 + s3
    s = p/2

    # Now for Area
    z = (s-s1) * (s-s2) * (s-s3)
    Area = (z * s) * 1/2

    print()
    print(round(Area, 2))

area_of_triangle()
