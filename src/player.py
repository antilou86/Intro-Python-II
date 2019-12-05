# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, room):
        self.room= current_room
        self.items = []

    def get_item(self, item):
        self.room.items.remove(item)
        self.items.append(item)
        print(f"picked up {item.description} {item.name}")

    def drop_item(self, item):
        self.items.remove(item)
        self.room.items.append(item)
        print(f"Dropped {item.description} {item.name}")
    
    def print_inv(self):
        if len(self.items) != 0:
            print(f"Current inventory: {self.items}")
        else:
            print("There is nothing in your inventory.")