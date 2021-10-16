ta = int(input("Please enter your temperature between -58 degrees F to 41 degrees F : "))
while (1) :
    if (ta<-58 or ta>41) :
        ta = int(input("Please re-enter your value between -58 degrees F to 41 degrees F: "))

    if (ta>=-58 and ta<=41) :
        break 

v = int(input("Please enter your windspeed >= 2 mph : "))
while (2) :
    if (v < 2) :
        v = int(input("Please re-enter your value >= 2 mph : "))

    if (v >= 2) :
        break 

wc = 35.74 + (0.6215 * ta) - (35.75 *(v**0.16)) + (0.4275 * ta * (v**0.16))
print("The windchill index is ", round(wc, 3))