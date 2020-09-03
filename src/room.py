# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room: 
    def __init__(self, name, description, storage=[]):
        self.name = name
        self.description = description
        self.storage = storage
       
    def __str__(self):
        return f'{self.name}, \n{self.description}, \n{self.storage}'

    def checkroom(self):
        for x in range(len(self.storage)):
            print(f"{self.storage[x]}")
    
    def add_inventory(self, storage):
        self.storage.append(storage)
    
    def remove_item(self, storage):
        del self.storage[storage]


