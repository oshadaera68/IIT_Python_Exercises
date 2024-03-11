# Find triangle's area with using Heron's formula
import math


def calculate_triangle_area(lfs, lss, lts):
    semi_perimeter = (lfs + lss + lts) / 2

    # Heron's Formula
    area = math.sqrt(semi_perimeter * (semi_perimeter - lfs) * (semi_perimeter - lss) * (semi_perimeter - lts))
    return area


area = calculate_triangle_area(5, 3, 5)
print(area)
