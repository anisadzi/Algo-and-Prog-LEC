import math

s = eval(input("Enter the side length of the hexagon : "))
Area = ((3 * math.sqrt(3) * (s * s)) / 2)
print("The minimum runway length needed for this area of a hexagon with side length ", s, " is ", round(Area,3))