def area_of_triangle(s1, s2, s3):

    perimeter = s1 + s2 + s3
    semi_perimeter = perimeter/2

    Area = (((semi_perimeter - s1) * (semi_perimeter - s2) * (semi_perimeter-s3)) * semi_perimeter) * 1/2

    return round(Area, 2)

area_of_triangle(5, 6, 2)
