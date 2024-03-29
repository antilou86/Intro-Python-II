from room import Room
from player import Player
from item import Item

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
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
# guess i'll declare the items here.
item = {
    'sword': Item("sword", "flaming"),
    'shield': Item("shield", "broken"),
    'key': Item("key", "rusty"),
}

# choose a room to place items
room['foyer'].items.append(item['key']) 
room['overlook'].items.append(item['sword'])
room['narrow'].items.append(item['shield'])

# Make a new player object that is currently in the 'outside' room.
p1 = Player(room['outside'])

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

print("\nWelcome to your adventure. An ancient treasure lies within. \nTravel the depths and discover riches beyond your wildest dreams. \n")
while True:
    if len(p1.room.items) == 0:
        print(f"{p1.room.name}.\n{p1.room.description}\n")
    else:
        print(f"{p1.room.name}.\n{p1.room.description}\n")
        p1.room.print_inv()
    
    cmd=input(">>> ")

    if len(cmd.split(" ")) == 1:
        if cmd == "n":
            if (p1.room.n_to != None):
                p1.room = p1.room.n_to
                pass
            else:
                print("Hmm, can't go North from here...\n")
                
        elif cmd == "s":
            if (p1.room.s_to != None):
                p1.room = p1.room.s_to
                pass
            else:
                print("Hmm, can't go South from here...\n")

        elif cmd == "e":
            if (p1.room.e_to != None):
                p1.room = p1.room.e_to
                pass
            else:
                print("Hmm, can't go East from here...\n")
        elif cmd == "w":
            if (p1.room.w_to != None):
                p1.room = p1.room.w_to
                pass
            else:
                print("Hmm, can't go West from here...\n")
        elif cmd == "inv" or cmd == "i" or cmd == "inventory":
            p1.print_inv()
            pass
        elif cmd == "q":
            print("Buh-Bye now, play again soon")
            break
        else:
            print("Sorry, I don't understand that command...")
            pass
    elif len(cmd.split(" ")) == 2:
            multi_cmd= cmd.split(" ")
            first= multi_cmd[0]
            second= multi_cmd[1]
            if first.lower() == "get" or first.lower() == "take":
                for i in p1.room.items:
                    if second.lower() == i.name:
                        p1.get_item(i)
                    else:
                        print(f"sorry, there doesn't seem to be a {second} here")
            elif first.lower() == "drop":
                for i in p1.items:
                    if second.lower() == i.name:
                        p1.drop_item(i)
                    else:
                        print(f"you have no {second} to drop")
            else:
                print("wait, what was that command?")

                
    
