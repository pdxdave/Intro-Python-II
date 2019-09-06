# Write a class to hold player information, e.g. what room they are in
# currently.
# Write a class to hold player information, e.g. what room they are in
# currently.
"""
Add capability to add Items to the player's inventory. 

The inventory can also be a list of items "in" the player, similar to how Items can be in a Room.

Players should have a name and current_room attributes

"""
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        self.items.remove(item)