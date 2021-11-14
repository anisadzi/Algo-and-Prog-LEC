def convert_temp() :
    f = eval(input("Enter a temperature in Fahrenheit : "))
    c = convert_to_celsius(f)
    k = convert_to_kelvin(c)

    print("The temperature in Fahrenheit is : ", f)
    print ("The temperature in Celsius is : ", c)
    print("The temperature in Kelvin is : ", k)


def convert_to_celsius(f) :
    c = 5/9 * (f - 32)
    return c


def convert_to_kelvin(c) :
    k = c + 273.15
    return k



convert_temp()