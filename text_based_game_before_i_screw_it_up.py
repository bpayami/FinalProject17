"""
                                +---------------+
                                |               |
    T H E   M A P               |               |
          O F                   |               |
                                |    Kitchen    |
        T H E   M A N S I O N   |               |
                                |               |
                                |               |
                +---------------+-------O-------+---------------+
                |               |      | |      |               |
                |               |      | |      |               |
                |               |______| |______|               |
                |     Study     O______ D ______O    Library    |
                |               |      | |      |               |
                |               |      | |      |               |
                |               |      | |      |               |
+---------------+-------O-------+______| |______+-------O-------+---------------+
|               |      | |      |  ____   ____  |      | |      |               |
|               |      | |      | |    | |    | |      | |      |               |
|      Art      |______| |______| |  +--0--+  | |______| |______|    Locked     |
|    Gallery    O______ B ______  |  | ??? |  |  ______ C ______O    Closet     |
|               |      | |      | |  +-----+  | |      | |      |               |
|               |      | |      | |___________| |      | |      |               |
|               |      | |      |______   ______|      | |      |               |
+---------------+-------O-------+      | |      +-------O-------+---------------+
                |               |      | |      |               |
                |               |      | |      |               |
                |  Grand        |______| |______|  Something    |
                |   Ballroom    O______ A ______O   Room        |
                |               |      | |      |               |
                |               |      | |      |               |
                |               |      | |      |               |
                +---------------+-------O-------+---------------+
                                |               |
                                |               |
                                |   Start       |
                                |     Here...   |
                                |               |
                                |               |
                                |               |
                                +---------------+




"""

"""
Costant Variables:
"""

DESC = 'desc'
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
FORWARD = 'forward'
BACK = 'back'
LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'
GROUND = 'ground'
SHOP = 'shop'
GROUNDDESC = 'grounddesc'
SHORTDESC = 'shortdesc'
LONGDESC = 'longdesc'
TAKEABLE = 'takeable'
EDIBLE = 'edible'
DESCWORDS = 'descwords'

SCREEN_WIDTH = 80

