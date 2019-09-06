from room import Room
from player import Player

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

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['outside'].w_to = room['treasure']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['outside'].w_to = room['overlook']
room['outside'].e_to = room['treasure']
#
# Main
#


test1 = True

player = Player('Rambo', room['outside'])
print("current room", room['outside'])

while test1 != False:
    moron = input("->")
    if moron == 'n' and player.current_room.n_to is not None:
        player.current_room = player.current_room.n_to
        print(player.current_room)
        # return player
    elif moron == 's' and player.current_room.s_to is not None:
        player.current_room = player.current_room.s_to
        print(player.current_room)
        # return player
    elif moron == 'e' and player.current_room.e_to is not None:
        player.current_room = player.current_room.e_to
        print(player.current_room)
        # return player
    elif moron == 'w' and player.current_room.w_to is not None:
        player.current_room = player.current_room.w_to
        print(player.current_room)
        # return player
    elif moron == 'q':
        print("See ya")
        break
    else:
        print("I am not aware of that direction. Let's do it again")
        

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
