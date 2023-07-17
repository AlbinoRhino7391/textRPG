#!/usr/bin/env python3
"""Eric
    dict to store character types."""

character_classes = {
    "1": {
        "name": "Warrior",
        "description": "A mighty warrior skilled in close combat.",
        "health": 30,
        "armor": 15,
        "damage": "1d8",
        "skill": "Power Attack"
    },
    "2": {
        "name": "Mage",
        "description": "A master of arcane magic with devastating spellcasting abilities.",
        "health": 20,
        "armor": 12,
        "damage": "1d6",
        "skill": "Magic Missile"
    },
    "3": {
        "name": "Rogue",
        "description": "A stealthy and agile thief, specializing in traps and sneak attacks.",
        "health": 25,
        "armor": 14,
        "damage": "2d4",
        "skill": "Backstab"
    }
}
"""Michael
    Dict to store usable skills and properties"""

skills = {
    "Power Attack": {
        "damage": 3,
        "description": "power attack text"
    },
    "Magic Missile": {
        "damage": 12,
        "description": "magic missile text"
    },
    "Backstab": {
        "damage": 5,
        "description": "Backstab text"
    }
}