"""
Dictionary:
"""
worldRooms = {
    'Start': {
        DESC: 'You wake up in a room with no memory of how you got there. ...',
        FORWARD: 'Wing A',
        GROUND: ['', '']},
    'Wing A from Start': {
        DESC: '',
        FORWARD: 'HALLWAY JUNCTION THING A',
        BACK: 'Start',
        LEFT: 'Grand Ballrooom',
        RIGHT: 'Something Room'},
    'Grand Ballroom': {
        DESC: '',
        LEFT: 'Wing B',
        RIGHT: 'Wing A',
        GROUND: ['']},
    'Wing A from Grand Ballroom': {
        DESC: '',
        FORWARD: 'Something Room',
        BACK: 'Grand Ballroom',
        LEFT: 'HALLWAY JUNCTION THING A',
        RIGHT: 'Start'},
    'Wing B from Grand Ballroom': {
        DESC: '',
        FORWARD: 'Study',
        BACK: 'Grand Ballroom',
        LEFT: 'Art Gallery',
        RIGHT: 'HALLWAY JUNCTION THING B'},
    'Something Room': {
        DESC: '',
        LEFT: 'Wing A',
        RIGHT: 'Wing C',
        GROUND: ['']},
    'Wing A from Something Room': {
        DESC: '',
        FORWARD: 'Grand Ballroom',
        BACK: 'Something Room',
        LEFT: 'Start',
        RIGHT: 'HALLWAY JUNCTION THING A'},
    'Wing C from Something Room': {
        DESC: '',
        FORWARD: 'Library',
        BACK: 'Something Room',
        LEFT: 'HALLWAY JUNCTION THING C',
        RIGHT: 'Locked Closet'},
    'Art Gallery': {
        DESC: '',
        FORWARD: 'Wing B',
        GROUND: []},
    'Wing B from Art Gallery': {
        DESC: '',
        FORWARD: 'HALLWAY JUNCTION THING B',
        BACK: 'Art Gallery',
        LEFT: 'Study',
        RIGHT: 'Grand Ballroom'},
    'Locked Closet': {
        DESC: '',
        FORWARD: 'Wing C',
        SHOP: [''],
        GROUND: ['Shop Howto']},
    'Wing C from Locked Closet': {
        DESC: '',
        FORWARD: 'HALLWAY JUNCTION THING C',
        BACK: 'Locked Closet',
        LEFT: 'Something Room',
        RIGHT: 'Library'},
    'Study': {
        DESC: '',
        LEFT: 'Wing D',
        RIGHT: 'Wing B',
        GROUND: []},
    'Wing B from Study': {
        DESC: '',
        FORWARD: 'Grand Ballroom',
        BACK: 'Study',
        LEFT: 'HALLWAY JUNCTION THING B',
        RIGHT: 'Art Gallery'},
    'Wing D from Study': {
        DESC: '',
        FORWARD: 'Library',
        BACK: 'Study',
        LEFT: 'Kitchen',
        RIGHT: 'Long Corridor'},
    'Library': {
        DESC: '',
        LEFT: 'Wing C',
        RIGHT: 'Wing D',
        UP: 'Secret Attic',
        GROUND: ['']},
    'Secret Attic': {
        DESC: '',
        DOWN: 'Library',
        GROUND: ['']},
    'Wing C from Library': {
        DESC: '',
        FORWARD: 'Something Room',
        BACK: 'Library',
        LEFT: 'Locked Closet',
        RIGHT: 'HALLWAY JUNCTION THING B'},
    'Wing D from Library': {
        DESC: '',
        FORWARD: 'Study',
        BACK: 'Library',
        LEFT: 'Long Corridor',
        RIGHT: 'Kitchen'},
    'Kitchen': {
        DESC: '',
        FORWARD: 'Wing D',
        SHOP: ['', '', ''],
        GROUND: ['', 'Shop Howto']},
    'Wing D from Kitchen': {
        DESC: '',
        FORWARD: 'Long Corridor',
        BACK: 'Kitchen',
        LEFT: 'Library',
        RIGHT: 'Study'},
    'Wing A leading to other wings': {
        DESC: '',
        BACK: '',
        LEFT: '',
        RIGHT: ''},
    'Wing B leading to other wings': {
        DESC: '',
        FORWARD: '',
        BACK: '',
        LEFT: '',
        RIGHT: ''},
    'Wing C leading to other wings': {
        DESC: '',
        FORWARD: '',
        BACK: '',
        LEFT: '',
        RIGHT: ''},
    'Wing D leading to other wings': {
        DESC: '',
        FORWARD: '',
        BACK: '',
        LEFT: '',
        RIGHT: ''},
    'Entrance to Wing A': {
        DESC: '',
        FORWARD: 'Start',
        LEFT: 'Something Room',
        RIGHT: 'Grand Ballroom'},
    'Entrance to Wing B': {
        DESC: '',
        FORWARD: 'Art Gallery',
        LEFT: 'Grand Ballroom',
        RIGHT: 'Study'},
    'Entrance to Wing C': {
        DESC: '',
        FORWARD: 'Locked Closet',
        LEFT: 'Library',
        RIGHT: 'Something Room'},
    'Entrance to Wing D': {
        DESC: '',
        FORWARD: 'Kitchen',
        LEFT: 'Study',
        RIGHT: 'Library'},
    'Long Corridor': {
        DESC: '',
        FORWARD: 'Locked Room',
        BACK: 'Wing B'},
    'Locked Room': {
        DESC: '',
        FORWARD: '',
        BACK: ''},
    }



