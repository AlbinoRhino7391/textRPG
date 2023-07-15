mw_rooms =  {
    'Entrance': {
        'east': 'Locked_RM',
        'west': 'Broken_Door_RM',
        'search': 'You see:\n \
            A broken door to the West that you might be able to squeeze through,\n \
            A solid closed door to the East,\n \
            A pile of rubble to the North blocking the passage that way',
        'item': 'rubble'
    },
    'Broken_Door_RM': {
        'north': 'Rm1_Closet',
        'east': 'Entrance',
        'item': 'monster'
    },
    'Rm1_Closet': {
        'south': 'Broken_Door_RM',
        'item': 'key'
    },
    'Locked_RM':{
        'west': 'Entrance',
        'north': 'Side_Chamber'
    },
    'Side_Chamber':{
        'south': 'Locked_RM',
        'west': 'Main_Room2'
    },
    'Main_Room2':{
        'east': 'Side_Chamber',
        'west': 'RespiteRoom',
        'north': 'Dias'
    },
    'RespiteRoom':{
        'east': 'Main_Room2',
        'north': 'Preparation'
    },
    'Preparation':{
        'south': 'RespiteRoom',
        'east': 'Dias'
    },
    'Dias':{
        'west': 'Preparation',
        'south': 'Main_Room2',
        'east': 'BasementAccess'
    },
    'BasementAccess':{
        'west': 'BasementAccess',
        'east': 'UD_Path'
    }
}

