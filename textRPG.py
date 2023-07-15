#!/usr/bin/env python3
""" Text-based RPG game
    Made By the WonderTwins:
    Michael and Eric"""

import os
import time
from character_classes import character_classes #import the dict of character classes
from main_level_map import main_floor #import the dict for the main_floor

def clear_screen():
    """Eric
    Clear the screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

def characterCreation():
    """Eric
    Prompts the player to create their character by entering their name and choosing a class.
    Returns the character's name, class choice, and class attributes.
    """
    print("Let's begin by creating your character.")
    name = input("Enter your character's name: ")

    print("Now, choose your character class:")
    for class_key, class_data in character_classes.items():
        print(class_key + ". " + class_data["name"] + ": " + class_data["description"])

    class_choice = input("Enter the number corresponding to your desired class: ")

    # Retrieve the selected character class and its attributes
    selected_class = character_classes.get(class_choice)

    # Return the character's name, class choice, and class attributes
    return name, selected_class["name"], selected_class["description"], selected_class["health"], selected_class["armor"], selected_class["damage"]

def displayIntroduction():
    """Eric
    Displays the introduction and premise of the game to the player.
    """
    print(f"\n\nWelcome, {character_name} the {character_class}!")
    print("You have received a quest about an evil priest being controlled by an Illithid.")
    print("Your mission is to venture into the Unholy temple and put an end to their dark alliance.")
    print("Prepare yourself for a treacherous journey filled with danger and secrets!\n")

def displayCommandList():
    """Eric
    Display the available commands to the player."""
    print("Available commands:")
    print("  look: Display available directions.")
    print("  go <direction>: Move to a new location (e.g., go north).")
    print("  exit: Quit the game.\n")

# --Eric--Game start
character_name, character_class, class_description, health, armor, damage = characterCreation()

# --Eric--Display character information
print("\n\nCharacter Name:", character_name)
print("Character Class:", character_class)
print("Class Description:", class_description)
print("Health:", health)
print("Armor:", armor)
print("Damage:", damage)
displayIntroduction()

# --Eric--Initialize the current_location to "entrance" where the character starts
current_location = "entrance"

# Game loop --both Eric and Michael
first_time_in_entrance = True

while True:
    # Clear the screen after the first time the player leaves the entrance
    if not first_time_in_entrance:
        time.sleep(1)  # Add a 1-second delay
        clear_screen()

    # Display the current location's name and description
    location = main_floor[current_location]
    print(f"\n{location['name']}")
    print(location['description'])

    # Set the flag to False after leaving the entrance for the first time
    if current_location != "entrance":
        first_time_in_entrance = False

    # Display the available commands
    displayCommandList()

    # Get available directions to move from the current location
    available_directions = [direction for direction in location if direction not in ["name", "description"]]
    
    # Ask the player for their next move
    next_move = input("Enter your command: ")

    # Check if the player wants to exit the game
    if next_move.lower() == "exit":
        print("Thank you for playing! Goodbye.")
        break

    # Check if the player wants to look at available directions
    if next_move.lower() == "look":
        print("Available directions:", ", ".join(available_directions))
    elif next_move.startswith("go "):
        # Extract the direction from the command
        direction = next_move.split(" ", 1)[1]
        # Check if the chosen direction is valid
        if direction in available_directions:
            # Move the player to the next location
            current_location = location[direction]
        else:
            print("Invalid direction. Please choose a valid direction.")
    else:
        print("Invalid command. Please enter a valid command.")
