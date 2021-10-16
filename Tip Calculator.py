import math

bill = eval(input("Enter the subtotal : $"))
tip_amount = eval(input("Enter tip amount (as a %) : "))
print("Subtotal : $", "{:,}".format(bill, ".00"))
total_1 = bill * (tip_amount / 100)
print("Tip : $", total_1)
total_2 = bill + total_1
print("Total : $", "{:,}".format(total_2))
