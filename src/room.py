# Implement a class to hold room information. This should have name and
# description attributes.


"""
Add the ability to add items to rooms.

The Room class should be extended with a list that holds the Items that are currently in that room.

Add functionality to the main loop that prints out all the items that are visible to the player when they are in that room.

"""


class Room: 
    def __init__(self, name, description):
        self.name = name,
        self.description = description
        self.items = []

    def __repr__(self):
        room_string = f"{self.name}\n\n"
        room_string = f"{self.description}"
        return room_string

    # def __str__(self):
    #     list_of_items = .join(str(x) for x in self.items)
    #     return f'Room: {self.name}, {self.description}\n 
    #              items: {list_of_items}'

    def add_an_item(self, item):
        self.items.append(item)
        print(f'{item.desc} is now available')

    def remove_an_item(self, item):
        self.items.remove(item)
        print(f'{item.desc} is not available')