def calc_new_height():
    width = float(input("Enter the current width : "))
    height = float(input("Enter the current height : "))
    new_width = float(input("Enter the desired width : "))

    hdivw = height / width
    newh = hdivw * new_width

    print("The corresponding height is : ", newh)
    return newh


calc_new_height()