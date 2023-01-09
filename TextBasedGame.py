# Version 1.0 of the currently untitled Harry Potter Text Adventure Game.
# This is the final project for IT-140 at Southern New Hampshire University.
# Project requirements explicitly state that everything must be coded within one script, otherwise this would be split into seperate files for clarity.
import random

logo = ''' _   _                             ____          _    _               
| | | |  __ _  _ __  _ __  _   _  |  _ \   ___  | |_ | |_   ___  _ __ 
| |_| | / _` || '__|| '__|| | | | | |_) | / _ \ | __|| __| / _ \| '__|
|  _  || (_| || |   | |   | |_| | |  __/ | (_) || |_ | |_ |  __/| |   
|_| |_| \__,_||_|   |_|    \__, | |_|     \___/  \__| \__| \___||_|   
                           |___/    & THE TEXT-BASED ADVENTURE GAME   '''


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
    'Headmaster\'s Office': {
        'south': 'first flight of stairs',
        'horcrux': 'Salazar Slytherin\'s Locket',
        'voldemort': 'no',
        'times': 0,
    }
}

#game_start_room = 'Entrance Hall'
#destroyed_horcruxes = []

# TODO: Dictionary of responses.

def player_status(room, horcrux, moving):
    '''Displays the player's current room, the horcrux in their current room if they have yet to destroy it, and the list of horcruxes they have already destroyed.'''

    print("POTTER STATUS:")

    if room == 'Snape\'s Office':
        print(f"• You are currently in {room}.")
    elif room == 'staircase to the dungeons' or room == 'first flight of stairs' or room == 'second flight of stairs':
        if moving == 'south':
            print(f"• You are currently going down the {room}.")
        else:
            print(f"• You are currently going up the {room}.")
    else:
        print(f"• You are currently in the {room}.")

    if len(destroyed_horcruxes) == 0:
        print(f"• You have yet to destroy any horcruxes.")
    elif len(destroyed_horcruxes) == 1:
        print(f"• You have only destroyed {destroyed_horcruxes[0]} so far.")
    else:
        print(f"• The horcruxes you have already destroyed are ", end='')
        print('{} and {}.'.format(', '.join(destroyed_horcruxes[:-1]) + ',', destroyed_horcruxes[-1]))

    x = 6 - len(destroyed_horcruxes)

    if x == 0:
        print(f"• There are no horcruxes remaining.")
    elif x == 1:
        print(f"• There is {x} horcruxes remaining.")
    else:
        print(f"• There are {x} horcruxes remaining.")


def nav(directions, horcrux):
    '''Displays all input options to the player.'''

    if len(directions) <= 2:
        print(f"\n[ From your current room, you can only go ", end="")
        print(' or '.join(directions), end=". ")
    else:
        print(f"\n[ From your current room, you can go ", end="")
        print('{} or {}.'.format(', '.join(directions[:-1]) + ',', directions[-1]), end=" ")

    if horcrux == 'none':
        print("As there are no horcruxes in this room, it seems going elsewhere is your only option. ]")
    elif horcrux in destroyed_horcruxes:
        print("As you have already destroyed the horcrux in this room, it seems going elsewhere is your only option. ]")
    else:
        length = ["short", "quick", "lengthy", "difficult", "long"]
        print(f"After a {random.choice(length)} search, you find that the horcrux in this room is {horcrux}. To destroy it, please type 'destroy'.")


# TODO: Move between rooms function.

# TODO: Destroy horcrux function

# TODO: Win/Lose Function

# TODO: Welcome screen.

# TODO: Game Loop


print(logo, "\n \n")

# Testing values.
current_room = 'second floor girl\'s bathroom'
room_dict = list_of_rooms.get(current_room)
options = list(room_dict.keys())
valid_directions = options[:len(options) - 3]
room_horcrux = room_dict.get('horcrux')
direction = 'north'
destroyed_horcruxes = ['Salazar Slytherin\'s Locket', 'Rowena Ravenclaw\'s Diadem', 'Helga Hufflepuff\'s Cup']

# Testing functions.

player_status(current_room, room_horcrux, direction)
nav(valid_directions, room_horcrux)
