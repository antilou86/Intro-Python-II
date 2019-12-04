from room import Room

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

# Make a new player object that is currently in the 'outside' room.

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

while True:
    cmd=input(">>> ")

    if cmd ==  "n":
        #check if there is a room, then move north
        if #.n_to in the player's current room is not None:
            #move to room
        else:
            print("Hmm, I can't go North from here")
    elif cmd == "s":
        #check if there is a room, then move south
        if #.s_to in the player's current room is not None:
            #move to room
        else:
            print("Hmm, I can't go South from way")
    elif cmd == "e":
        #check if there is a room, then move east
        if #.e_to in the player's current room is not None:
            #move to room
        else:
            print("Hmm, I can't go East from here")
    elif cmd == "w":
        #check if there is a room, then move west
        if #.w_to in the player's current room is not None:
            #move to room
        else:
            print("Hmm, I can't go West from here")
    elif cmd == "q":
        #quit game
        print("Buh-Bye now")
        break
    else:
        print("Sorry, I don't understand that command.")
    pass