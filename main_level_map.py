#!/usr/bin/env python3
"""Eric
    dict to store the rooms in the main level of the Temple."""

main_floor = {
    "entrance": {
        "name": "Entrance",
        "description": "You stand at the entrance of the Unholy temple.",
        "north": "corridor1"
    },
    "corridor1": {
        "name": "Corridor 1",
        "description": "You find yourself in a dimly lit corridor.",
        "north": "corridor2",
        "east": "damp_room",  
        "south": "entrance"
    },
    "corridor2": {
        "name": "Corridor 2",
        "description": "You continue through the winding corridor.",
        "north": "corridor3",
        "south": "corridor1",
        "east": "torture_chamber",
        "west": "chamber_of_remnants"
    },
    "corridor3": {
        "name": "Corridor 3",
        "description": "You enter a long corridor with eerie whispers echoing.",
        "north": "hall_of_mirrors",
        "west": "unholy_archives",
        "south": "corridor2"
    },
    "hall_of_mirrors": {
        "name": "Hall of Mirrors",
        "description": "You stand in a chamber filled with mirrors reflecting twisted images.",
        "north": "altar_room",
        "west": "chamber_of_shadows",
        "south": "corridor3",
        "east": "summoning_chamber"
    },
    "altar_room": {
        "name": "Altar Room",
        "description": "You stand before the unholy altar where dark rituals take place.",
        "south": "hall_of_mirrors",
        "west": "library_of_forbbiden_knowledge"
    },
    "damp_room": {
        "name": "Damp Room",
        "description": "The Damp Room is filled with an unsettling smell of mildew and dripping water.",
        "west": "corridor1"
    },
    "torture_chamber" : {
        "name": "Torture Chamber",
        "description": "You enter the Torture Chamber, filled with grim devices and instruments of torment.",
        "west": "corridor2", 
        "north": "chamber_of_despair"
    },
    "chamber_of_despair" : {
        "name": "Chamber of Despair",
        "description": "You step into the Chamber of Despair, where tormented souls cry out in anguish.",
        "south": "torture_chamber"
    },
    "chamber_of_remnants" : {
        "name": "Chamber of Remnants",
        "description": "You arrive at the Chamber of Remnants, filled with ancient relics of the past.",
        "east": "corridor2",
        "south": "meditation_chamber",
        "north": "unholy_archives"
    },
    "meditation_chamber" : {
        "name": "Meditation Chamber",
        "description": "You step into the Meditation Chamber, an area of tranquility and reflection.",
        "north": "chamber_of_remnants"
    },
    "unholy_archives" : {
        "name": "Unholy Archives",
        "description": "You enter the Unholy Archives, a repository of forbidden knowledge and dark history.",
        "north": "chamber_of_shadows",
        "east": "corridor3",
        "south": "chamber_of_remnants"
    },
    "chamber_of_shadows" : {
        "name": "Chamber of Shadows",
        "description": "You stand in the Chamber of Shadows, shrouded in darkness and mystery.",
        "east": "hall_of_mirrors",
        "south": "unholy_archives"
    },
    "summoning_chamber" : {
        "name": "Summoning Chamber",
        "description": "You enter the Summoning Chamber, a place where dark entities are conjured.",
        "west": "hall_of_mirrors",
        "north": "ritual_bath"
    },
    "ritual_bath" : {
        "name": "Ritual Bath",
        "description": "You arrive at the Ritual Bath, a sacred space for pre-ritual cleansing.",
        "east": "sacrificial_chamber",
        "south": "summoning_chamber"
    },
    "sacrificial_chamber" : {
        "name": "Sacrificial Chamber",
        "description": "You step into the Sacrificial Chamber, where dark offerings are made.",
        "west": "ritual_bath"
    },
    "crypt" : {
        "name": "Crypt",
        "description": "You find yourself in the Crypt, where the remains of the deceased rest in eternal darkness.",
        "north": "damp_room"
    },
    "library_of_forbbiden_knowledge" : {
        "name": "Library of Forbidden Knowledge",
        "description": "You step through a obsidian encrested door to find a room filled with ancient books and scrolls, containing forbidden spells.",
        "east": "altar_room"
    }
}