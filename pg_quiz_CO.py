import pyautogui as pg
import time
import webbrowser


points = 0

# Question
answer = pg.prompt(
"""
Where would you land in Fortnight?

a) Tomato Town
b) Dusty Depot
c) Fatal Fields
d) Tilted Towers
e) Pleasant Park
f) Salty Springs

"""
    )

#Answer
pg.alert("You chose " + answer)

if answer == "a" or answer == "A":
    points += 1
elif answer == "b" or answer == "B":
    points += 5
elif answer == "c" or answer == "C":
    points += 10
elif answer == "d" or answer == "D":
    points += 15
elif answer == "e" or answer == "E":
    points += 20
elif answer == "f" or answer == "F":
    points += 25



# Question
answer = pg.prompt(
"""
What is your favorite weapon?

a) RPG/Grenade Launcher
b) Sniper 
c) Assult Riffle
d) Tactical Shotgun
e) Pistol
f) Pump Shotgun

"""
    )

#Answer
pg.alert("You chose " + answer)

if answer == "e" or answer == "E":
    points += 1
elif answer == "f" or answer == "F":
    points += 5
elif answer == "c" or answer == "C":
    points += 10
elif answer == "d" or answer == "D":
    points += 15
elif answer == "a" or answer == "A":
    points += 20
elif answer == "b" or answer == "B":
    points += 25




# Question
answer = pg.prompt(
"""
What is your average place?

a) 80-100
b) 50-79
c) 30-49
d) 10-29
e) 2-9 
f) Victory Royale

"""
    )

#Answer
pg.alert("You chose " + answer)

if answer == "a" or answer == "A":
    points += 1
elif answer == "b" or answer == "B":
    points += 5
elif answer == "c" or answer == "C":
    points += 10
elif answer == "d" or answer == "D":
    points += 15
elif answer == "e" or answer == "E":
    points += 20
elif answer == "f" or answer == "F":
    points += 25



# Question
answer = pg.prompt(
"""
What is your best Emote?

a) What is that?
b) Original Dance
c) Wave
d) Flex
e) Worm
f) Electro Shuffle

"""
    )

#Answer
pg.alert("You chose " + answer)

if answer == "a" or answer == "A":
    points = -250
elif answer == "b" or answer == "B":
    points += 5
elif answer == "c" or answer == "C":
    points += 10
elif answer == "d" or answer == "D":
    points += 15
elif answer == "e" or answer == "E":
    points += 20
elif answer == "f" or answer == "F":
    points += 25



# END OF SERVEY
pg.alert("Your character is...")


if points < 4:
    pg.alert("You are a noob.")
    webbrowser.open("https://www.google.com/search?q=tide+pods&rlz=1C1GCEA_enUS752US765&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiJwqOXovHYAhWPUt8KHbcvA2kQ_AUICygC&biw=681&bih=617#imgrc=CTrRDjlPFIL0-M:")
elif points >= 4 and points < 50:
    pg.alert("You are decent.")
elif points >= 50:
    pg.alert("You are the GOAT!")




