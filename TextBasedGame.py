# Version 1.0 of the currently untitled Harry Potter Text Adventure Game.
# This is the final project for IT-140 at Southern New Hampshire University.
# Project requirements explicitly state that everything must be coded within one file, otherwise this would be split into multiple files for clarity.


list_of_rooms = {
    'entrance': {
        'north': 'first stairs',
        'south': 'dungeon',
        'east': 'kitchen',
        'west': 'ravenclaw',
        'item': 'none',
        'times': 1,
    },
    'dungeon': {
        'north': 'entrance',
        'east': 'slytherin',
        'west': 'snape',
        'item': 'none',
        'times': 0,
    },
    'slytherin': {
        'west': 'dungeon',
        'item': 'ring',
        'times': 0,
    },
    'snape': {
        'east': 'dungeon',
        'item': 'nagini',
        'times': 0,
    },
    'ravenclaw': {
        'east': 'entrance',
        'item': 'none',
        'times': 0,
    },
    'kitchen': {
        'east': 'hufflepuff',
        'west': 'entrance',
        'item': 'none',
        'times': 0,
    },
    'hufflepuff': {
        'west': 'kitchen',
        'item': 'cup',
        'times': 0,
    },
    'first stairs': {
        'north': 'second stairs',
        'east': 'bathroom',
        'south': 'entrance',
        'item': 'none',
        'times': 0,
    },
    'bathroom': {
        'west': 'first stairs',
        'south': 'chamber',
        'item': 'none',
        'times': 0,
    },
    'chamber': {
        'north': 'bathroom',
        'item': 'diary',
        'times': 0,
    },
    'second stairs': {
        'north': 'headmaster',
        'east': 'requirement',
        'west': 'gryffindor',
        'item': 'none',
        'times': 0,
    },
    'requirement': {
        'west': 'second stairs',
        'item': 'diadem',
        'times': 0,
    },
    'gryffindor': {
        'east': 'second stairs',
        'item': 'voldemort',
        'times': 0,
    },
    'headmaster': {
        'south': 'second stairs',
        'item': 'locket',
        'times': 0,
    }
}

current_room = 'entrance'