def area_of_triangle(side1, side2, side3):

    perimeter = side1 + side2 + side3
    semi_perimeter = perimeter/2

    Area = (((semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter-side3)) * semi_perimeter) * 1/2

    return round(Area, 2)

area_of_triangle(5, 6, 2)
