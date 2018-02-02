
import cmd


worldRooms = {
    'Start': {
        'DOORS': {'FORWARD': 'Wing A'},
        'DESC': 'You wake up in a room with no memory of how you got there. ...',
        'GROUND': ['', '']},
    'Wing A from Start': {
        'DOORS': {'FORWARD': 'HALLWAY JUNCTION THING A', 'BACK': 'Start', 'LEFT': 'Grand Ballroom', 'RIGHT': 'Something Room'},
        'DESC': ''},
    'Grand Ballroom': {
        'DOORS': {'LEFT': 'Wing B', 'RIGHT': 'Wing A'},
        'DESC': '',
        'GROUND': ['']},
    'Wing A from Grand Ballroom': {
        'DOORS': {'FORWARD': 'Something Room', 'BACK': 'Grand Ballroom', 'LEFT': 'HALLWAY JUNCTION THING A', 'RIGHT': 'Start'},
        'DESC': ''},
    'Wing B from Grand Ballroom': {
        'DOORS': {'FORWARD': 'Study', 'BACK': 'Grand Ballroom', 'LEFT': 'Art Gallery', 'RIGHT': 'HALLWAY JUNCTION THING B'},
        'DESC': ''},
    'Something Room': {
        'DOORS': {'LEFT': 'Wing A', 'RIGHT': 'Wing C'},
        'DESC': '',
        'GROUND': ['']},
    'Wing A from Something Room': {
        'DOORS': {'FORWARD': 'Grand Ballroom', 'BACK': 'Something Room', 'LEFT': 'Start', 'RIGHT': 'HALLWAY JUNCTION THING A'},
        'DESC': ''},
    'Wing C from Something Room': {
        'DOORS': {'FORWARD': 'Library', 'BACK': 'Something Room', 'LEFT': 'HALLWAY JUNCTION THING C', 'RIGHT': 'Locked Closet'},
        'DESC': ''},
    'Art Gallery': {
        'DOORS': {'FORWARD': 'Wing B'},
        'DESC': '',
        'GROUND': []},
    'Wing B from Art Gallery': {
        'DOORS': {'FORWARD': 'HALLWAY JUNCTION THING B', 'BACK': 'Art Gallery', 'LEFT': 'Study', 'RIGHT': 'Grand Ballroom'},
        'DESC': ''},
    'Locked Closet': {
        'DOORS': {'FORWARD': 'Wing C'},
        'DESC': '',
        'SHOP': [''],
        'GROUND': ['Shop Howto']},
    'Wing C from Locked Closet': {
        'DOORS': {'FORWARD': 'HALLWAY JUNCTION THING C', 'BACK': 'Locked Closet', 'LEFT': 'Something Room', 'RIGHT': 'Library'},
        'DESC': ''},
    'Study': {
        'DOORS': {'LEFT': 'Wing D', 'RIGHT': 'Wing B'},
        'DESC': '',
        'GROUND': []},
    'Wing B from Study': {
        'DOORS': {'FORWARD': 'Grand Ballroom', 'BACK': 'Study', 'LEFT': 'HALLWAY JUNCTION THING B', 'RIGHT': 'Art Gallery'},
        'DESC': ''},
    'Wing D from Study': {
        'DOORS': {'FORWARD': 'Library', 'BACK': 'Study', 'LEFT': 'Kitchen', 'RIGHT': 'Long Corridor'},
        'DESC': ''},
    'Library': {
        'DOORS': {'LEFT': 'Wing C', 'RIGHT': 'Wing D'},
        'DESC': '',
        'UP': 'Secret Attic',  #SPECIAL CASE -- MIGHT NEED TWEAKING
        'GROUND': ['']},
    'Secret Attic': {
        'DESC': '',
        'DOWN': 'Library',     #SPECIAL CASE -- MIGHT NEED TWEAKING
        'GROUND': ['']},
    'Wing C from Library': {
        'DOORS': {'FORWARD': 'Something Room', 'BACK': 'Library', 'LEFT': 'Locked Closet', 'RIGHT': 'HALLWAY JUNCTION THING B'},
        'DESC': ''},
    'Wing D from Library': {
        'DOORS': {'FORWARD': 'Study', 'BACK': 'Library', 'LEFT': 'Long Corridor', 'RIGHT': 'Kitchen'},
        'DESC': ''},
    'Kitchen': {
        'DOORS': {'FORWARD': 'Wing D'},
        'DESC': '',
        'SHOP': ['', '', ''],
        'GROUND': ['', 'Shop Howto']},
    'Wing D from Kitchen': {
        'DOORS': {'FORWARD': 'Long Corridor', 'BACK': 'Kitchen', 'LEFT': 'Library', 'RIGHT': 'Study'},
        'DESC': ''},
    'Wing A leading to other wings': {
        'DESC': '',
        'BACK': '',
        'LEFT': '',
        'RIGHT': ''},
    'Wing B leading to other wings': {
        'DESC': '',
        'FORWARD': '',
        'BACK': '',
        'LEFT': '',
        'RIGHT': ''},
    'Wing C leading to other wings': {
        'DESC': '',
        'FORWARD': '',
        'BACK': '',
        'LEFT': '',
        'RIGHT': ''},
    'Wing D leading to other wings': {
        'DESC': '',
        'FORWARD': '',
        'BACK': '',
        'LEFT': '',
        'RIGHT': ''},
    'Entrance to Wing A': {
        'DESC': '',
        'FORWARD': 'Start',
        'LEFT': 'Something Room',
        'RIGHT': 'Grand Ballroom'},
    'Entrance to Wing B': {
        'DESC': '',
        'FORWARD': 'Art Gallery',
        'LEFT': 'Grand Ballroom',
        'RIGHT': 'Study'},
    'Entrance to Wing C': {
        'DESC': '',
        'FORWARD': 'Locked Closet',
        'LEFT': 'Library',
        'RIGHT': 'Something Room'},
    'Entrance to Wing D': {
        'DESC': '',
        'FORWARD': 'Kitchen',
        'LEFT': 'Study',
        'RIGHT': 'Library'},
    'Long Corridor': {
        'DESC': '',
        'FORWARD': 'Locked Room',
        'BACK': 'Wing B'},
    'Locked Room': {
        'DESC': '',
        'FORWARD': '',
        'BACK': ''},
    }

