# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, room):
        self.room= current_room
        self.items = []

    def get_item(self, item):
        self.items.append(item)
        current_room.remove(item)
        print(f"picked up {item.description} {item.name}")

    def drop_item(self, item, current_room):
        self.items.remove(item)
        current_room.items.append(item)
        print(f"dropped {item.description} {item.name}")
    
    def print_inv(self):
        if len(self.items) != 0:
            print(f"Current inventory: {self.items}")
        else:
            print("There is nothing in your inventory.")