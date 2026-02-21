# import math

# def area_of_circle(r):
#     return math.pi * r ** 2

# diameter = float(input("What is the diameter of the Circle? "))
# radius = diameter / 2
# print("Radius:", radius)
# print("Area of the circle is " + str(area_of_circle(radius)))

# import math
# def area_rectangle(l, w):
#     return l * w

# l = float(input("Enter a length: "))
# w = float(input("Enter a width:"))
# print("Area of the rectangle is " + str(area_rectangle(l, w)))

# import math
# def triangle_area ( l , w):
#     return l * w / 2
# l = float(input("Enter a length: "))
# w = float(input("Enter a width: "))
# print("Area of a triangle is  " + str(triangle_area(l, w)))

# percent of free throws
# import math
# def ft_perc (made,attempts):
#     return  made / attempts * 100
# a = float(input("Enter number of attempts: "))
# m = float(input("Enter the number of made: "))
# # print("Percent of Free Throws is ", ft_perc(m,a), ".2f")
# print("Percent of Free Throws is %.2f" % ft_perc(m,a))

import math
def miles_per_gallon (miles,gallons):
    return miles/gallons
miles = float(input("Enter the miles driven: "))
gallons = float(input("Enter the gallons used: "))
print("Miles per gallon is %.2f" % miles_per_gallon(miles, gallons))