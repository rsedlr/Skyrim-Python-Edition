from random import *
from slowprints import printslow , inputslow , separate, ps
from playerinfo import player
import time , sys


#player.name = "Elfis"
#player.race = "High Elf"
global sworddmg
sworddmg = int(20)

global bowdmg
bowdmg = int(10)

global firedmg
firedmg = int(30)

def RNG():

    global rng
    rng = randrange(0,100)


class dragons:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


def dragonbattle():
    drnum = randrange(1,10)
    import playerinfo
    player1 = player(player.name,player.race,100)
    playerhp = player1.hp
    
    if drnum <= 4:
        dragon = dragons("Fire Dragon",120)
        global dragonname
        dragonname = dragon.name
        dragonhp = dragon.hp

    if drnum > 4 and drnum <= 10:
        dragon = dragons("Ice Dragon", 120)
        dragonname = dragon.name
        dragonhp = dragon.hp

    if drnum < 8 and drnum <= 10:
        dragon = dragons("Legendary Dragon" , 160)
        dragonname = dragon.name
        dragonhp = dragon.hp
        
    separate()
    ps("The enemy is a " + dragon.name + "!")
    time.sleep(0.5)
    playerhp = str(playerhp)
    printslow('''You have ''' + playerhp + '''HP, and you carry a sword,
                    a bow with arrows, and can cast fireball spells.''')
    playerhp = int(playerhp)
    time.sleep(0.5)
    separate()
    
    printslow("Sword, has a medium hit chance, and does medium damage,")
    time.sleep(0.5)
    printslow("Bow and Arrow, has a very high hit chance, but does less damage,")
    time.sleep(0.5)
    printslow("Fireball, has a lower hit chance, but does higher damage.")   
    separate()
    
    time.sleep(0.5)
    printslow("The " + dragon.name + " swoops in, slashing with its claws, but they just miss.")
    separate()

    while True:
        time.sleep(0.5)
        
        while True:
            separate()
            printslow("You attack, what are you going to attack with?")
            time.sleep(0.5)
            printslow("Sword")
            time.sleep(0.4)
            printslow("Bow")
            time.sleep(0.4)
            printslow("Fireball")
            time.sleep(0.2)
            atkans = str(input(inputslow("Attack: ")))

            if atkans.lower() == "sword":
                RNG()
                if rng <= 75:
                    dragonhp = int(dragonhp - sworddmg)
                    dragonhp = str(dragonhp)
                    printslow("Your attack hit! The " + dragonname + " is now on " + dragonhp + "HP.")
                    time.sleep(0.5)
                    dragonhp = int(dragonhp)
                    dmg = int(randrange(1,15))
                    playerhp = int(playerhp - dmg)
                    playerhp = str(playerhp)
                    dmg = str(dmg)
                    printslow("The dragon strikes you back for " + dmg + " damage! You are now on " + playerhp + "HP.")
                    dmg= int(dmg)
                    playerhp = int(playerhp)
                    break
                    
                else:
                    printslow("Your attack has missed!")
                    dmg = int(randrange(1,20))
                    playerhp = int(playerhp - dmg)
                    playerhp = str(playerhp)
                    dmg = str(dmg)
                    printslow("The dragon strikes you for " + dmg + " damage! You are now on " + playerhp + "HP.")
                    playerhp = int(playerhp)
                    dmg = int(dmg)
                    break
                        
            elif atkans.lower() == "bow":
                RNG()
                if rng <= 90:
                    
                    dragonhp = int(dragonhp - 10)
                    dragonhp = str(dragonhp)
                    printslow("Your attack hit! The " + dragonname + " is now on " + dragonhp + "HP.")
                    dragonhp = int(dragonhp)
                    time.sleep(0.5)
                    dmg = int(randrange(1,15))
                    playerhp = int(playerhp - dmg)
                    playerhp = str(playerhp)
                    dmg = str(dmg)
                    printslow("The dragon strikes you back for " + dmg + " damage! You are now on " + playerhp + "HP.")
                    dmg= int(dmg)
                    playerhp = int(playerhp)
                    break
                    
                else:
                    printslow("Your attack has missed!")
                    dmg = int(randrange(1,20))
                    playerhp = int(playerhp - dmg)
                    playerhp = str(playerhp)
                    dmg = str(dmg)
                    printslow("The dragon strikes you for " + dmg + " damage! You are now on " + playerhp + "HP.")
                    playerhp = int(playerhp)
                    dmg = int(dmg)
                    break
                    
            elif atkans.lower() == "fireball":
                RNG()
                if rng <= 60:
                    dragonhp = int(dragonhp - firedmg)
                    dragonhp = str(dragonhp)
                    printslow("Your attack hit! The " + dragonname + " is now on " + dragonhp + "HP.")
                    dragonhp = int(dragonhp)
                    time.sleep(0.5)
                    dmg = int(randrange(1,15))
                    playerhp = int(playerhp - dmg)
                    playerhp = str(playerhp)
                    dmg = str(dmg)
                    printslow("The dragon strikes you back for " + dmg + " damage! You are now on " + playerhp + "HP.")
                    dmg= int(dmg)
                    playerhp = int(playerhp)
                    
                else:
                    printslow("Your attack has missed!")
                    dmg = int(randrange(1,20))
                    playerhp = int(playerhp - dmg)
                    playerhp = str(playerhp)
                    dmg = str(dmg)
                    printslow("The dragon strikes you for " + dmg + " damage! You are now on " + playerhp + "HP.")
                    playerhp = int(playerhp)
                    dmg = int(dmg)
                    break
            elif atkans == "admin.command.end":
                playerhp = 0
                break
            elif atkans == "admin.command.win":
                dragonhp = 0
                break

            else:
                printslow("Choose your method of attack, Dragonborn!")

        if dragonhp < 0 or dragonhp == 0 or playerhp < 0 or playerhp == 0:
             break

    if playerhp <= 0:
        separate()
        printslow("No! The " + dragonname + " has defeated you!")
        time.sleep(1.5)
        printslow("GAME OVER!")
        time.sleep(0.4)
        printslow("Program closing in:")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        printslow("bye!")
        sys.exit()

    if dragonhp <= 0 or dragonhp == 0:
        separate()
        printslow("The dragon crashes to the ground, defeated!")
        
        time.sleep(0.8)
        printslow("Congratulations! You killed the " + dragonname+ "!")
        separate()
        time.sleep(0.5)
        ps("You start to absorb the " + dragonname + "'s soul.")
        
        if dragonname == "Fire Dragon":
            separate()
            time.sleep(1)
            ps("As you absorb the dragon's soul, you feel your fireball spell increasing in power.")
            firedmg = firedmg + 5
            firedmg = str(firedmg)
            ps("Instead of doing " + (firedmg-5) + ", your new and improved spell now does " + firedmg + "!")
            firedmg = int(firedmg)
            
        if dragonname == "Ice dragon":
            separate()
            time.sleep(1)
            ps("As you absorb the dragon's soul, you feel your health increasing.")
            playerhp = playerhp + 10
            playerhp = str(playerhp)
            ps("You now have " + playerhp + "HP!")
            playerhp = int(playerhp)
            player.hp = playerhp
            
        if dragonname == "Legendary Dragon":
            separate()
            time.sleep(1)
            ps("As you absorb the dragon's soul, you feel your health increasing\nand your fireball spell growing in power")
            firedmg = firedmg + 5
            playerhp = playerhp + 10
            playerhp = str(playerhp)
            firedmg = str(firedmg)
            ps("Instead of doing " + (firedmg-5) + ", your new and improved spell now does " + firedmg + "!")
            ps("You now have " + playerhp + "HP!")
            firedmg = int(firedmg)
            playerhp = int(playerhp)
            player.hp = playerhp

        separate()
        printslow("Would you like to continue, or end the game?")
        
        while True:
            contans = str(input(inputslow("Continue or End? ")))    
            if contans.lower() == "continue":
                time.sleep(0.4)
                printslow("Off you go then!")
                break
            elif contans.lower() == "end":
                time.sleep(0.8)
                printslow("Program closing in:")
                print("3")
                time.sleep(1)
                print("2")
                time.sleep(1)
                print("1")
                time.sleep(1)
                printslow("bye!")
                sys.exit()
            elif contans.lower() == "retry":
                separate()
                dragonbattle()
                break
            else:
                printslow("Correct answer please?")
                time.sleep(0.5)
                


#dragonbattle()     
                    
                    