class Room(object):
    """Create a room object

    Each room is assumed to have four walls, with one possible door in each.
    Each wall will either have a door or not. No support for closed/open doors yet
    """

    def __init__(self, name, desc, front=True, back=True, left=True, right=True):
        self.name = name
        self.walls = {'front': front, 'back': back, 'left': left, 'right': right}
        self.desc = desc

    wallDirections = {
        'front':  worldRooms[self.name][FORWARD],
        'back': worldRooms[self.name][BACK],
        'left': worldRooms[self.name][LEFT],
        'right': worldRooms[self.name][RIGHT]
        }

    def nextTurn(self):
        #prints room name
        print(self.name)
        print("=" * len(self.name))

        #prints description
        print(self.desc)

        #prints available doors
        for k, v in self.walls.items():
            if v:
                print(f"You see a door to the {k}.")
                print(' ')

        #prints which direction is which room
        for k, v in self.walls.items():
            if v == True:
                if k == 'front':
                    print(wallDirections["front"]+ worldRooms[self.name][FORWARD])
                elif k == 'back':
                    print(wallDirections["back"] + worldRooms[self.name][BACK])
                elif k == 'left':
                    print(wallDirections["left"] + worldRooms[self.name][LEFT])
                elif k == 'right':
                    print(f'Right: ' + worldRooms[self.name][RIGHT])
                #^^ PICK UP RIGHT HERE THIS WAS WORKING IF YOU DELETE THE DICTIONARY AND RESTORE TO FORMAT OF RIGHT


#Begginning Fancy Stuff
title = 'I still have to think of a title'
print(title)
print(f'=' * len(title))
print(' ')
print('(Type "help" for commands.)')
print(' ')


#prints turn for Start
location = 'Start'
start = Room(location, worldRooms[location][DESC], back=False, left=False, right=False)
start.nextTurn()
print(' ')

#implement this later for simplification in code
#def current_room():
#    user_input = str(input()).upper()
#    input_converted = worldRooms[current_room][{user_input}]

user_input = str(input('Where would you like to travel?')).upper()
#this will print 'FORWARD'
#i need this to become the variable FORWARD
#b/c it then needs to reference the direction in the given room


print(user_input)
print(location)
#input_converted =

print(worldRooms[location][user_input])
#print(worldRooms[current_room][{user_input}])


#direction = Room({current_room}, worldRooms[{current_room}][DESC], back=False, left=False, right=False)
#direction.nextTurn()

#print(direction)




#OLD BEGINNING FUCTIONS OF GAME (IGNORE)
"""
location = 'Start'
#inventory = ['']

def displayLocation(loc):  #function for room title
    print(loc)  #prints room name
    print("=" * len(loc))  #prints a double line under name


def displayDescription(loc):
    print(' ')
    print(worldRooms[loc][DESC])

def displayDirections(loc):
    print(' ')
    for key, value in worldRooms[loc].items():
        print(f'* {str(key).upper()}: {value}')


    if FORWARD:
        print(f'Forward: ' + worldRooms[loc][FORWARD])
    if BACK:
        print(f'Back: ' + worldRooms[loc][BACK])


displayLocation('Start')
displayDescription('Start')
displayDirections('Start')
"""


"""
ToDo List:
-print location and description
-print direction options
-ask for user input
-translate input into new location
"""


"""
#Random code I'm unwilling to part with lol

                #if 'front' == True:
                    #print(f'Forward: ' + worldRooms[self.walls.items()])
                #if BACK:
                    #print(f'Back: ' + worldRooms[loc][BACK])
"""


"""
#EXAMPLE CODE FROM GERSTEIN

def check_inventory(item_to_check):
    if item_to_check in inventory.keys() and item_to_check > 0:
        print(f'Yes, you have at least one of {item_to_check}')
    elif item_to_check in inventory.keys():
        print(f"You don't have any {item_to_check} right now.")
    else:
        print(f"I don't know what that is.")

check_inventory('item goes here')

def eat_item(item_to_eat):
    if item_to_eat in inventory.keys() and inventory[item_to_eat] > 1
    print(f'You have {inventory[item_to_eat]} {item_to_eat}')
    print("You are now less hungry")
    print



inventory = {

    'flashlight':
        {'qty': 1, 'category': 'clothing', 'durability': 100},
    'item'
"""