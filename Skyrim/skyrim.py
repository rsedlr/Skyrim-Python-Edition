from slowprints import printslow , inputslow ,  separate, ps
from skyrimarrays  import races , places
from riverwood import rwevent, rwrandomevents, dragonattack
from battles import dragonbattle
from random import *
from playerinfo import player
import time , sys


def RNG():
    global rng
    rng = randrange(0,100)

separate()

time.sleep(1)
printslow("Welcome to Skyrim: Python Edition")
time.sleep(1)

while True:             #while loop allows the code to repeat if they do not write a correct answer
    answer = str(input(inputslow("Would you like to play? ")))
    if answer.lower() == "yes" or answer.lower() == "y":
        printslow("On your way then")
        break
    elif answer == "no" or answer.lower() == "n":
        printslow("Begone from this land")
        sys.exit()
    else:
        printslow("Answer me.")

time.sleep(1)
printslow("Dialogue: select the number next the to line you want your character to say")
separate()

printslow("What is your name, adventurer?")
time.sleep(1)
player.name = input("Name:  ")
time.sleep(1.5)
printslow("What is your race?")

for x in races:
    printslow(x)
    time.sleep(0.3)

while True:
    player.race = str(input(inputslow("Race: ")))
    time.sleep(1.2)
    if player.race.lower() == "argonian":
        player.race = "Argonian"
        origin = "Black Marsh"
        break
    elif player.race.lower() == "breton":
        player.race = "Breton"
        origin = "High Rock"
        break
    elif player.race.lower() == "nord":
        player.race = "Nord"
        origin = "Skyrim"
        break
    elif player.race.lower() == "imperial":
        player.race = "Imperial"
        origin = "Cyrodil"
        break
    elif player.race.lower() == "dark elf":
        player.race = "Dark Elf"
        origin = "Morrowind"
        break
    elif player.race.lower() == "high elf":
        player.race = "High Elf"
        origin  = "Sommerset"
        break
    elif player.race.lower() == "wood elf":
        player.race = "Wood Elf"
        origin = "Valenwood"
        break
    elif player.race.lower() == "kahjiit":
        player.race = "Kahjiit"
        origin = "Elswehyr"
        break
    elif player.race.lower() == "redguard":
        player.race = "Redguard"
        origin = "Hammerfell"
        break
    elif player.race.lower() == "orc":
        player.race = "Orc"
        origin = "Orsinium"
        break
    else:
        printslow("Answer me! What race are you?")

printslow("You are " + player.name +   ", a " + player.race + " from " +  origin)

separate()
time.sleep(0.8)
printslow("Where would you like to go?")

for x in places:
    printslow(x)
    time.sleep(0.3)

time.sleep(1)
while True:
    placeans = str(input(inputslow("Place:")))
    if placeans.lower() == "riverwood" or placeans == "Riverwood":
        rwevent()
        break
    else:
        printslow("That area is not available yet...")





        
