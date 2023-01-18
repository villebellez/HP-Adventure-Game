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

# TODO: Finish dialogue, make sure 'else' statements aren't executed if a horcrux room has beeen visited but it hasn't been destroyed.
def dialogue(current_room, direction, times, room_horcrux, previous_room):
    '''Unique NPC dialogue dependent on current room, number of times visited, and if horcrux has been destroyed or not.'''

    if current_room == 'Entrance Hall':
        if times == 0:
            print('As Harry, Ron, and Hermione step into Hogwarts, they find themselves in the Entrance Hall. '
                  'Hermione looks to her friend, wand held tightly in her hand as she says, "We\'re with you to the end, Harry. '
                  'We\'ll follow your lead."\n'
                  '"Although we\'d appreciate if you didn\'t get us murdered, mate, so maybe try to pick the right way?" '
                  'Ron half-jokes, prompting Hermione to shoot him an unamused look.\n')
        else:
            print('\n"Well, we know nothing is in here," Ron says, looking over at Harry for guidance. "Where to next?"\n')

    elif current_room == 'staircase to the dungeons':

        slytherin = list_of_rooms.get('Slytherin Common Room')
        slytherin_times = slytherin.get('times')

        snape = list_of_rooms.get('Snape\'s Office')
        snape_times = snape.get('times')

        if times == 0:
            print('\n"Do we really have to come down here? Nothing good ever happens in the dungeons," Ron complains.\n'
                  '"We need to explore every possibility, Ron," Hermione reminds him, but Ron still doesn\'t look happy.\n')
        elif previous_room == "Slytherin Common Room" or previous_room == "Snape\'s Office":
            if snape_times == 0 or slytherin_times == 0:
                print('\n"We should probably check out the other room before we go back upstairs," Hermione reminds everyone.\n'
                      'Ron gulps. "But You-Know-Who could be in there."\n'
                      '"True, every room is a gamble, but what other choice do we have?"\n')
            else:
                print('\n"I don\'t think there\'s anything left for us to explore down here," Hermione mentions as Ron nods quickly in agreement. \n')
        elif previous_room == "Entrance Hall":
            if snape_times == 0 or slytherin_times == 0:
                print('\n"Back to the dungeons AGAIN?" Ron groans.\n'
                      '"We still have another room to explore down there, Ron," Herminone reminds him. "It\'s best not to leave any stone unturned." \n'
                      '"Yeah, unless You-Know-Who is waiting for us under the stone," Ron mutters miserably.\n')
            else:
                print('\n"There\'s nothing else down here, Harry," Hermione reminds her friend. "We should probably go back upstairs."\n')

    elif current_room == 'Slytherin Common Room':
        if times == 0:
            print('\n"There\'s definitely something here," Ron assures Harry with confidence. "If You-Know-Who didn\'t '
                  'hide something in his old Common Room, I\'ll eat my foot." \n')
        else:
            if room_horcrux in destroyed:
                print('\n"The ring\'s been destroyed - no point hanging around here anymore," Ron says. "Where to next?"\n')
            else:
                print('\n"We\'re definitely going to destroy the ring this time, right?" Ron prompts. "Because I don\'t want to be down'
                      ' here any longer than I have to."\n')

    elif current_room == 'Snape\'s Office':
        if times == 0:
            print('\nWhen the trio enter the room, they are greeted by a horrible sight. Professor Snape\'s lifeless body '
                  'is being used as snake food, and it prompts Hermione to let out a quiet gasp of horror.\n')
        else:
            if room_horcrux in destroyed:
                print('\nHermione looks at the lifeless body of their former professor, the corners of her mouth turning downward.\n'
                      '"You can\'t possibly feel sorry for the bloke," Ron responds incredulously. "He was a traitor! He killed Dumbledore!"\n'
                      '"It was just a horrible way to die, that\'s all," Hermione responds quietly.\n')
            else:
                print('\n"WILL YOU JUST KILL IT BEFORE IT KILLS US?!" Ron shrieks. "Stop tempting fate!"\n')

    elif current_room == 'Ravenclaw Common Room':
        if times == 0:
            print('\n"I can\'t believe Ravenclaws have to answer a riddle any time they want to go back to their room. Can you imagine '
                  'trying to make your brain work when you\'re coming back from the library dead tired? I\'d just sleep on the floor outside the door."\n'
                  '"The riddle really wasn\'t that hard, Ron," Hermione insists. "You just need to give it more than 5 seconds of your attention." \n'
                  'Ron rolls his eyes.\n')
        else:
            print('\n"There wasn\'t anything in here, remember?" Ron reminds Harry, who nods silently.\n'
                  '"Strange," Hermione mutters. "I wonder where the diadem is then..."\n')

    elif current_room == 'kitchen':
        if times == 0:
            print('\n"Excellent, I could use a snack," Ron says, but before he can get anywhere, there\'s a hand on his arm.\n'
                  '"Will you stop thinking with your stomach?" Hermione lectures. "We have to destroy these horcruxes! '
                  'Come on, the Hufflepuff Common Room is this way." She points east.\n')
        else:
            print('\n"Now can I have a snack?" Ron asks hopefully.\n'
                  '"No!"\n')

    elif current_room == 'Hufflepuff Common Room':
        if times == 0:
            print('\n"I wish our Common Room was right off the kitchen," Ron says with a sigh. Hermione rolls her eyes.\n'
                  '"Of course you do."\n')
        else:
            if room_horcrux in destroyed:
                print('\n"We\'ve destroyed the cup," Hermione says. "We should probably move on."\n')
            else:
                print('\n"I don\'t think we should wait again to destroy the cup," Hermione says to Harry with some urgency. '
                      '"We need to destroy these horcruxes as quickly as possible."\n')

    elif current_room == 'first flight of stairs':

        bathroom = list_of_rooms.get('second floor girl\'s bathroom')
        bathroom_times = bathroom.get('times')

        chamber = list_of_rooms.get('Chamber of Secrets')
        chamber_times = chamber.get('times')

        if times == 0:
            print('\n"The second floor... you\'re going to make us go into the girl\'s bathroom again, aren\'t you?" Ron asks, looking toward the east hesitantly. \n'
                  '"Of course he is," Hermione responds before Harry even has a chance to open his mouth. "How else do you think we\'ll get to the Chamber of Secrets?" \n'
                  'Ron wrinkles his nose. "Yeah, but... but Myrtle is probably in there."\n')
        elif previous_room == "second floor girl\'s bathroom" or previous_room == "Entrance Hall" or previous_room == "second flight of stairs":
            if bathroom_times == 0 or chamber_times == 0:
                print('\n"We really should explore all options on this floor before moving on, Harry," Hermione reminds her friend.\n')
            else:
                print('\n"Nothing left to explore on this floor," Ron says. "Let\'s keep moving."\n')

    elif current_room == 'second floor girl\'s bathroom':

        chamber = list_of_rooms.get('Chamber of Secrets')
        chamber_times = chamber.get('times')

        if times == 0:
            print('\nRon looks around, expecting Moaning Myrtle to peek her head out and lament about her death again, but all is quiet.\n'
                  '"Go on, Harry," Hermione encourages. "Say something in Parseltounge so we can go down to the Chamber."\n')
        elif chamber_times == 0:
            print('\n"We need to go down to the Chamber, Harry," Hermione presses. "The diary is still down there."\n')
        else:
            print('\n"We\'ve already been down to the Chamber, so there\'s nothing left for us here," Hermione says. '
                  '"Let\'s go back to the stairs."\n')

    elif current_room == 'Chamber of Secrets':
        if times == 0:
            print('\n"Appreciate you saving my sister and all, but I really wish you would have properly destroyed the diary '
                  'the first time around," Ron lightly complains as he dodges one very large snakeskin.\n')
        else:
            if room_horcrux in destroyed:
                print('\n"Let\'s get out of here," Ron encourages. "With the diary destroyed, there\'s no reason to stay down in this hole."\n')
            else:
                print('\n"You can\'t keep leaving the diary, Harry," Hermione scolds. "It needs to be destroyed."\n')

    elif current_room == 'second flight of stairs':

        gryffindor = list_of_rooms.get('Gryffindor Common Room')
        gryffindor_times = gryffindor.get('times')

        headmaster = list_of_rooms.get('Headmaster\'s Office')
        headmaster_times = headmaster.get('times')

        requirement = list_of_rooms.get('Room of Requirement')
        requirement_times = requirement.get('times')

        if times == 0:
            print('\n// Dialogue for second flight of stairs, first time, to be added later //\n')
        elif previous_room == "Room of Requirement" or previous_room == "Headmaster\'s Office":
            if gryffindor_times == 0 or headmaster_times == 0 or requirement_times == 0:
                print('\n// Dialogue for second flight of stairs, revisited, going DOWN, still another room to be explored, to be added later. //\n')
            else:
                print('\n// Dialogue for second flight of stairs, revisited, going DOWN, to be added later. //\n')
        elif previous_room == "first flight of stairs":
            if gryffindor_times == 0 or headmaster_times == 0 or requirement_times == 0:
                print(
                    '\n// Dialogue for second flight of stairs, revisited, going UP, other room to be explored, to be added later. //\n')
            else:
                print('\n// Dialogue for second flight of stairs, revisited, going UP, to be added later. //\n')


    elif current_room == 'Room of Requirement':
        if times == 0:
            print('\n// Dialogue for Room of Requirement, first time, to be added later. //\n')
        else:
            if room_horcrux in destroyed:
                print('\n// Dialogue for Room of Requirement, revisited, horcrux destroyed, to be added later. //\n')
            else:
                print('\n// Dialogue for Room of Requirement, revisited, horcrux NOT destroyed, to be added later. //\n')

    elif current_room == 'Gryffindor Common Room':
        if len(destroyed) == 6:
            print('\n// Battle dialogue - win, to be added later. //\n')
        else:
            print('\n// Battle dialogue - lose, to be added later. //\n')
        win_lose(destroyed)

    elif current_room == 'Headmaster\'s Office':
        if times == 0:
            print('\n// Dialogue for Headmaster\'s Office, first time, to be added later. //\n')
        else:
            if room_horcrux in destroyed:
                print('\n// Dialogue for Headmaster\'s Office, revisited, horcrux destroyed, to be added later. //\n')
            else:
                print('\n// Dialogue for Headmaster\'s Office, revisited, horcrux NOT destroyed, to be added later. //\n')


