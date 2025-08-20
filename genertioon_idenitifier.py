print("___Generation Identifier___")
theYear = int(input("Which year were you born in?  "))
if theYear < 1900 and theYear > 1883:
    print("Damn! i didn't know dinosaurs are still alive!? is that true that the Lost Generation live in the Jurassic Park?")
elif theYear < 1927 and theYear >= 1901:    
    print("oh wow guys! come here look at the mummy 🤩. Right now we are observing one of the rare and probably unrepideble things on the earch. How one of the rappresentanties the Greatest Generation using computer.")
elif theYear < 1946 and theYear >= 1928:
    print("You are from the Silent Generation. hello grandpa or ma?!")
elif theYear < 1964 and theYear >= 1947:
    print("You are from the Baby Boomer Generation. You are getting old.")
elif theYear < 1980 and theYear >= 1965:
    print("You are from Generation X. You are middle-aged. i guess somebody's grumpy parent")
elif theYear < 1996 and theYear >= 1981:
    print("You are from the Millennial Generation. You are prob balding huh?! 😏.")
elif theYear < 2012 and theYear >= 1997:
    print("You are from Generation Z. aging, tik-tok, tik-tok, tik-tok.")
elif theYear > 2012 and theYear <= 2023:
    print("You are from Generation Alpha. You are a child. Your mom will be really mad at you!")
elif theYear > 2023:
    print("pfff! 🙄😏 yeah, sure, go away ")
else:
    print("what are you?! 🧐")
