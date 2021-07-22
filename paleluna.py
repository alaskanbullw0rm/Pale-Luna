import random, time

# Global variables and arrays
validDirection = ["north", "east", "west"]
messages = ["PALE LUNA SMILES AT YOU", "THE AIR CHARS YOUR LUNGS", "PALE LUNA STARES",
            "DO YOU REMEMBER NOW", "BEAUTY IS IN THE EYE OF THE BEHOLDER"]
pickedUpShovel = doorOpen = notepad =  False
diggedHole = droppedHole = filledHole = goEast = False

# Prints following text
def Smiling():
    print()
    print(random.choice(messages))
    print()

# Self explanatory
def DarkCabinText():
    print()
    print("You are in a dark room. Moonlight shines through the window.")
    print("There is GOLD in the corner, along with a SHOVEL, a NOTEPAD with a pen, and a ROPE.")
    print("There is a DOOR in the EAST.")
    print()

# Asks for input from player and returns the input
def checkInput():
    print()
    print("Command?")
    print()
    Input = str(input(">"))
    print()
    return Input
    
# Covers first part of game. 
def DarkCabin():
    DarkCabinText()
    DarkCabinLoop()

# Contains loop for while player is in cabin
def DarkCabinLoop():
    global pickedUpShovel, doorOpen, goEast
    global notepad
    while goEast != True:
        time.sleep(2)
        print()
        print("You can see a DOOR here.")
        print()
        Input = str.lower(checkInput())

        if Input == "east":
            if doorOpen == True:
                goEast = True
            else:
                print("You open the door first.")
                goEast = True
        elif Input != "go east":
            if Input == "open door":
                doorOpen = True
                print("The door is now open. You can't see.")
            elif Input == "pick up shovel":
                pickedUpShovel = True
                print("Taken.")
            elif Input == "pick up gold":
                print("Taken.")
            elif Input == "pick up notepad":
                notepad = True
                print("Taken.")
            elif Input == "pick up rope":
                print("You've already used this.")
            elif Input == "use gold":
                print("Not here.")
            elif Input == "use rope":
                print("You've already used this.")
            else:
                print("I don't recognize that verb.")
    else:
        ForestPartTextOnce()
                
# Text for beginning of PathLoop()
def ForestPartTextOnce():
    print("Reap your reward again.")
    print("PALE LUNA SMILES AT YOU")
    print("You are in a wilderness that spans over infinity. The paths lead NORTH, WEST, and EAST")
    PathLoop()

# Loops until the correct path is chosen 29 times. Chosen path is randomly generated
# and will not crash game unlike original if wrong choice is inputted. Instead, loop
# will reset to previous iterator value
def PathLoop():
    time.sleep(2)
    correctDirections = []
    i = reset_i = 1
    while i < 5:
        command = str.lower(checkInput())
        direction = random.choice(validDirection)
        if command == direction:
            correctDirections.append(command.upper())
            print("You keep track of your location.")
            reset_i = i
            i += 1
        elif command == "look at notepad":
            if notepad == True:
                print("You look at your notepad:")
                print(*correctDirections, sep = " ")
            else:
                print("You forgot it.")
        else:
            print("You've strayed too far from the path, so you head back.")
            i = reset_i
        SmilingWidely(i)
    else:
        EndWhileLoop()

# Randomly prints text each time
def SmilingWidely(i):
    if i == random.randrange(1,30):
            Smiling()

# Consists of a print block.
def EndText():
    print()
    print("PALE LUNA SMILES WIDE")
    print()
    print("There are no more paths")
    print()
    print("PALE LUNA SMILES WIDE")
    print()
    print("The ground is soft")
    print()
    print("PALE LUNA SMILES WIDE")
    print()

# Calls print block then executes loop
# While loop will continue until following boolean values are all set to true
def EndWhileLoop():
    global diggedHole, droppedHole, filledHole, pickedUpShovel
    
    time.sleep(2)
    EndText()
    while filledHole != True:
        command = str.lower(checkInput())
        if pickedUpShovel == True:
            if command == "dig hole":
                print("You dig a hole. You feel the ground shake.")
                diggedHole = True
            elif command == "drop gold":
                if diggedHole == True:
                    print("The hole widens.")
                    droppedHole = True
                else:
                    print("There is nothing to drop it in.")
            elif command == "fill hole":
                if droppedHole == True:
                    print("You lose your balance and fall in. The ground shuts.")
                    time.sleep(4)
                    filledHole = True
                else:
                    print("I don't recognize that verb.")
            else:
                print("I don't recognize that verb.")
        else:
            Failure()
    else:
        Congrats()

#End of game. Loops message until EXIT is inputted
def Congrats():
    print()
    print("Congratulations")
    print()
    print("—— 69.3910 ——")
    print("—— 30.6052 ——")
    print()
    print("PALE LUNA LAUGHS")
    print()
    CongratsLoop()

def Failure():
    print("PALE LUNA FROWNS")
    print()
    CongratsLoop()
        
def CongratsLoop():
    time.sleep(2)
    print("INPUT EXIT")
    command = str.lower(checkInput())
    if command != "exit":
        CongratsLoop()

#main
DarkCabin()