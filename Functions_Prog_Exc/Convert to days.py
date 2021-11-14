#user input numbers

def convert_to_days() :
    hours = eval(input("Enter number of hours : "))
    minutes = eval(input("Enter number of minutes : "))
    seconds = eval(input("Enter number of seconds : "))
    return hours, minutes, seconds

def get_days(hours, minutes, seconds):
    days = (hours / 24) + (minutes / 1440) + (seconds / 86400)
    print(round(days,4))

def main():
    hours, minutes, seconds = convert_to_days()
    get_days(hours, minutes, seconds)


main()
