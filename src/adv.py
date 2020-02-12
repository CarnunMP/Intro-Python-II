from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

### I didn't like the above implementation. Went for the following instead:
room['outside'].n_to = 'foyer'
room['foyer'].s_to = 'outside'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'
room['overlook'].s_to = 'foyer'
room['narrow'].w_to = 'foyer'
room['narrow'].n_to = 'treasure'
room['treasure'].s_to = 'narrow'

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
current_room_key = 'outside'
player = Player('Carnun', current_room_key)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while current_room_key != 'QUIT':
    current_room = room[current_room_key]

    print("- - - - - - - - - - - - - - - - - - - - - - \n")
    print(f'You are in {current_room.name}.')
    print(textwrap.fill(current_room.description))

    # Todo: make prompt dynamic!
    available_directions = current_room.get_available_directions()
    prompt_middle = ""
    if len(available_directions) == 1:
        prompt_middle = f"Enter {available_directions[0]}."
    elif len(available_directions) == 2:
        prompt_middle = f"Enter {available_directions[0]} or {available_directions[1]}."
    elif len(available_directions) == 3:
        prompt_middle = f"Enter {available_directions[0]}, {available_directions[1]}, or {available_directions[2]}."
    else:
        prompt_middle = f"Enter {available_directions[0]}, {available_directions[1]}, {available_directions[2]}, or {available_directions[4]}."
    prompt = f"> Where would you like to go? {prompt_middle} (Or enter 'q' to quit.) \n"
    user_input = input(prompt).lower()

    if user_input == 'q':
        print("You have quit the game. Bye!")
        current_room_key = 'QUIT'
    elif user_input != 'n' and user_input != 'e' and user_input != 's' and user_input != 'w':
        print("Please enter one of the cardinal directions. (Or enter 'q' to quit.)")
    else:
        try:
            next_room_key = current_room.enter(user_input)
            # If this next line fails...
            current_room = room[next_room_key]
            # ... this never gets called:
            current_room_key = next_room_key
        except KeyError:
            print("***Please choose an available direction for this room.***")


