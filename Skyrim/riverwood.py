from random import *
import sys , time
from battles import dragonbattle
from slowprints import printslow , inputslow , separate, ps
from playerinfo import player

#name = "Elfis"


def RNG():
    global rng
    rng = randrange(0,100)



def rwrandomevents():
    RNG()
    if rng <= 140:
        RNG()
        if rng <= 110:
            
            dragonattack()
        else:
            banditattack()

def rwevent():
    printslow("You chose to head to Riverwood")
    separate()
    time.sleep(1)
    printslow("You set off from your travels to Riverwood")
    time.sleep(0.25)
    printslow("a scenic town in a valley,")
    time.sleep(0.25)
    printslow("surrounded by huge mountains")

    time.sleep(2)
    rwrandomevents()
    separate()
    printslow("You have arrived in Riverwood")
    riverwoodvisit()

def dragonattack():
    separate()
    printslow("As you are travelling down the road,")
    time.sleep(0.5)
    printslow("you hear a bone-chilling roar,")
    printslow("and a shadow passes over your head")
    time.sleep(0.5)
    printslow("The unmistakable shape of a Dragon!")
    separate()
    time.sleep(1)
    while True:
        ansb = str(input(inputslow("""Are you going to face this monster?
Yes or No """)))
        if ansb.lower() == "yes" or answer.lower() == "y" :
            printslow("To Battle!!")
            dragonbattle()
            
            break
        elif ansb.lower() == "no" or answer.lower() == "n":
            printslow("Retreat!!!")
            break
        else:
            printslow("Answer Me!")
        


def riverwoodvisit():
    separate()
    printslow("Riverwood is a small town, only a short ride from Whiterun,")
    time.sleep(1)
    printslow("There are only  three areas of interest in this town:")
    time.sleep(0.5)
    printslow("Riverwood Blacksmith *Not Available*")
    printslow("The Sleeping Giant Inn")
    printslow("The Riverwood Trader *Not Available*")
    while True:
        ans = str(input(inputslow("Where would you like to go? ")))
        if ans.lower() == "the sleeping giant inn" or "inn" or "sleeping giant inn" or "the inn":
            printslow("You have chosen to go to the Sleeping Giant Inn")
            separate()
            time.sleep(1.5)
            printslow("You enter the Sleeping Giant Inn")
            sleepinggiantinn()
            break
        elif ans.lower() == "the blacksmith" or "riverwood blacksmith" or "blacksmith":
            printslow("This area is not available yet, please select another.")
            separate()
            break
        elif ans.lower() == "the riverwood trader" or "trader" or "riverwood trader":
            printslow("This area is not available yet please select another,")
            separate()
            break
        else:
            printslow("That is not a place in Riverwood, dragonborn.")
            separate()
    
