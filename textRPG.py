#!/usr/bin/env python3
""" Text-based RPG game
    Made By the WonderTwins:
    Michael and Eric"""

from character_classes import character_classes

def characterCreation():
    """
    eric
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
    """
    Eric
    Displays the introduction and premise of the game to the player.
    """
    print(f"\n\nWelcome, {character_name} the {character_class}!")
    print("You have received a quest about an evil priest being controlled by an Illithid.")
    print("Your mission is to venture into the Unholy temple and put an end to their dark alliance.")
    print("Prepare yourself for a treacherous journey filled with danger and secrets!\n")

#GameLoop starts here, TODO wrap in a loop.
character_name, character_class, class_description, health, armor, damage = characterCreation()
# Display character information
print("\n\nCharacter Name:", character_name)
print("Character Class:", character_class)
print("Class Description:", class_description)
print("Health:", health)
print("Armor:", armor)
print("Damage:", damage)
displayIntroduction()


