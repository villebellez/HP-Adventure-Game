# Version 1.0 of the currently untitled Harry Potter Text Adventure Game.
# This is the final project for IT-140 at Southern New Hampshire University.
# Project requirements explicitly state that everything must be coded within one file, otherwise this would be split into multiple files for clarity.


list_of_rooms = {
    'Entrance Hall': {
        'north': 'first flight of stairs',
        'south': 'staircase to the dungeons',
        'east': 'kitchen',
        'west': 'Ravenclaw Common Room',
        'horcrux': 'none',
        'voldemort': 'no',
        'times': 1,
    },
    'staircase to the dungeons': {
        'north': 'Entrance Hall',
        'east': 'Slytherin Common Room',
        'west': 'Snape’s Office',
        'horcrux': 'none',
        'voldemort': 'no',
        'times': 0,
    },
    'Slytherin Common Room': {
        'west': 'staircase to the dungeons',
        'horcrux': 'Marvolo Gaunt\'s Ring',
        'voldemort': 'no',
        'times': 0,
    },
    'Snape\'s Office': {
        'east': 'staircase to the dungeons',
        'horcrux': 'Nagini',
        'voldemort': 'no',
        'times': 0,
    },
    'Ravenclaw Common Room': {
        'east': 'Entrance Hall',
        'horcrux': 'none',
        'voldemort': 'no',
        'times': 0,
    },
    'kitchen': {
        'east': 'Hufflepuff Common Room',
        'west': 'Entrance Hall',
        'horcrux': 'none',
        'voldemort': 'no',
        'times': 0,
    },
    'Hufflepuff Common Room': {
        'west': 'kitchen',
        'horcrux': 'Helga Hufflepuff\'s Cup',
        'voldemort': 'no',
        'times': 0,
    },
    'first flight of stairs': {
        'north': 'first flight of stairs',
        'east': 'second floor girl\'s bathroom',
        'south': 'Entrance Hall',
        'horcrux': 'none',
        'voldemort': 'no',
        'times': 0,
    },
    'second floor girl\'s bathroom': {
        'west': 'first flight of stairs',
        'south': 'Chamber of Secrets',
        'horcrux': 'none',
        'voldemort': 'no',
        'times': 0,
    },
    'Chamber of Secrets': {
        'north': 'second floor girl\'s bathroom',
        'horcrux': 'Tom Riddle\'s Diary',
        'voldemort': 'no',
        'times': 0,
    },
    'first flight of stairs': {
        'north': 'Headmaster\' Office',
        'east': 'Room of Requirement',
        'west': 'Gryffindor Common Room',
        'horcrux': 'none',
        'voldemort': 'no',
        'times': 0,
    },
    'Room of Requirement': {
        'west': 'first flight of stairs',
        'horcrux': 'Rowena Ravenclaw\'s Diadem',
        'voldemort': 'no',
        'times': 0,
    },
    'Gryffindor Common Room': {
        'east': 'first flight of stairs',
        'horcrux': 'none',
        'voldemort': 'yes',
        'times': 0,
    },
    'Headmaster\' Office': {
        'south': 'first flight of stairs',
        'horcrux': 'Salazar Slytherin\'s Locket',
        'voldemort': 'no',
        'times': 0,
    }
}

#game_start_room = 'Entrance Hall'
#destroyed_horcruxes = []

#current_room = list_of_rooms.get(game_start_room)
#room_horcrux = current_room.get('horcrux')

# TODO: Dictionary of responses.

def player_status(room, horcrux, destroyed, moving):
    '''Displays the player's current room, the horcrux in their current room, and the list of horcruxes they have already destroyed.'''

    # TODO: Style player_status.
    print("PLAYER STATUS:")

    if room == 'Snape\'s Office':
        print(f"• You are currently in {room}.")
    elif room == 'staircase to the dungeons' or room == 'first flight of stairs' or room == 'second flight of stairs':
        if moving == 'south':
            print(f"• You are currently going down the {room}.")
        else:
            print(f"• You are currently going up the {room}.")
    else:
        print(f"• You are currently in the {room}.")

    if horcrux == 'none':
        print("• There are no horcruxes in this room.")
    elif horcrux in destroyed:
        print("• You have already destroyed the horcrux in this room.")
    else:
        print(f"• The horcrux in this room is {horcrux}.")

    if len(destroyed) == 0:
        print(f"• In case you\'ve forgotten, you have yet to destroy any horcruxes.")
    elif len(destroyed) == 1:
        print(f"• In case you\'ve forgotten, you have only destroyed {destroyed[0]} so far.")
    else:
        print(f"• In case you\'ve forgotten, the horcruxes you have destroyed already are ", end='')
        print('{} and {}.'.format(', '.join(destroyed[:-1]) + ',', destroyed[-1]))

# TODO: Navigation function ( what commands they can enter )

# TODO: Move between rooms function.

# TODO: Destroy horcrux function

# TODO: Win/Lose Function

# TODO: Welcome screen.

# TODO: Game Loop

# Testing area.
current_room = 'Headmaster\' Office'
validation = list_of_rooms.get(current_room)
room_horcrux = validation.get('horcrux')
direction = 'north'
destroyed_horcruxes = ['Salazar Slytherin\'s Locket', 'Rowena Ravenclaw\'s Diadem', 'Helga Hufflepuff\'s Cup']

player_status(current_room, room_horcrux, destroyed_horcruxes, direction)
