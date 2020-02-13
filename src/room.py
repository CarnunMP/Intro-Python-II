# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap

class Room:
    def __init__(self, name, description, n_to = None, e_to = None, s_to = None, w_to = None, item_list = []):
        self.name = name
        self.description = description
        
        self.n_to = n_to
        self.e_to = e_to
        self.s_to = s_to
        self.w_to = w_to

        self.item_list = item_list
    
    def enter(self, user_input):
        if user_input == 'n':
            return self.n_to
        if user_input == 'e':
            return self.e_to
        if user_input == 's':
            return self.s_to
        if user_input == 'w':
            return self.w_to

    def get_available_directions(self):
        available_directions = []

        available_directions.append("'n' for North") if self.n_to != None else None
        available_directions.append("'e' for East") if self.e_to != None else None
        available_directions.append("'s' for South") if self.s_to != None else None
        available_directions.append("'w' for West") if self.w_to != None else None

        return available_directions

    def print_items(self):
        print("Items in this room:")

        for i, item in enumerate(self.item_list):
            print(textwrap.fill(f" - Item [{i + 1}]: {item}"))
        
        print("")
