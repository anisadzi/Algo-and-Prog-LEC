import math

g = 9.8

m = eval(input("Enter the mass of the cart (in kg): "))
F = eval(input("Enter the force to push the cart (in N): "))

math.sin = F / (m * g)

print("The angle of the ramp is", round(math.degrees(math.sin), 1), "degrees")