def sleepinggiantinn():
    #printslow("You enter the Sleeping Giant Inn and see there are 4 interesting people.")
    separate()
    time.sleep(0.7)
    
    while True:
        printslow("There are 4 interesting people")
        printslow("There is the Innkeeper")
        printslow("There is the Shady figure in the corner of the room")
        printslow("There is the Guard by the hearth")
        printslow("There is the bard, playing her lute and singing")
        separate()
        time.sleep(0.5)
        printslow("Who would you like to talk to?")
        persans = str("")
        persans = str(input(inputslow("Answer: ")))
        if persans.lower() == "innkeeper" or persans.lower() == "the innkeeper":
            separate()
            time.sleep(0.5)
            printslow("You have chosen to speak to the Innkeeper")
            separate()
            printslow("""You approach the Innkeeper, she is busy cleaning a tankard.

"Hello """+ player.race +""", my name is Delphine, how can I help you?"

(1) I would like to rent a room.
(2) Heard any rumours lately?
(3) Who is that man in the corner?
             """)
        
            separate()
            choice = input(inputslow("Choice: "))            
            if choice == "1":
                printslow("Okay! Your room is on the right there.")
                separate()
                time.sleep(3)
                printslow("You wake up the next morning feeling well rested.")
                time.sleep(1)
                
                separate()
                    
            elif choice == "2":
                separate()
                printslow(""""I believe that there are a high quantity of bandits
on the road to Whiterun, I would be careful if I was you." """)
                    
            elif choice == "3":
                separate()
                printslow(""""I don't know friend. He pays, so i dont ask questions" """)
                    
            else:
                ps("Please enter the correct number")
            
                
        elif persans.lower() == "shady" or persans.lower() == "the shady figure" or persans.lower() == "shady figure" or persans.lower() == "mr slim shady":
            separate()
            time.sleep(0.5)
            ps("You have chosen to speak to the Shady Figure in the corner of the room.")
            separate()
            ps("""You approach the shady figure, he sees you coming and stares at you.
"Get away if you want to live,  """ + player.race + """"
You decide it's best to leave him be.""")

        elif persans.lower() == "bard" or persans.lower() == "the bard":
            separate()
            time.sleep(0.5)
            ps("You have chosen to speak to the Bard, playing her lute and singing.")
            separate()
            ps("""You approach the bard, she see you coming.
She stares at you while shes singing, and gestures for you to get lost,
You decide its best to leave her alone.""")
            
        elif persans.lower() == "the guard" or persans.lower() == "guard" or persans.lower() == "the guard by the hearth" or persans.lower() == "guard by the hearth":
            separate()
            time.sleep(0.5)
            ps("You have chosen to speak to the Guard by the hearth")
            separate()
            while True:
                quote = randrange(1,10)
                if quote == 1:
                    ps(""" You approach the guard, he looks bored.
"I'd be a lot warmer and a lot happier with a bellyful of mead..."
He then stares at you blankly.""")
                if quote == 2:
                    ps("""You approach the guard, he looks in pain.
"I used to be an adventurer like you. Then I took an arrow in the knee..."
He then stares at you blankly.""")
                if quote == 3:
                    ps("""You approach the guard, he looks bored.
"No lollygaggin'."
He then stares at you blankly.""")
                if quote == 4:
                    ps("""You approach the guard, he looks angry.
"Let me guess... someone stole your sweetroll."
He then stares at you blankly.""")
                if quote == 5:
                    ps("""You approach the guard, he looks bored.
"My cousin's out fighting dragons, and what do I get? Guard duty."
He then stares at you blankly.""")
                if quote == 6:
                    ps("""You approach the guard, he looks concerned.
"What is it? Dragons?"
He then stares at you blankly.""")
                if quote == 7:
                    ps("""You approach the guard, he looks angry.
"Disrespect the law, and you disrespect me."
He then stares at you blankly.""")
                if quote == 8:
                    ps("""You approach the guard, he looks anxious.
"Gotta keep my eyes open. Damn dragons could swoop down at any time."
He then stares at you blankly.""")
                if quote == 9:
                    ps("""You approach the guard, he looks anxious;
"Fear not. Come dragon or giant, we'll be ready."
He then stares at you blankly.""")
                if quote == 10:
                    ps("""You approach the guard, he looks disinterested.
"I mostly deal with petty thievery and drunken brawls. Been too long since we've had a good bandit raid."
He then stares at you blankly""")
                    
                                     
                separate()
                ps("Would you like to interact with him again? \nYes or No")
                answer = str(input(inputslow("Answer: ")))
                if answer.lower() == "yes" or answer.lower() == "y":
                    ps("You speak to the Guard again")
                    separate()
                elif answer.lower() == "no" or answer.lower() == "n":
                    ps("You have chosen to not speak to the Guard again")
                    break
                else:
                    ps("I'll take your weird answer as a no")
                    
                    break               
        separate()
        ps("Would you like to talk to another person?\nYes or No")
        answer = str(input(inputslow("Answer: ")))
        if answer.lower() == "yes" or answer.lower() == "y":
            ps("You have chosen to talk to people again.")
            separate()
            continue
        elif answer.lower() == "no" or answer.lower() == "n":
            ps("You exit the Inn")
            break
        else:
            ps("I'll take your weird answer as a no")
            break
    
    ps("You have exited the inn")  
            

#sleepinggiantinn()

        
                                        
                    
            
        
        


        





    

    
            
