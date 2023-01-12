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
        'times': 0,
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

# TODO: Finish up or down stairs, test to make sure all directions work as intended.
def dialogue(current_room, direction, times, room_horcrux):
    '''Unique NPC dialogue dependent on current room, number of times visited, and if horcrux has been destroyed or not.'''

    if current_room == 'Entrance Hall':
        if times == 0:
            print("\n// Dialogue for Entrance Hall, first time, to be added later. //\n")
        else:
            print("\n// Dialogue for Entrance Hall, revisited, to be added later. //\n")
    elif current_room == 'staircase to the dungeons':
        if times == 0:
            print("\n// Dialogue for dungeon staircase, first time, to be added later. //\n")
        elif times == 1:
            print("\n// Dialogue for dungeon staircase, revisited, going UP, still another room to be explored, to be added later. //\n")
        else:
            if direction == 'west' or direction == 'east':
                print("\n// Dialogue for dungeon staircase, revisited, going UP, to be added later. //\n")
            else:
                print("\n// Dialogue for dungeon staircase, revisited, going DOWN, to be added later. //\n")
    elif current_room == 'Slytherin Common Room':
        if times == 0:
            print("\n// Dialogue for Slytherin Common Room, first time, to be added later. //\n")
        else:
            if room_horcrux in destroyed:
                print("\n// Dialogue for Slytherin Common Room, revisited, horcrux destroyed, to be added later. //\n")
            else:
                print("\n// Dialogue for Slytherin Common Room, revisited, horcrux NOT destroyed, to be added later. //\n")
    elif current_room == 'Snape\'s Office':
        if times == 0:
            print("\n// Dialogue for Snape\'s Office, first time, to be added later. //\n")
        else:
            if room_horcrux in destroyed:
                print("\n// Dialogue for Snape\'s Office, revisited, horcrux destroyed, to be added later. //\n")
            else:
                print("\n// Dialogue for Snape\'s Office, revisited, horcrux NOT destroyed, to be added later. //\n")
    elif current_room == 'Ravenclaw Common Room':
        if times == 0:
            print("\n// Dialogue for Ravenclaw Common Room, first time, to be added later. //\n")
        else:
            print("\n// Dialogue for Ravenclaw Common Room, revisited, to be added later. //\n")
    elif current_room == 'kitchen':
        print(times)
        if times == 0:
            print("\n// Dialogue for kitchen, first time, to be added later. //\n")
        else:
            print("\n// Dialogue for kitchen, revisited, to be added later. //\n")
    elif current_room == 'Hufflepuff Common Room':
        if times == 0:
            print("\n// Dialogue for Hufflepuff Common Room, first time, to be added later. //\n")
        else:
            if room_horcrux in destroyed:
                print("\n// Dialogue for Hufflepuff Common Room, revisited, horcrux destroyed, to be added later. //\n")
            else:
                print(
                    "\n// Dialogue for Hufflepuff Common Room, revisited, horcrux NOT destroyed, to be added later. //\n")
    elif current_room == 'first flight of stairs':
        if times == 0:
            print("\n// Dialogue for first flight of stairs, first time, to be added later. //\n")
        else:
            print("\n// Dialogue for first flight of stairs, revisited, to be added later. //\n")
    elif current_room == 'second floor girl\'s bathroom':
        if times == 0:
            print("\n// Dialogue for second floor girl\'s bathroom, first time, to be added later. //\n")
        else:
            print("\n// Dialogue for second floor girl\'s bathroom, revisited, to be added later. //\n")
    elif current_room == 'Chamber of Secrets':
        if times == 0:
            print("\n// Dialogue for Chamber of Secrets, first time, to be added later. //\n")
        else:
            if room_horcrux in destroyed:
                print("\n// Dialogue for Chamber of Secrets, revisited, horcrux destroyed, to be added later. //\n")
            else:
                print("\n// Dialogue for Chamber of Secrets, revisited, horcrux NOT destroyed, to be added later. //\n")
    elif current_room == 'second flight of stairs':
        if times == 0:
            print("\n// Dialogue for second flight of stairs, first time, to be added later. //\n")
        else:
            print("\n// Dialogue for second flight of stairs, revisited, to be added later. //\n")
    elif current_room == 'Room of Requirement':
        if times == 0:
            print("\n// Dialogue for Room of Requirement, first time, to be added later. //\n")
        else:
            if room_horcrux in destroyed:
                print("\n// Dialogue for Room of Requirement, revisited, horcrux destroyed, to be added later. //\n")
            else:
                print("\n// Dialogue for Room of Requirement, revisited, horcrux NOT destroyed, to be added later. //\n")
    elif current_room == 'Gryffindor Common Room':
        if len(destroyed) == 6:
            print("\n// Battle dialogue - win, to be added later. //\n")
        else:
            print("\n// Battle dialogue - lose, to be added later. //\n")
        win_lose(destroyed)
    elif current_room == 'Headmaster\'s Office':
        if times == 0:
            print("\n// Dialogue for Headmaster\'s Office, first time, to be added later. //\n")
        else:
            if room_horcrux in destroyed:
                print("\n// Dialogue for Headmaster\'s Office, revisited, horcrux destroyed, to be added later. //\n")
            else:
                print("\n// Dialogue for Headmaster\'s Office, revisited, horcrux NOT destroyed, to be added later. //\n")


