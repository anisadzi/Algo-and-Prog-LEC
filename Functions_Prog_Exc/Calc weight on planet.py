def calc_weight_on_planet (weight, g = 23.1) :
    mass = weight / 9.8
    wg = mass * g
    print(wg)

calc_weight_on_planet(120, 9.8)
calc_weight_on_planet(120)
calc_weight_on_planet(120, 23.1)