print("Wholesome Positive Machine 🤗")
name = input("who are you?")
if name == "Diana" or name == "diana" or name == "DIANA" or name == "Luna" or name == "Eva" or name == "Aliya":
    print("Hello, " + name + "! You are a wholesome person.")
goal = input("what do you want to achieve? ")
mood = input("on a scale of 1-10, how do you feel today? ")
if mood.isdigit():
    mood = int(mood)
    if mood < 5:
        print("I'm sorry to hear that you're feeling down. Remember, it's okay to have off days.")
    elif mood == 5:
        print("You're feeling neutral. Let's work towards a positive mindset!")
    else:
        print("That's great to hear! Keep up the positive energy!")
        