print("what year is it, i will calculate how many seconds are in it")
year = int(input("Enter the year: "))
secondsInDay = 24 * 60 * 60  # seconds in a day
leapyear = input("Is it a leap year? (yes for yes, 'idk' if you r a dumbass): ")

isLeap = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

if leapyear.lower() == "yes":
    if isLeap:
        secondsInYear = secondsInDay * 366
        print("Seconds in a year:", secondsInYear)
    else:
        print("Did you really think you can trick me? 😏")
        secondsInYear = secondsInDay * 365
        print("Seconds in a year:", secondsInYear)
elif leapyear.lower() == "idk":
    if isLeap:
        secondsInYear = secondsInDay * 366
    else:
        secondsInYear = secondsInDay * 365
    print("Seconds in a year:", secondsInYear)
else:
    secondsInYear = secondsInDay * 365
    print("Seconds in a year:", secondsInYear)