worldWings = {
    'Wing A': {
        'DESC': 'write desc',
        'NORTH': 'HALLWAY JUNCTION THING A',
        'EAST': 'Something Room',
        'SOUTH': 'Start',
        'WEST': 'Grand Ballroom'},
    'Wing B': {
        'DESC': 'write desc',
        'NORTH': 'Study',
        'EAST': 'HALLWAY JUNCTION THING B',
        'SOUTH': 'Grand Ballroom',
        'WEST': 'Art Gallery'},
    'Wing C': {
        'DESC': 'write desc',
        'NORTH': 'Library',
        'EAST': 'Locked Closet',
        'SOUTH': 'Something Room',
        'WEST': 'HALLWAY JUNCTION THING C'},
    'Wing D': {
        'DESC': 'write desc',
        'NORTH': 'Kitchen',
        'EAST': 'Library',
        'SOUTH': 'HALLWAY JUNCTION THING D',
        'WEST': 'Study'}
    }

#Class:

class Room(object):
    """Create a room object

    Each room is assumed to have four walls, with one possible door in each.
    Each wall will either have a door or not. No support for closed/open doors yet
    """

    def __init__(self, name, desc, front=True, back=True, left=True, right=True):
        self.name = name
        self.walls = {'front': front, 'back': back, 'left': left, 'right': right}
        self.desc = desc

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
                    print(f'Forward: '+ worldRooms[self.name]['DOORS']['FORWARD'])
                elif k == 'back':
                    print(f'Back: ' + worldRooms[self.name]['DOORS']['BACK'])
                elif k == 'left':
                    print(f'Left: ' + worldRooms[self.name]['DOORS']['LEFT'])
                elif k == 'right':
                    print(f'Right: ' + worldRooms[self.name]['DOORS']['RIGHT'])
                else:
                    break


#Class -- modified for wings

class Wing(object):
    """Blah blah blah description"""

    def __init__(self, name, desc, north=True, south=True, east=True, west=True):
        self.name = name
        self.walls = {'north': north, 'south': south, 'east': east, 'west': west}
        self.desc = desc

    def altnextTurn(self):
        #prints room name
        print(self.name)
        print("=" * len(self.name))

        #prints description
        print(self.desc)
        print(' ')

        #mimicing available rooms
        for k,v in self.walls.items():
            if v == True:
                name_2 = (f'{self.name} from {prevlocation}')
                list1 = (worldRooms[name_2]['DOORS']).keys()
                for n in list1:
                    print((str(f"{n}: {worldRooms[name_2]['DOORS'][n]}")).title())
            break

