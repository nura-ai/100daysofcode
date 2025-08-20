myBill = float(input("what was the bill? : "))
numberOfPeople = int(input("how many people to split the bill? : "))
eachPerson = myBill / numberOfPeople
eachPerson = round(eachPerson, 2)  # rounding to 2 decimal places
print("Each person should pay: ", eachPerson)