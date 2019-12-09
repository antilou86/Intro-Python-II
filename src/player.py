# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, room):
        self.room= room
        self.items = []

    def get_item(self, item):
        self.room.items.remove(item)
        self.items.append(item)
        print(f"\npicked up {item.description} {item.name}\n")

    def drop_item(self, item):
        self.items.remove(item)
        self.room.items.append(item)
        print(f"\nDropped {item.description} {item.name}\n")
    

    def print_inv(self):
        if len(self.items) != 0:
            for i in self.items:
                print(f"Current inventory: {i.description} {i.name}\n")
        else:
            print("There is nothing in your inventory.")