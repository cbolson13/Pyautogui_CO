import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("What is your favorite color?")

answer = pg.prompt("Enter your favorite color below.")

if answer == "orange":
    speak.Speak("Wow, my favorite is orange too. We must be related.")
elif answer == "blue":
    speak.Speak("Blue screens make me scared.")
else:
    speak.Speak("Your favorite color is " + answer)

speak.Speak("What video would you like to watch?")

video = pg.prompt("Enter your video below")

speak.Speak("OK, let's look for " + video + " on Youtube.")

wb.open("https://www.youtube.com/results?search_query=" + video)
