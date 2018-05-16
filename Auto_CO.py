import pyautogui as pg
import webbrowser
import time

player = pg.prompt(
    """:
Who is your favorite NBA basketball player?
a)Donovan Mitchel
b)Donovan Mitchel
c)Donovan Mitchel
d)Ben Simmons
e)Other
""")

if player == "a" or player == "b" or player == "c":
    pg.alert("Here's a video to prove you right!")
    webbrowser.open("https://www.youtube.com/watch?v=E0zOf3f4rgM")


elif player == "d":
    answer = pg.prompt(
        """
Do you think this video will change your answer?

""")
    pg.alert("We will see? He has only taken three pointers when the clock was running out.")
    webbrowser.open("https://www.youtube.com/watch?v=BN3sWGOT-rE")
    time.sleep(35)
    pg.alert("Well?")

elif player == "e":
    pg.alert("Here is a video of Donovan Mitchel. Maybe you will begin to follow him.")
    webbrowser.open("https://www.youtube.com/watch?v=E0zOf3f4rgM")
