price_per_package = 99

quantity = float(input("Enter the number of packages purchased :"))

total_price = price_per_package * quantity
if quantity >= 1 and quantity <10 :
    discount_percentage = 0
elif quantity >= 10 and quantity <20 :
    discount_percentage = 0.1
elif quantity >= 20 and quantity <50 :
    discount_percentage = 0.2
elif quantity >= 50 and quantity <100 :
    discount_percentage = 0.3
elif quantity >100 :
    discount_percentage = 0.4
discount_amount = total_price * discount_percentage
total = total_price - discount_amount

print("Discount Amount @", discount_percentage * 100,"% : $", discount_amount)
print("Total Amount : $", total)
