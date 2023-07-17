#!/usr/bin/env python3
from monsters import monsters
import random
import time
import os

global player_health
player_health = 20

def combat(monster_name, player_health):
    monster = monsters[monster_name]
    monster_health = monster["health"]
    player_health = player_health

    print(f"A {monster_name} appears! What do you want to do?")
    while True:
        choice = input("1. Fight\n2. Run\nEnter your choice: ")
        if choice == "1":
            fight(monster_health)
            break
        elif choice == "2":
            run(monster_health)
            break
        else:
            print("Invalid choice. Please choose a valid option.")

def roll(dice):
    num_dice, dice_sides = map(int, dice.split('d'))
    total = sum(random.randint(1, dice_sides) for _ in range(num_dice))
    return total

def fight(monster_health):
    while monster_health > 0 and player_health > 0:
        time.sleep(2)
        os.system('clear')
        print("Your health:", player_health)
        print(f"{monster_name}'s health: {monster_health}")
        choice = input("\n1. Attack\n2. Run\nEnter your choice: ")
        if choice == "1":
            hit_roll = roll("1d20")
            if hit_roll >= 10:
                print("\nYou hit the monster!")
                damage_roll = roll("1d6")
                print("You deal", damage_roll, "damage.")
                monster_health -= damage_roll
            else:
                print("\nYou miss the monster!")
            if monster_health <= 0:
                print("You defeated the monster!")
            else:
                print(f"The monster's health: {monster_health}")
        elif choice == "2":
            run(monster_health)
            break
        else:
            print("Invalid choice. Please choose a valid option.")
        time.sleep(1)
        monsterAttack()

def run(monster_health):
    run_roll = roll("1d20")
    if run_roll >= 13:
        print("You successfully run away.")
    else:
        print("You failed to escape and got attacked!")
        monsterAttack()
        fight(monster_health)

def monsterAttack():
    global player_health
    hit_roll = roll("1d20")
    if hit_roll >= 10:
        print("\nYou got hit hit by the monster!")
        damage_roll = roll("1d6")
        print("You took", damage_roll, "damage.")
        player_health -= damage_roll
    else:
        print("\nThe monster missed it's attack!")
    if player_health <= 0:
        print("You were defeated, GAME OVER!")
    else:
        print(f"Your health: {player_health}")


monster_name = "Zombie"
combat(monster_name, player_health)