def player_status(current_room, room_horcrux, direction, valid_directions):
    '''Displays the player's current room, the horcrux in their current room if they have yet to destroy it,
    and the list of horcruxes they have already destroyed.'''

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


def nav(valid_directions, room_horcrux, current_room):
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


def move_rooms(direction, valid_directions, room_dict, room_horcrux, times, current_room, previous_room):
    '''Moves the player to the specified room, or allows them to see their progress.'''

    while True:
        decision = input(f"[ Which way would you like to go? You may also type 'status' to see more info on your progress. ] \n").lower()

        if decision in valid_directions:

            direction = decision
            new_room = room_dict.get(direction)
            previous_room = current_room
            current_room = new_room
            room_dict = list_of_rooms.get(current_room)
            times = room_dict.get('times')


            if current_room == 'Snape\'s Office':
                if times == 0:
                    print(f"\n[ You move into {current_room}. ]")
                else:
                    (f"\n[ You return to {current_room}. ]")
            elif current_room == 'staircase to the dungeons' or current_room == 'first flight of stairs' or current_room == 'second flight of stairs':
                if direction == 'south':
                    if times == 0:
                        print(f"\n[ You move down the {current_room}. ]")
                    else:
                        print(f"\n[ You move down the {current_room} once again. ]")
                elif direction == 'north':
                    if times == 0:
                        print(f"\n[ You move up the {current_room}. ]")
                    else:
                        print(f"\n[ You move up the {current_room} once more. ]")
                else:
                    if times == 0:
                        print(f"\n[ You move to the {current_room}. ]")
                    else:
                        print(f"\n[ You move back to the {current_room} once more. ]")
            else:
                if times == 0:
                    print(f"\n[ You move into the {current_room}. ]")
                else:
                    print(f"\n[ You move back into the {current_room}. ]")
            return current_room, times, previous_room

        elif decision == 'status':
            player_status(current_room, room_horcrux, direction, valid_directions)

        else:
            print("\n[ That is an invalid input. Please try again. ]")


