from room import Room
from item import Item
from player import Player
import textwrap
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("bag of weed", "sativa")]), 

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('teslas', 'monkey droppings')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("apples", "oranges")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("apples", "banananas")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("apples", "pear")]),
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
        print(player.current_room.checkroom())
    #pick up item from room
    elif user_input[0] == 'g':
        item = input(f"Which item would you like to wield?")
        #use item to index into list to grab item 
        item_name_list = [i.name for i in player.current_room.storage]
        item_index = item_name_list.index(item)
        player.add_inventory(player.current_room.storage[item_index])
        player.current_room.remove_item(item_index)
        #remove item from room 
    elif user_input[0] == 'd':
        item = input(f"Which item would you like to drop?")
        #use item to index into list to grab item 
        item_name_list = [i.name for i in player.inventory]
        item_index = item_name_list.index(item)
        player.current_room.add_inventory(player.inventory[item_index])
        player.remove_item(item_index)
        print(f"{player.name} drops {item}")
    #check player inventory 
    elif user_input[0] == 'i':
        if len(player.inventory) > 0:
            print(f"{player.name} currently has:")
            for x in range(len(player.inventory)):
                print(f"{player.inventory[x]}")
        else:
            print(f"{player.name} has nothing.")
    else:
        print(player.change_room(user_input[0]))


   