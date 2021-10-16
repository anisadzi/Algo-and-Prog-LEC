v = eval(input("Enter the plane's take off speed in m/s : "))
a = eval(input("Enter the plane's acceleration in m/s**2: "))

result = ((v ** 2)/(2 * a))
print("The minimum runway length needed for this airplane is", round(result,4), "meters.")