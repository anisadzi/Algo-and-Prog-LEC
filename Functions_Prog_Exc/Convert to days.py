hours = eval(input("Enter number of hours : "))
minutes = eval(input("Enter number of minutes : "))
seconds = eval(input("Enter number of seconds : "))


day1 = hours // 24
day2 = minutes // 1440
day3 = seconds // 86400

days = day1 + day2 +day3

print("The number of days is: ", days)