def destroy_horcrux(direction, valid_directions, room_dict, room_horcrux, times, current_room, previous_room):
    '''Asks player if they want to destroy a horcrux or continue on with it undestroyed.'''

    yn = input(f"[ Would you like to destroy it? Yes or no. ]\n").lower()

    if yn == 'yes':
        print(f"[ You have destroyed {room_horcrux}. ]")
        destroyed.append(room_horcrux)
        return current_room, times, previous_room
    elif yn == 'no':
        current_room, times, previous_room = move_rooms(direction, valid_directions, room_dict, room_horcrux, times, current_room, previous_room)
        return current_room, times, previous_room
    else:
        print("[ That is an invalid input. Please try again. ]")
        return current_room, times, previous_room


def win_lose(destroyed):
    '''Checks if player has destroyed all the necessary items in order to win the game.'''

    if len(destroyed) == 6:
        print("[ You win! ]")
        exit()
    else:
        print("[ You lose! ]")
        exit()


def main():
    '''Main function of the game.'''

    # TODO: Mess around later and see if I can use global keyword for these to decrease clutter, and if I always need to pass a value for a function..
    # Default starting values.
    current_room = 'Entrance Hall'
    previous_room = 'none'
    direction = 'none'

    print(logo, "\n")
    print("> Harry Potter has just returned to Hogwarts to face Lord Voldemort in the final battle.\n"
          "> Luckily, although Voldemort may be evil, it seems as though he is not very bright, "
          "as he hid the six other peices of his soul in horcruxes around the castle.\n"
          "> With a little help from his friends Ron and Hermione, Harry must search the castle and destroy all six horcruxes "
          "before finding and facing his enemy in battle.\n"
          "> But watch out! If Harry comes face-to-face with Voldemort unprepared, the final battle will not have a happy ending. "
          "Are you prepared to step into Harry's shoes and save the wizarding world?\n"
          "\n                    __________________________________________________________________________________________"
          "_______________________________\n")

    while True:

        # Continuously updating variables.
        room_dict = list_of_rooms.get(current_room)
        options = list(room_dict.keys())
        valid_directions = options[:len(options) - 3]
        room_horcrux = room_dict.get('horcrux')
        times = room_dict.get('times')

        dialogue(current_room, direction, times, room_horcrux, previous_room)

        nav(valid_directions, room_horcrux, current_room)
        if room_horcrux != 'none' and room_horcrux not in destroyed:
            current_room, times, previous_room = destroy_horcrux(direction, valid_directions, room_dict, room_horcrux, times, current_room, previous_room)
        else:
            current_room, times, previous_room = move_rooms(direction, valid_directions, room_dict, room_horcrux, times, current_room, previous_room)
        times += 1
        room_dict.update({'times': times})

destroyed = []

if __name__ == "__main__":
    main()
