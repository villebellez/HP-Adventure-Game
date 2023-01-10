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

def player_status(room, horcrux, moving, directions):
    '''Displays the player's current room, the horcrux in their current room if they have yet to destroy it, and the list of horcruxes they have already destroyed.'''

    print("\nPOTTER STATUS:")

    if room == 'Snape\'s Office':
        print(f"• You are currently in {room}. ", end="")
    elif room == 'staircase to the dungeons' or room == 'first flight of stairs' or room == 'second flight of stairs':
        if moving == 'south':
            print(f"• You are currently going down the {room}. ", end="")
        else:
            print(f"• You are currently going up the {room}. ", end="")
    else:
        print(f"• You are currently in the {room}. ", end="")

    if len(directions) <= 2:
        print(f"You can only go ", end="")
        print(' or '.join(directions), end=". \n")
    else:
        print(f"You can go ", end="")
        print('{} or {}'.format(', '.join(directions[:-1]) + ',', directions[-1]), end=". \n")

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


def move_rooms(valid_directions, room_dict, horcrux, times, current_room):
    '''Moves the player to the specified room, or allows them to see their progress.'''

    while True:
        decision = input(f"[ Which way would you like to go? You may also type 'status' to see more info on your progress. ] \n").lower()

        if decision in valid_directions:

            direction = decision
            new_room = room_dict.get(direction)

            current_room = new_room
            room_dict = list_of_rooms.get(current_room)
            times = room_dict.get('times')


            if new_room == 'Snape\'s Office':
                if times == 0:
                    print(f"\n[ You move into {new_room}. ]")
                else:
                    (f"\n[ You return to {new_room}. ]")
            elif new_room == 'staircase to the dungeons' or new_room == 'first flight of stairs' or new_room == 'second flight of stairs':
                if direction == 'south':
                    if times == 0:
                        print(f"\n[ You move down the {new_room}. ]")
                    else:
                        print(f"\n[ You move down the {new_room} once again. ]")
                elif direction == 'north':
                    if times == 0:
                        print(f"\n[ You move up the {new_room}. ]")
                    else:
                        print(f"\n[ You move up the {new_room} once more. ]")
                else:
                    if times == 0:
                        print(f"\n[ You move to the {new_room}. ]")
                    else:
                        print(f"\n[ You move back to the {new_room} once more. ]")
            elif new_room == 'Entrance Hall':
                print(f"\n[ You move back to the {new_room}. ]")
            elif new_room == 'Gryffindor Common Room':
                print(f"\n[ You move into to the {new_room}. ]")
                win_lose(destroyed_horcruxes)
            else:
                if times == 0:
                    print(f"\n[ You move into the {new_room}. ]")
                else:
                    print(f"\n[ You move back into the {new_room}. ]")
            return new_room, times

        elif decision == 'status':
            player_status(current_room, horcrux, direction, valid_directions)

        else:
            print("\n[ That is an invalid input. Please try again. ]")


def win_lose(destroyed_horcruxes):
    '''Checks if player has destroyed all the necessary items in order to win the game.'''

    if len(destroyed_horcruxes) == 6:
        print("[ You win! ]")
        exit()
    else:
        print("[ You lose! ]")
        exit()


# TODO: Welcome screen.

# Testing values.
current_room = 'Entrance Hall'
destroyed_horcruxes = []

def main(current_room):
    '''Main loop function of the game.'''

    while True:
        # TODO: Try to move some of these outside so I can stop passing them all through.

        room_dict = list_of_rooms.get(current_room)
        options = list(room_dict.keys())
        valid_directions = options[:len(options) - 3]
        room_horcrux = room_dict.get('horcrux')
        times = room_dict.get('times')

        nav(valid_directions, room_horcrux)

        if room_horcrux != 'none' and room_horcrux not in destroyed_horcruxes:
            yn = input(f"[ Would you like to destroy it? Yes or no. ]\n").lower()
            if yn == 'yes':
                print(f"You have destroyed {room_horcrux}.")
                destroyed_horcruxes.append(room_horcrux)
            elif yn == 'no':
                current_room, times = move_rooms(valid_directions, room_dict, room_horcrux, times, current_room)
                times += 1
                room_dict.update({'times': times})
            else:
                print("[ That is an invalid input. Please try again. ]\n")
        else:
            current_room, times = move_rooms(valid_directions, room_dict, room_horcrux, times, current_room)
            times += 1
            room_dict.update({'times': times})

print(logo, "\n \n")
main(current_room)
