print("***TIP CALCULATOR***")
bill = float(input("how much did u spend? $"))
tip_percentage = float(input("What percentage tip would you like to give? "))
tip = bill * (tip_percentage / 100)
total = bill + tip
number_of_people = int(input("How many people to split the bill? "))
each_person = total / number_of_people
each_person = round(each_person, 2)  # rounding to 2 decimal places
print("Each person should pay: $", each_person)