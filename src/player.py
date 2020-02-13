# Write a class to hold player information, e.g. what room they are in
# currently.
import textwrap

class Player:
    def __init__(self, name, current_room, inventory = []):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def print_inventory(self):
        if len(self.inventory) == 0:
            print("Your inventory is empty.\n")
        else:
            print(f"Inventory:")

            for i, item in enumerate(self.inventory):
                print(textwrap.fill(f" - Item [{i + 1}]: {item}"))
            
            print("")