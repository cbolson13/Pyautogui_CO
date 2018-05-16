name = "Connor"
state = "Montana"
city = "Big Sky"
tvshow = "The Flash"
videogame = "fifa18"
sport = "kiteboarding"
animal = "rock"
food = "water"
color = "beige"


print(name + " likes to visit " + state + " and " + city)
print("He also likes to do " + sport + " and always watches " + tvshow)
print(name + " wastes all of his time playing " + videogame + " all the time")
print(name + "'s favorite animal is a " + animal + " and it likes to eat " + food)
print(name + " likes the color " + color)


print("What's your favorite subject?")
subject = input()

if subject == "Rock" or subject == "The Flash":
    print("That is cool bro, same")


print("What is your favorite tv show?")
tvshow = input()

if tvshow == "The Flash" or tvshow == "Rick and Morty":
    print("No way same, bro")
elif tvshow == "Supergirl" or tvshow == "iZombie":
    print("You are a wierd person")
else:
    print("I don't know that one.")
    
