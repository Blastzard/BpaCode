#128194
import random

# Starting attributes
name = ""
weapon = ""
health = 1000
gold = 0
strength = random.randint(12,17)
level = 0


'''
HELPER STRINGS -- Feel free to copy these lines to aid in your printouts:


A monster is attacking you!
Enter:  '1' to use your ___
        '2' to run away
Choice: ___
You defeated the monster and found ___!
That was rough! You lost ___ health.
Luckily you managed to get past the monster!
Press Enter to continue
___ gold
a health potion. You restored ___ health
Hello, ___
In this dungeon, you will fight three monsters.
If you survive to the end, treasure awaits!
You have your trusty ___, I see.
Good. You will need it.
Press Enter when you are ready to begin...
You made it to the treasure! You found ___ gold!
You didn't find the treasure, but you survived to fight again another day...
You fought as best you could, but didn't make it. 
The treasure waits for the next adventurer...
'''

# Write your functions here


def start_game():
    global name
    global weapon
    global gold
    global health
    global strength
    global level
    global index
    print("Welcome to the dungeon!")
    enter_name = input("What is your name, adventurer? ")
    enter_weapon = input("What is your weapon of choice? ")
    weapon=enter_weapon
    name=enter_name
    display_character()
    print(f"Hello {name}!\nIn this dungeon, you will fight three monsters. \nIf you survive to the end, treasure awaits!\nYou have your trusty {weapon}, I see\nGood. You will need it. ")
    input("Press enter when you are ready to begin...")
    index=0
    choice=1
    while index!=3 and choice!=2 and health>=0: #SC5 use a while loop to run the encounter function 3 times SC6 it also end the function if it is under 0 health or a 2 as the choice
        index+=1
        level+=1
        choice=encounter()
        if choice!=2 and health!=0:
            display_character()
        
    gameover() #SC7 calls gameover()
    display_character()
def display_character():
    #SC1 Prints the values for level, name, weapon, health, strength, gold
    global name
    global weapon
    global gold
    global health
    global strength
    global level
    if health==0:
        health=0
    print("\nName: ",name,"\t\tLevel: ", level)
    #SC2 This is where the gold is formated plus other outputs
    print("Gold: ",format(gold, ".2f"), "\t\tWeapon: ", weapon)
    print(f"Health: {health}\t\tStrength: {strength}\n")
def found_loot():
    global name
    global weapon
    global gold
    global health
    global strength
    global level
    randonum=random.randint(1,10) #SC3 this is a random value that gives a 30% chance health pot and 70% chance gold
    if (randonum>7):
        randonum==random.randint(1,3)*10
        health+=randonum
        print(f"a health potion. You restored {randonum} health.")
    else:
        randomnum=random.randint(25,150) #SC4 this makes a random number and adds it to global gold
        gold+=randomnum
        print(f"{randomnum} gold!")
        
def encounter():
    global name
    global weapon
    global gold
    global health
    global strength
    global level
    print("A monster is attacking you!")
    choice=3
    go=False
    while go==False: 
        try:
            choice=int(input(f"Enter: \t'1' to use your {weapon}, \n\t'2' to run away\nChoice: "))
            while choice<1 or choice>2: #SC8 makes sure there is no other values besides 1 and 2
                choice=int(input("Input a number between 1 and 2: "))
            go=True
        except:
            go=False
    if choice==1:
        monsterstrength=random.randint(10,20)
        if strength>=monsterstrength:
            print("You defeated the monster and found ",end='')
            found_loot() #SC9 calls found_loot()
            input()
        else:
            healthlost=(monsterstrength-strength)*10 #SC9 monster strength
            health-=healthlost
            print(f"That was rough! you lost {healthlost} health")
            print("Luckily you managed to get past the monster! ")
            print("Press enter to continue...")
            input()
    return choice #SC10 Returns user input
def gameover():
    global name #SC13 global variables
    global weapon
    global gold
    global health
    global strength
    global level
    global index
    #SC11 establishes 3 criteria
    if health<=0:
        health=0
        print("You fought as best as you could, but didn't make it. \nThe treasure waits for the next adventurer\n")
    elif index==3:
        randomgold=random.randint(500,5000) #sC12 random gold amount between 500 and 5000
        print(f"You made it to the treasure! You found {randomgold} gold!\n")
        gold+=randomgold
    else:
        print("\nYou didn't find the treasure, but you survived to fight another day...\n")
start_game()