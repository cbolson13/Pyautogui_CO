from MadLib_Chapter1 import *

print("Chapter 2")
print("Are you ready to begin your adventures? Yes/No")
if ready == "Yes":
    print("Okay.")
    print("My name is " + name1 + ", I have been the protector of " + city1 + "for the past six months.")
    print("Type a noun.")
    noun11 = input().lower()
    print("Type a verb in the past tense.")
    verb11 = input().lower()
    print("Type a verb in the past tense.")
    verb12 = input().lower()
    print("Type an adjective.")
    adj11 = input().lower()
    print("Type an adjective.")
    adj12 = input().title()
    print("Type an action verb in the past tense.")
    verb13 = input().lower()
    print("Type a group of people.")
    name11 = input().lower()
    
    print("Last week my friends, " + name2 + ", " + name3 + " and I came across an evil " + noun11 + ".")
    print("When we encountered the evil " + noun11 + ",we " + verb11 + " it.")
    print("We quickly " + verb12 + " away in a " + adj11 + "without looking back.")
    print("When we got back to the " + adj12 "quarters we were " + verb13 + "by our " + name11 ".")
    print("")

elif ready == "No":
    print("Your loss.")
else:
    print("That is not a valid answer.")
