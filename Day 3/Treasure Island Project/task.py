print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
side = str(input("Do u wanna go left or right? Type L to Left or R to Right\n"))

if side == "L":
    print("U have come to a lake. There's an island in the middle of the lake." )
    boat = str(input("Type 'wait' to wait for a boat or 'swim' to swim across.\n"))
    if boat == "WAIT":
        door = str(input(("U arrived at the island. There's a house with 3 doors."
                          "\n One red, one yellow and one blue. Which one u choose?\n")))
        if door == "YELLOW":
            print("Congrats! U Won!")
        elif door == "RED":
            print("Burned by fire.Game Over")
        elif door == "BLUE":
            print("Eaten by beasts.Game Over.")
        else:
            print("Game Over!")
    else:
            print("U got attacked by sharks. Game over.")
else:
    print("U fell into a hole. Game Over.")
