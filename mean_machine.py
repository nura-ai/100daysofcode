print("Mean Old Insult Machine")
name = input("Who are you? ")
if name == "Diana" or name == "diana" or name == "DIANA":
    print("Oh great, it's you again.")
    print("on a scale of 1-10, how annoying are you today?")
    annoyance_level = input()
    if annoyance_level.isdigit():
        annoyance_level = int(annoyance_level)
        if annoyance_level < 5:
            print("Well, that's not too bad.")
        elif annoyance_level < 10:
            print("Hmm, you could be worse.")
        else:
            print("Wow, you're really pushing it today!")
    else:
        print("I don't have time for your nonsense.")
elif name == "Luna" or name == "luna" or name == "LUNA":
    print("What do you want, Luna?")
elif name == "Eva" or name == "eva" or name == "EVA":
    print("Eva, huh? Make it quick.")
elif name == "Aliya" or name == "aliya" or name == "ALIYA":
    print("Aliya? I don't have all day.")
print("on a scale of 1-10, how annoying are you today?")
annoyance_level = input()
if annoyance_level.isdigit():
    annoyance_level = int(annoyance_level)
    if annoyance_level < 5:
        print("Well, that's not too bad.")
    elif annoyance_level < 10:
        print("Hmm, you could be worse.")
    else:
        print("Wow, you're really pushing it today!")
else:
    print("Who are you again?")
    print("I don't have time for you " + name + ". ")
    print("Just go away!")
