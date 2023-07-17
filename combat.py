#!/usr/bin/env python3
"""Michael
    function to handle combat and import into main file"""

from monsters import monsters
from character_classes import character_classes
import random
import time
import os

# global player_health  #temp: create global variable for use below
# player_health = 20    #temp: player_health will pull from character_classes file

# combat function to be imported and used in main file
def combat(monster_name, character_class, player_health):    #----------Will need to make adjustments when not hard coding
    player_health = None
    for class_data in character_classes.values():
        if class_data["name"] == character_class:
            player_health = class_data["health"]
            break
    if player_health is None:
        print("Invalid character class")
        return
    
    monster = monsters[monster_name]        # setting local monster to name from monsters dict
    monster_health = monster["health"]      # setting monster health from monsters dict
    # player_health = character_classes[character_class]["health"]           #----------Will need to make adjustments when not hard coding

    # show the user a monster appears in the room and ask for their action
    print(f"A {monster_name} appears! What do you want to do?")
    while True:     # start loop for encounter
        # ask player to choose to fight or run. Only valid input accepted
        choice = input("1. Fight\n2. Run\nEnter your choice: ")
        if choice == "1":
            fight(monster_name, monster_health, player_health)  # begin fight function
            break                  # if fight function concludes, break out of this while loop
        elif choice == "2":
            run(monster_name, monster_health, player_health)     # begin run function
            break                   # if run function concludes, break out of this while loop
        else:
            print("Invalid choice. Please choose a valid option.")

# simple roll function for use everywhere!!!!!!!!
def roll(dice):     # will input dice as "1d20", "2d4", "2d6", etc...
    # split the dice input using the "d".  The left entry is how many and the right is what number they go up to.
    num_dice, dice_sides = map(int, dice.split('d'))
    # roll and sum up the total amount of dice and each of their individual random rolls
    total = sum(random.randint(1, dice_sides) for _ in range(num_dice))
    return total    # return the total

# player turn fight function inside of combat
def fight(monster_name, monster_health, player_health):
    # while both player and monster are still alive
    while monster_health > 0 and player_health > 0:
        # time.sleep(2)           # after a 2 second delay
        # os.system('clear')      # clear the screen
        print("Your health:", player_health)    # display player's current health
        print(f"{monster_name}'s health: {monster_health}") # display monster's current health
        # ask the player if they want to attack or try to run(during combat)
        choice = input("\n1. Attack\n2. Run\nEnter your choice: ")
        if choice == "1":
            monster = monsters[monster_name]
            
            # if attack, roll 1d20 to see if the player hits
            hit_roll = roll("1d20")
            # display your hit roll
            print("You rolled a: " + str(hit_roll) + " to hit!")
            time.sleep(1)   # add a 1 second delay before moving forward
            # compare roll to monster's armor value
            if hit_roll > monster["armor"]: 
                print("\nYou hit the monster!")
                damage_roll = roll("1d6")   #----------changing this to pull damage value from character_classes dict
                # display the damage that you dealt, and reduce the monster's health by that amount
                print("You deal", damage_roll, "damage.")
                monster_health -= damage_roll
            else:
                # if you miss, display it
                print("\nYou miss the monster!")
            if monster_health <= 0:
                # check if monster is dead and display message
                print("You defeated the monster!")
            else:
                # if monster is still alive, display it's health
                print(f"The monster's health: {monster_health}")
        # if you choose run, execute run() function
        elif choice == "2":
            run(monster_name, monster_health, player_health)
            break   # if you succeed, break out of loop
        else:
            # check for invalid input
            print("Invalid choice. Please choose a valid option.")
        # after a 1 second delay, the monster takes his turn
        time.sleep(1)
        monsterAttack(monster_name, monster_health, player_health)

# function for if the player chooses run at anytime during combat
def run(monster_name, monster_health, player_health):
    # roll 1d20 to see if you succeed
    run_roll = roll("1d20")
    # gives a 50% chance to run
    if run_roll > 10:
        print("You successfully run away.")
    else:
        # if you fail to succeed, the monster takes a turn and attacks you
        print("You failed to escape and got attacked!")
        monsterAttack(monster_name, monster_health, player_health)
        # after the monster attacks, begin the normal fight() function
        fight(monster_name, monster_health, player_health)

# monster's turn attack function 
def monsterAttack(monster_name, monster_health, player_health):
    # global player_health  #------------currently hard coded, will change
    if monster_health > 0:
        # roll 1d20 for hit
        hit_roll = roll("1d20")
        if hit_roll >= 10:      #----------- will change to pull from armor value in character_classes dict
            monster = monsters[monster_name]
            print("\nYou got hit hit by the monster!")
            # damage roll calculated from monsters damage value in monsters dict
            damage_roll = roll(monster["damage"])
            print("You took", damage_roll, "damage.")
            # adjust player health by damage dealt
            player_health -= damage_roll
        else:
            # if the monster misses
            print("\nThe monster missed it's attack!")
        # check if the player is dead, and return message
        if player_health <= 0:
            print("You were defeated, GAME OVER!")
        else:
            # if the player is still alive, display player health
            print(f"Your health: {player_health}\n")      

# Currently hard coded to test function and ensure this file is working as intented
#------- this will instead pull monster_name from current_room["monster"] once imported in main file
# monster_name = "Skeleton"     
# #----- combat() will instead execute in the main file if there is a monster in the current room
# combat(monster_name, player_health)  