from player import status


list_of_rooms = {
    'Entrance Hall': {
        'north': 'first flight of stairs',
        'south': 'staircase to the dungeons',
        'east': 'kitchen',
        'west': 'Ravenclaw Common Room',
        'horcrux': 'none',
        'times': 0,
    },
    'staircase to the dungeons': {
        'north': 'Entrance Hall',
        'east': 'Slytherin Common Room',
        'west': 'Snape\'s Office',
        'horcrux': 'none',
        'times': 0,
    },
    'Slytherin Common Room': {
        'west': 'staircase to the dungeons',
        'horcrux': 'Marvolo Gaunt\'s Ring',
        'times': 0,
    },
    'Snape\'s Office': {
        'east': 'staircase to the dungeons',
        'horcrux': 'Nagini',
        'times': 0,
    },
    'Ravenclaw Common Room': {
        'east': 'Entrance Hall',
        'horcrux': 'none',
        'times': 0,
    },
    'kitchen': {
        'east': 'Hufflepuff Common Room',
        'west': 'Entrance Hall',
        'horcrux': 'none',
        'times': 0,
    },
    'Hufflepuff Common Room': {
        'west': 'kitchen',
        'horcrux': 'Helga Hufflepuff\'s Cup',
        'times': 0,
    },
    'first flight of stairs': {
        'north': 'second flight of stairs',
        'east': 'second floor girl\'s bathroom',
        'south': 'Entrance Hall',
        'horcrux': 'none',
        'times': 0,
    },
    'second floor girl\'s bathroom': {
        'west': 'first flight of stairs',
        'south': 'Chamber of Secrets',
        'horcrux': 'none',
        'times': 0,
    },
    'Chamber of Secrets': {
        'north': 'second floor girl\'s bathroom',
        'horcrux': 'Tom Riddle\'s Diary',
        'times': 0,
    },
    'second flight of stairs': {
        'north': 'Headmaster\'s Office',
        'east': 'Room of Requirement',
        'west': 'Gryffindor Common Room',
        'horcrux': 'none',
        'times': 0,
    },
    'Room of Requirement': {
        'west': 'second flight of stairs',
        'horcrux': 'Rowena Ravenclaw\'s Diadem',
        'times': 0,
    },
    'Gryffindor Common Room': {
        'east': 'second flight of stairs',
        'horcrux': 'none',
        'times': 0,
    },
    'Headmaster\'s Office': {
        'south': 'second flight of stairs',
        'horcrux': 'Salazar Slytherin\'s Locket',
        'times': 0,
    }
}

def update(current_room):
    '''Updates some of the frequently changing variables when the player changes rooms.'''

    room_dict = list_of_rooms.get(current_room)
    options = list(room_dict.keys())
    valid_directions = options[:len(options) - 2]
    room_horcrux = room_dict.get('horcrux')
    times = room_dict.get('times')

    return room_dict, valid_directions, room_horcrux, times


def move_rooms(direction, valid_directions, room_dict, current_room, destroyed):
    '''Moves the player to the specified room, or allows them to see their progress.'''

    while True:
        decision = input(f"[ Which way would you like to go? You may also type 'status' to see more info on your progress. ] \n").lower()

        if decision in valid_directions:

            direction = decision
            new_room = room_dict.get(direction)
            previous_room = current_room
            current_room = new_room

            room_dict, valid_directions, room_horcrux, times = update(current_room)

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
                    print(f"\n[ You return to the {current_room}. ]")
            return current_room, times, previous_room

        elif decision == 'status':
            status(current_room, direction, valid_directions, destroyed)

        else:
            print("\n[ That is an invalid input. Please try again. ]")


