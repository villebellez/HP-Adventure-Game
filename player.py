import random

def status(current_room, direction, valid_directions, destroyed):
    '''Displays the player's current room, available directions,
    the list of horcruxes they have already destroyed, and the amount of horcruxes remaining.'''

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


def nav(valid_directions, room_horcrux, current_room, destroyed):
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
    elif current_room == 'Snape\'s Office':
        print(f"Unfortunately, you have stumbled upon Voldemort's snake, Nagini, devouring its next meal. Should you act quickly, "
              f"you may be able to destroy it before it notices you. ]")
    else:
        length = ["short", "quick", "lengthy", "difficult", "long", "tiring"]
        print(f"After a {random.choice(length)} search, you find that the horcrux in this room is {room_horcrux}. ]")

