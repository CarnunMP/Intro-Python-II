from room import Room
from player import Player
from item import Item
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

### Items:
room['outside'].item_list = [Item("Stick", "It's brown and sticky."), Item("Newspaper", "It appears to be black and white and read all over.")]
room['foyer'].item_list = []
room['overlook'].item_list = []
room['narrow'].item_list = []
room['treasure'].item_list = []

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

print("- - - - - - - - - - - - - - - - - - - - - - \n")

display_inventory = False

while current_room_key != 'QUIT':
    current_room = room[current_room_key]
    number_of_items = len(current_room.item_list)

    print(f'You are in {current_room.name}.')
    print(textwrap.fill(current_room.description) + "\n")
    current_room.print_items()

    if display_inventory : player.print_inventory()

    prompt = "> Where would you like to go? "

    prompt_directions = ""
    available_directions = current_room.get_available_directions()
    if len(available_directions) == 1:
        prompt_directions = f"> Enter {available_directions[0]}.\n"
    elif len(available_directions) == 2:
        prompt_directions = f"> Enter {available_directions[0]} or {available_directions[1]}.\n"
    elif len(available_directions) == 3:
        prompt_directions = f"> Enter {available_directions[0]}, {available_directions[1]}, or {available_directions[2]}.\n"
    else:
        prompt_directions = f"> Enter {available_directions[0]}, {available_directions[1]}, {available_directions[2]}, or {available_directions[4]}.\n"
    prompt += prompt_directions

    prompt_items = "> Alternatively, enter "
    for i, item in enumerate(current_room.item_list):
        prompt_items += f"'{i + 1}' to pick up the {item.name} or "
    prompt_items = prompt_items[:-4] + ".\n"
    prompt += textwrap.fill(prompt_items if len(current_room.item_list) != 0 else "")

    prompt += f"\n> Or, enter 'i' to "
    prompt += "hide " if display_inventory else "show "
    prompt += "your inventory.\n"
    
    prompt += "> (Or 'q' to quit.) \n"
    prompt += ">>> "

    user_input = input(prompt).lower()

    print("- - - - - - - - - - - - - - - - - - - - - - \n")

    user_input_array = user_input.split(" ")
    # print(user_input_array)

    try:
        if user_input == 'q':
            print("> You have quit the game. Bye!")
            current_room_key = 'QUIT'
        elif user_input == 'i':
            display_inventory = False if display_inventory else True
        elif len(user_input_array) == 2:
            try:
                if user_input_array[0] == 'get' or user_input_array[0] == 'take':
                    item_name_input = user_input_array[1][:1].upper() + user_input_array[1][1:]
                    # print(item_name_input)

                    [item] = [x for x in current_room.item_list if x.name == item_name_input]
                    current_room.item_list.remove(item)
                    player.inventory.append(item)
                elif user_input_array[0] == 'drop':
                    None
            except:
                None
            # item = current_room.item_list.pop(int(user_input) - 1)
            # player.inventory.append(item)
        elif user_input != 'n' and user_input != 'e' and user_input != 's' and user_input != 'w':
            print("***Please enter one of the cardinal directions.***\n")
        else:
                next_room_key = current_room.enter(user_input)
                # If this next line fails...
                current_room = room[next_room_key]
                # ... this never gets called:
                current_room_key = next_room_key
    except KeyError:
        print("***Please choose an available direction for this room.***\n")
    # except ValueError:
    #     print("***Invalid input. Please try again.***\n")


