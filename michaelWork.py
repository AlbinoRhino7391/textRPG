#!/usr/bin/env python3
""" Text-based RPG game
    Made by the WonderTwins
    Michael and Eric"""

from random import randint
from monsters import *

def roll_damage(damage_dice):
    num_dice, dice_sides = map(int, damage_dice.split('d'))
    total = sum(randint(1, dice_sides) for _ in range(num_dice))
    print("Rolled a " + str(total) + " damage.")
    return total

def roll_for_monster(monster_name):
    if monster_name in monsters:
        monster_info = monsters[monster_name]
        damage_dice = monster_info["damage"]
        roll_damage(damage_dice)
    else:
        print("Monster not found")

# roll_for_monster("Zombie")