def player_status(current_room, room_horcrux, direction, valid_directions):
    '''Displays the player's current room, the horcrux in their current room if they have yet to destroy it, and the list of horcruxes they have already destroyed.'''

    print("\nPOTTER STATUS:")

    if current_room == 'Snape\'s Office':
        print(f"• You are currently in {current_room}. ", end="")
    elif current_room == 'staircase to the dungeons' or current_room == 'first flight of stairs' or current_room == 'second flight of stairs':
        if direction == 'south':
            print(f"• You are currently going down the {current_room}. ", end="")
        else:
            print(f"• You are currently going up the {current_room}. ", end="")
    else:
        print(f"• You are currently in the {current_room}. ", end="")

    if len(valid_directions) <= 2:
        print(f"You can only go ", end="")
        print(' or '.join(valid_directions), end=". \n")
    else:
        print(f"You can go ", end="")
        print('{} or {}'.format(', '.join(valid_directions[:-1]) + ',', valid_directions[-1]), end=". \n")

    if len(destroyed) == 0:
        print(f"• You have yet to destroy any horcruxes.")
    elif len(destroyed) == 1:
        print(f"• You have only destroyed {destroyed[0]} so far.")
    else:
        print(f"• The horcruxes you have already destroyed are ", end='')
        print('{} and {}.'.format(', '.join(destroyed[:-1]) + ',', destroyed[-1]))

    x = 6 - len(destroyed)

    if x == 0:
        print(f"• There are no horcruxes remaining.\n")
    elif x == 1:
        print(f"• There is {x} horcrux remaining.\n")
    else:
        print(f"• There are {x} horcruxes remaining.\n")


def nav(valid_directions, room_horcrux):
    '''Displays all input options to the player.'''

    if len(valid_directions) <= 2:
        print(f"[ From your current room, you can only go ", end="")
        print(' or '.join(valid_directions), end=". ")
    else:
        print(f"[ From your current room, you can go ", end="")
        print('{} or {}.'.format(', '.join(valid_directions[:-1]) + ',', valid_directions[-1]), end=" ")

    if room_horcrux == 'none':
        print("As there are no horcruxes in this room, it seems going elsewhere is your only option. ]")
    elif room_horcrux in destroyed:
        print("As you have already destroyed the horcrux in this room, it seems going elsewhere is your only option. ]")
    else:
        length = ["short", "quick", "lengthy", "difficult", "long", "tiring"]
        print(f"After a {random.choice(length)} search, you find that the horcrux in this room is {room_horcrux}. ]")


def move_rooms(direction, valid_directions, room_dict, room_horcrux, times, current_room):
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
            else:
                if times == 0:
                    print(f"\n[ You move into the {new_room}. ]")
                else:
                    print(f"\n[ You move back into the {new_room}. ]")
            return new_room, times

        elif decision == 'status':
            player_status(current_room, room_horcrux, direction, valid_directions)

        else:
            print("\n[ That is an invalid input. Please try again. ]")

def destroy_horcrux(direction, valid_directions, room_dict, room_horcrux, times, current_room):
    '''Asks player if they want to destroy a horcrux or continue on with it undestroyed.'''

    yn = input(f"[ Would you like to destroy it? Yes or no. ]\n").lower()

    if yn == 'yes':
        print(f"You have destroyed {room_horcrux}.\n")
        destroyed.append(room_horcrux)
        return current_room, times
    elif yn == 'no':
        current_room, times = move_rooms(direction, valid_directions, room_dict, room_horcrux, times, current_room)
        return current_room, times
    else:
        print("[ That is an invalid input. Please try again. ]\n")
        return current_room, times


def win_lose(destroyed):
    '''Checks if player has destroyed all the necessary items in order to win the game.'''

    if len(destroyed) == 6:
        print("[ You win! ]")
        exit()
    else:
        print("[ You lose! ]")
        exit()


def main(current_room, direction):
    '''Main loop function of the game.'''

    while True:
        room_dict = list_of_rooms.get(current_room)
        options = list(room_dict.keys())
        valid_directions = options[:len(options) - 3]
        room_horcrux = room_dict.get('horcrux')
        times = room_dict.get('times')

        print(current_room)
        print(times)

        nav(valid_directions, room_horcrux)
        if room_horcrux != 'none' and room_horcrux not in destroyed:
            current_room, times = destroy_horcrux(direction, valid_directions, room_dict, room_horcrux, times, current_room)
        else:
            current_room, times = move_rooms(direction, valid_directions, room_dict, room_horcrux, times, current_room)
        dialogue(current_room, direction, times, room_horcrux)
        times += 1
        room_dict.update({'times': times})

# Default starting values.
current_room = 'Entrance Hall'
destroyed = []
direction = 'none'

print(logo, "\n \n")

# TODO: Welcome screen.

main(current_room, direction)
