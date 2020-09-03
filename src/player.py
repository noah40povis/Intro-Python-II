# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
from item import Item
class Player:

    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f'Hi {self.name}, you are currently in room: {self.current_room}'
    
    def change_room(self, direction):
        #Do you have the ability to move in this direction 
        if hasattr(self.current_room, f'{direction}_to'):
            #moving the character to the certain direction 
            self.current_room = getattr(self.current_room, f'{direction}_to')
        else:
            print('Sorry you cannot go this way.')
    #need to add to adv still!!!
    def get_room(self, current_room):
        print(f'{self.current_room}')
    
    def add_inventory(self, inventory):
        self.inventory.append(inventory)
    
    def remove_item(self, inventory):
        del self.inventory[inventory]

    


   

    
  