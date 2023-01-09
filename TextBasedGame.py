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
        'west': 'Snape\'s Office',
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
        'north': 'second flight of stairs',
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
    'second flight of stairs': {
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

# TODO: Dictionary of responses.

def player_status(room, horcrux, moving):
    '''Displays the player's current room, the horcrux in their current room if they have yet to destroy it, and the list of horcruxes they have already destroyed.'''

    print("\nPOTTER STATUS:")

    # TODO: Add moving options
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
        print(f"• There are no horcruxes remaining.\n")
    elif x == 1:
        print(f"• There is {x} horcruxes remaining.\n")
    else:
        print(f"• There are {x} horcruxes remaining.\n")


def nav(directions, horcrux):
    '''Displays all input options to the player.'''

    if len(directions) <= 2:
        print(f"[ From your current room, you can only go ", end="")
        print(' or '.join(directions), end=". ")
    else:
        print(f"[ From your current room, you can go ", end="")
        print('{} or {}.'.format(', '.join(directions[:-1]) + ',', directions[-1]), end=" ")

    if horcrux == 'none':
        print("As there are no horcruxes in this room, it seems going elsewhere is your only option. ]")
    elif horcrux in destroyed_horcruxes:
        print("As you have already destroyed the horcrux in this room, it seems going elsewhere is your only option. ]")
    else:
        length = ["short", "quick", "lengthy", "difficult", "long"]
        print(f"After a {random.choice(length)} search, you find that the horcrux in this room is {horcrux}. ]")


def move_rooms(valid_directions, direction, room_dict):
    '''Moves the player to the specified room, or allows them to see their progress.'''

    while True:
        decision = input(f"[ Which way would you like to go? You may also type 'status' to see more info on your progress. ] \n").lower()

        if decision in valid_directions:

            direction = decision
            room = room_dict.get(direction)

            if room == 'Snape\'s Office':
                print(f"[ You move into {room}. ]\n")
            elif room == 'staircase to the dungeons' or room == 'first flight of stairs' or room == 'second flight of stairs':
                if direction == 'south':
                    print(f"[ You move down the {room}. ]\n")
                else:
                    print(f"[ You move up the {room}. ]\n")
            else:
                print(f"[ You move into the {room}. ]\n")
            return room

        elif decision == 'status':
            player_status(current_room, room_horcrux, direction)

        else:
            print("[ That is an invalid input. Please try again. ]\n")

# TODO: Destroy horcrux function

# TODO: Win/Lose Check

# TODO: Welcome screen.

# Testing values.
current_room = 'Entrance Hall'
#destroyed_horcruxes = []
destroyed_horcruxes = ['Salazar Slytherin\'s Locket', 'Rowena Ravenclaw\'s Diadem']
direction = 'north'


def main(current_room):
    while True:
        room_dict = list_of_rooms.get(current_room)
        options = list(room_dict.keys())
        valid_directions = options[:len(options) - 3]
        room_horcrux = room_dict.get('horcrux')

        nav(valid_directions, room_horcrux)

        if room_horcrux != 'none' and room_horcrux not in destroyed_horcruxes:
            yn = input(f"[ Would you like to destroy it? Yes or no. ]\n").lower()
            if yn == 'yes':
                # TODO: Add in function.
                print("Well there's no get item function yet so you're SOL.")
            else:
                current_room = move_rooms(valid_directions, direction, room_dict)
        else:
            current_room = move_rooms(valid_directions, direction, room_dict)

print(logo, "\n \n")
main(current_room)