class TextAdventureCmd(cmd.Cmd):
    prompt = '\n> '

    def default(self, arg):
        print('I do not understand that command. Type "help" for a list of commands.')

    def do_quit(self, arg):
        return True

    def do_forward(self, arg):
        if location != 'Wing A' or 'Wing B' or 'Wing C' or 'Wing D':
        location = location
        parameters = {
            'start': Room(location, worldRooms[location]['DESC'], back=False, left=False, right=False),
            'grandballroom': Room(location, worldRooms[location]['DESC'], front=False, back=False),
            'somethingroom': Room(location, worldRooms[location]['DESC'], front=False, back=False),
            'artgallery': Room(location, worldRooms[location]['DESC'], back=False, left=False, right=False),
            'locked room': Room(location, worldRooms[location]['DESC'], back=False, left=False, right=False),
            'study': Room(location, worldRooms[location]['DESC'], left=False, right=False),
            'library': Room(location, worldRooms[location]['DESC'], front=False, back=False), #has special case of 'up'
            'secretattic': Room(location, worldRooms[location]['DESC'], front=False, back=False, left=False, right=False), #ADD DOWN=FALSE TO CLASS
            'kitchen': Room(location, worldRooms[location]['DESC'], back=False, left=False, right=False),
            }
        location_modified = location.lower()
        if ' ' in (location_modified):
            location_modified = location_modified.replace(" ", "")
        self = parameters[location_modified]
        self.nextTurn()
        print(' ')
        user_input = str(input('Where would you like to travel? ')).upper()
        print(' ')
        print(' ')
        print(' ')
        newlocation = worldRooms[location]['DOORS'][user_input]
        prevlocation = location
        location = newlocation
    if location == 'Wing A' or 'Wing B' or 'Wing C' or 'Wing D':
        location = location
        parameters = {
            'winga': Wing(location, worldWings[location]['DESC']),
            'wingb': Wing(location, worldWings[location]['DESC']),
            'wingc': Wing(location, worldWings[location]['DESC']),
            'wingd': Wing(location, worldWings[location]['DESC'])
            }
        location_modified = location.lower()
        if ' ' in (location_modified):
            location_modified = location_modified.replace(" ", "")
        self = parameters[location_modified]
        self.altnextTurn()
        print(' ')
        user_input = str(input('Which way would you like to go next? ')).upper()
        print(' ')
        print(' ')
        print(' ')
        name_3 = str(f'{location} from {prevlocation}')
        newlocation = worldRooms[name_3]['DOORS'][user_input]
        prevlocation = location
        location = newlocation
    else:
        print('Sorry, you are unable to go in that direction.')





#Begginning Fancy Stuff
title = 'I still have to think of a title'
print(title)
print(f'=' * len(title))
print(' ')
print('(Type "help" for commands.)')
print(' ')


#prints turn for Start
location = 'Start'




while True:
    if location != 'Wing A' or 'Wing B' or 'Wing C' or 'Wing D':
        location = location
        parameters = {
            'start': Room(location, worldRooms[location]['DESC'], back=False, left=False, right=False),
            'grandballroom': Room(location, worldRooms[location]['DESC'], front=False, back=False),
            'somethingroom': Room(location, worldRooms[location]['DESC'], front=False, back=False),
            'artgallery': Room(location, worldRooms[location]['DESC'], back=False, left=False, right=False),
            'locked room': Room(location, worldRooms[location]['DESC'], back=False, left=False, right=False),
            'study': Room(location, worldRooms[location]['DESC'], left=False, right=False),
            'library': Room(location, worldRooms[location]['DESC'], front=False, back=False), #has special case of 'up'
            'secretattic': Room(location, worldRooms[location]['DESC'], front=False, back=False, left=False, right=False), #ADD DOWN=FALSE TO CLASS
            'kitchen': Room(location, worldRooms[location]['DESC'], back=False, left=False, right=False),
            }
        location_modified = location.lower()
        if ' ' in (location_modified):
            location_modified = location_modified.replace(" ", "")
        self = parameters[location_modified]
        self.nextTurn()
        print(' ')
        user_input = str(input('Where would you like to travel? ')).upper()
        print(' ')
        print(' ')
        print(' ')
        newlocation = worldRooms[location]['DOORS'][user_input]
        prevlocation = location
        location = newlocation
    if location == 'Wing A' or 'Wing B' or 'Wing C' or 'Wing D':
        location = location
        parameters = {
            'winga': Wing(location, worldWings[location]['DESC']),
            'wingb': Wing(location, worldWings[location]['DESC']),
            'wingc': Wing(location, worldWings[location]['DESC']),
            'wingd': Wing(location, worldWings[location]['DESC'])
            }
        location_modified = location.lower()
        if ' ' in (location_modified):
            location_modified = location_modified.replace(" ", "")
        self = parameters[location_modified]
        self.altnextTurn()
        print(' ')
        user_input = str(input('Which way would you like to go next? ')).upper()
        print(' ')
        print(' ')
        print(' ')
        name_3 = str(f'{location} from {prevlocation}')
        newlocation = worldRooms[name_3]['DOORS'][user_input]
        prevlocation = location
        location = newlocation
    else:
        print('Sorry, you are unable to go in that direction.')