def dialogue(current_room, times, room_horcrux, previous_room,destroyed):
    '''Unique NPC dialogue dependent on current room, number of times visited, and if horcrux has been destroyed or not.'''

    if current_room == 'Entrance Hall' and times != 0:
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
            print('\n"Was kind of expecting the staircases to change on us," Ron says, surprised by the straightforward path.\n'
                  '"Maybe the castle is trying to help us out," Hermione responds, and Harry is apt to agree.\n')
        elif previous_room == "Room of Requirement" or previous_room == "Headmaster\'s Office":
            if gryffindor_times == 0 or headmaster_times == 0 or requirement_times == 0:
                print('\n"I don\'t think we should head back downstairs until we\'ve checked out every room," Hermione reminds Harry, '
                      'but Ron shakes his head.\n'
                      '"You don\'t know what room You-Know-Who is lurking in! Harry\'s just being smart."\n')
            else:
                print('\n"Should we head back downstairs then?" asks Ron."\n')
        elif previous_room == "first flight of stairs":
            if gryffindor_times == 0 or headmaster_times == 0 or requirement_times == 0:
                print(
                    '\n"I think it\'s a good idea we\'re coming back up here," Hermione tells the group. "We really should check out '
                    'every room before moving on. The horcruxes could be anywhere."\n'
                    '"Yeah, but so could You-Know-Who," Ron interjects, and Harry silently agrees.\n')
            else:
                print('\n"You feeling okay, Harry?" Ron asks, no doubt wondering if his friend is just as nervous as he is. '
                      'Harry nods, but his expression is a little more strained than usual."\n')


    elif current_room == 'Room of Requirement':
        if times == 0:
            print('\n"Finding a horcrux in this mess is going to be impossible," Ron notes, looking at the piles upon piles of '
                  'lost or stashed items that have accumulated over the years.\n'
                  '"Oh, don\'t be so negative, Ronald," Hermione responds. "I\'m sure it won\'t take that long."\n')
        else:
            if room_horcrux in destroyed:
                print('\n"Nothing left to do in here with the diadem destroyed," Hermione says. "Let\'s head out."\n')
            else:
                print('\n"We have to destroy the diadem this time, Harry," Hermione reminds her friend. "We can\'t defeat Voldemort '
                      'without all of his horcruxes being destroyed first."\n')

    elif current_room == 'Gryffindor Common Room':
        if len(destroyed) == 6:
            print('\nThe trio enters their old Common Room, only to be greeted by the smiling face of their enemy.\n'
                  '"Ah, Harry... I knew you would come," Voldemort drawls as he pulls out his wand. Although they are scared, '
                  'Ron and Hermione stand tall next to their friend.\n'
                  '"Too bad for you, we came prepared!" shouts Ron, but Voldemort just laughs as he raises his wand menacingly.\n'
                  'However, when Voldemort casts his Killing Curse, Harry counters it with a spell of his own, and their twin wand cores connect the two spells.\n'
                  'With the blood pumping in his ears, Harry can hardly hear the triumphant shout of his friends as he finally overpowers Voldemort, and saves the day!\n')
        else:
            print('\nThe trio enters their old Common Room, only to be greeted by the smiling face of their enemy.\n'
                  '"Ah, Harry... I knew you would come," Voldemort drawls as he pulls out his wand. Hermione grabs Harry\'s arm in fear. \n'
                  'They weren\'t ready, and they did not come prepared. Voldemort raises his arm, and Ron winces.\n'
                  '"Harry Potter... prepare to die."\n')
        win_lose(destroyed)

    elif current_room == 'Headmaster\'s Office':
        if times == 0:
            print('\n"I wish Dumbledore was here," Ron laments, and Harry exhales a small, saddened breath next to him.\n'
                  '"He\'ll always be with us," Hermione reminds them, and Harry finds himself hoping that is true.\n')
        else:
            if room_horcrux in destroyed:
                print('\n"Putting Slytherin\'s locket in here... what a wank," Ron swears.\n'
                      '"Ron!" Hermione protests, but Ron isn\'t apologetic in the slightest, and Harry silently agrees with the sentiment.\n')
            else:
                print('\n"We need to destroy the locket this time, Harry. It only adds to Voldemort\'s strength," Hermione reminds her friend.\n')

def destroy_horcrux(direction, current_room, previous_room, destroyed):
    '''Asks player if they want to destroy a horcrux or continue on with it undestroyed.'''

    room_dict, valid_directions, room_horcrux, times = update(current_room)

    yn = input(f"[ Would you like to destroy it? Yes or no. ]\n").lower()

    if yn == 'yes':
        print(f"[ You have destroyed {room_horcrux}. ]")
        destroyed.append(room_horcrux)
    elif yn == 'no':
        current_room, times, previous_room = move_rooms(direction, valid_directions, room_dict, current_room, destroyed)
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
