from room import Room
from item import Item
from player import Player
import textwrap
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("bag of weed", "sativa")]), 

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", Item('teslas', 'monkey droppings')),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", Item("apples", "oranges")),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", Item("apples", "banananas")),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", Item("apples", "pear")),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input("What is your name?"),room["outside"])

# directions = ['n', 's', 'e', 'w']


# Write a loop that:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
running = True

while running: 

    print(f"You are in the {player.current_room.name}.") 
    for line in textwrap.wrap(player.current_room.description):
        print(line)
    user_input = input(f"Where would you like to go {player.name}? \nPlease Type: North, South, East, or West.").lower().strip()
    
    if user_input[0] == 'n':
        player.change_room(user_input[0])
        print(player.current_room.name)
    
    elif user_input[0] == 's':
        player.change_room(user_input[0])
        print(player.current_room.name)
    
    elif user_input[0] == 'e':
        player.change_room(user_input[0])
        print(player.current_room.name)
    
    elif user_input[0] == 'w':
        player.change_room(user_input[0])
        print(player.current_room.name)
    #quit out of gaem 
    elif user_input[0] == 'q':
        running = False
    #check room for item 
    elif user_input[0] == 'c':
        Room = player.current_room 
        print(player.current_room.checkroom())
    else:
        print(player.change_room(user_input[0]))


   