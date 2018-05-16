print("What's your name?")
name = input().title()

if name == "Connor":
    print("Same here!")
else:
    print(name + " is a pretty cool name.")
                

print("What's your favorite sport")
sport = input().title()

if sport == "Soccer":
    print("Cool, what's your favorite team!")
    soccerteam = input().title()

    if soccerteam == "Liverpool":
        print("That is my favorite team also!")
    elif soccerteam == "Manchester United" or soccerteam == "Everton":
        print("Oh no, I like Liverpool and not " + soccerteam)
    else:
        print(soccerteam + " is not my favorite team, but I don't mind them")

    
elif sport == "Tenis":
    print("Cool, sometimes I like to play tenis too!")
else:
    print("Wow, " + sport + " sound fun!")



print("What's your favorite TV Show?")
tvshow = input().title()

if tvshow == "Flash" or tvshow == "Rick And Morty" or tvshow == "The Flash":
    print("I love " + tvshow + " too! Who is your favorite character?")
    character = input().title()

    if character == "Cisco" or character == "Barry" or character == "The Flash" or character == "Joe" or character == "Wally" or character == "Kid Flash" or character == "HR" or character == "Rick" or character == "Morty" or character == "Beth" or character == "Jerry" or character == "Summer" or character == "Mr.Meeseeks":
        print("Awesome, " + character + " is one of my favorite character too!")
    elif character == "Iris":
        print("I don't really like " + character + " that much.")
    else:
        print(character + " isn't my favorite, but I don't mind them.")

              
elif tvshow == "Leverage" or tvshow == "Psych" or tvshow == "Wizards Of Waverly Place":
    print("I used to watch " + tvshow + " too!")
else:
    print("I don't know about " + tvshow + " but it sounds good!")

