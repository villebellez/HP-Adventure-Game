from art import logo
from rooms import list_of_rooms, move_rooms, update, dialogue, destroy_horcrux, win_lose
from player import nav

destroyed = []

def welcome_message():
    '''Prints the game logo, objective, and first set of NPC dialogue'''

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
    print('As Harry, Ron, and Hermione step into Hogwarts, they find themselves in the Entrance Hall. '
          'Hermione looks to her friend, wand held tightly in her hand as she says, "We\'re with you to the end, Harry. '
          'We\'ll follow your lead."\n'
          '"Although we\'d appreciate if you didn\'t get us murdered, mate, so maybe try to pick the right way?" '
          'Ron half-jokes, prompting Hermione to shoot him an unamused look.\n')

def main():
    '''Main function of the game.'''

    welcome_message()

    current_room = 'Entrance Hall'
    previous_room = None
    direction = None

    while True:
        room_dict, valid_directions, room_horcrux, times = update(current_room)

        dialogue(current_room, times, room_horcrux, previous_room, destroyed)
        nav(valid_directions, room_horcrux, current_room, destroyed)

        if room_horcrux != 'none' and room_horcrux not in destroyed:
            current_room, times, previous_room = destroy_horcrux(direction, current_room, previous_room, destroyed)
        else:
            current_room, times, previous_room = move_rooms(direction, valid_directions, room_dict, current_room, destroyed)
        times += 1
        room_dict.update({'times': times})


if __name__ == "__main__":
    main()
