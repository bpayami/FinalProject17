#SEE NOTE TO SELF ON LINE 271 YOU EVIL GENIUS

import cmd

def map():
    print("""


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

    """)

worldRooms = {
    'Start': {
        'DOORS': {'FORWARD': 'Wing A'},
        'DESC': 'You wake up in a room with no memory of how you got there. ...',
        'GROUND': ['', '']},
    'Wing A from Start': {
        'DOORS': {'FORWARD': 'Main Hall from Wing A', 'BACK': 'Start', 'LEFT': 'Grand Ballroom', 'RIGHT': 'Something Room'},
        'DESC': ''},
    'Grand Ballroom': {
        'DOORS': {'LEFT': 'Wing B', 'RIGHT': 'Wing A'},
        'DESC': '',
        'GROUND': ['']},
    'Wing A from Grand Ballroom': {
        'DOORS': {'FORWARD': 'Something Room', 'BACK': 'Grand Ballroom', 'LEFT': 'Main Hall from Wing A', 'RIGHT': 'Start'},
        'DESC': ''},
    'Wing B from Grand Ballroom': {
        'DOORS': {'FORWARD': 'Study', 'BACK': 'Grand Ballroom', 'LEFT': 'Art Gallery', 'RIGHT': 'Main Hall from Wing B'},
        'DESC': ''},
    'Something Room': {
        'DOORS': {'LEFT': 'Wing A', 'RIGHT': 'Wing C'},
        'DESC': '',
        'GROUND': ['']},
    'Wing A from Something Room': {
        'DOORS': {'FORWARD': 'Grand Ballroom', 'BACK': 'Something Room', 'LEFT': 'Start', 'RIGHT': 'Main Hall from Wing A'},
        'DESC': ''},
    'Wing C from Something Room': {
        'DOORS': {'FORWARD': 'Library', 'BACK': 'Something Room', 'LEFT': 'Main Hall from Wing C', 'RIGHT': 'Locked Closet'},
        'DESC': ''},
    'Art Gallery': {
        'DOORS': {'FORWARD': 'Wing B'},
        'DESC': '',
        'GROUND': []},
    'Wing B from Art Gallery': {
        'DOORS': {'FORWARD': 'Main Hall from Wing B', 'BACK': 'Art Gallery', 'LEFT': 'Study', 'RIGHT': 'Grand Ballroom'},
        'DESC': ''},
    'Locked Closet': {
        'DOORS': {'FORWARD': 'Wing C'},
        'DESC': '',
        'SHOP': [''],
        'GROUND': ['Shop Howto']},
    'Wing C from Locked Closet': {
        'DOORS': {'FORWARD': 'Main Hall from Wing C', 'BACK': 'Locked Closet', 'LEFT': 'Something Room', 'RIGHT': 'Library'},
        'DESC': ''},
    'Study': {
        'DOORS': {'LEFT': 'Wing D', 'RIGHT': 'Wing B'},
        'DESC': '',
        'GROUND': []},
    'Wing B from Study': {
        'DOORS': {'FORWARD': 'Grand Ballroom', 'BACK': 'Study', 'LEFT': 'Main Hall from Wing B', 'RIGHT': 'Art Gallery'},
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
        'DOORS': {'FORWARD': 'Something Room', 'BACK': 'Library', 'LEFT': 'Locked Closet', 'RIGHT': 'Main Hall from Wing B'},
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
    'Main Hall from Wing A': {
        'DOORS': {'LEFT': 'Wing B', 'RIGHT': 'Wing C'},
        'DESC': ''},
    'Main Hall from Wing B': {
        'DOORS': {'LEFT': 'Wing D', 'RIGHT': 'Wing A'},
        'DESC': ''},
    'Main Hall from Wing C': {
        'DOORS': {'LEFT': 'Wing A', 'RIGHT': 'Wing D'},
        'DESC': ''},
    'Main Hall from Wing D': {
        'DOORS': {'LEFT': 'Wing C', 'RIGHT': 'Wing B'},
        'DESC': ''},
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
        'NORTH': 'Main Hall from Wing A',
        'EAST': 'Something Room',
        'SOUTH': 'Start',
        'WEST': 'Grand Ballroom'},
    'Wing B': {
        'DESC': 'write desc',
        'NORTH': 'Study',
        'EAST': 'Main Hall from Wing B',
        'SOUTH': 'Grand Ballroom',
        'WEST': 'Art Gallery'},
    'Wing C': {
        'DESC': 'write desc',
        'NORTH': 'Library',
        'EAST': 'Locked Closet',
        'SOUTH': 'Something Room',
        'WEST': 'Main Hall from Wing C'},
    'Wing D': {
        'DESC': 'write desc',
        'NORTH': 'Kitchen',
        'EAST': 'Library',
        'SOUTH': 'Main Hall from Wing D',
        'WEST': 'Study'}
    }

worldHalls = {
    'Main Hall from Wing A': {
        'DOORS': {'LEFT': 'Wing B', 'RIGHT': 'Wing C'},
        'DESC': ''},
    'Main Hall from Wing B': {
        'DOORS': {'LEFT': 'Wing D', 'RIGHT': 'Wing A'},
        'DESC': ''},
    'Main Hall from Wing C': {
        'DOORS': {'LEFT': 'Wing A', 'RIGHT': 'Wing D'},
        'DESC': ''},
    'Main Hall from Wing D': {
        'DOORS': {'LEFT': 'Wing C', 'RIGHT': 'Wing B'},
        'DESC': ''}
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

class Hall(object):
    """Blah blah blah description"""

    def __init__(self, name, desc, right=True, left=True):
        self.name = name
        self.halls = {'right': right, 'left': left}
        self.desc = desc

    def alt2nextTurn(self):
        #prints room name
        print(self.name)
        print("=" * len(self.name))

        #prints description
        print(self.desc)
        print(' ')

        #mimicing available rooms
        for k,v in self.halls.items():
            if v == True:
                name_3 = (f'{self.name} from {prevlocation}')
                list1 = (worldRooms[name_3]['DOORS']).keys()
                for n in list1:
                    print((str(f"{n}: {worldRooms[name_3]['DOORS'][n]}")).title())
            break

class TextAdventureCmd(cmd.Cmd):
    prompt = '\n> '

    def default(self, arg):
        print('I do not understand that command. Type "help" for a list of commands.')

    """
    def do_quit(self, arg):
        return True            #THIS WILL HAVE TO BE INCORPORATED INTO WHILE LOOP AS AN IF STATEMENT
    """

    def do_forward(self, arg):
        global user_input
        user_input = 'FORWARD'
        return True

    def do_back(self,arg):
        global user_input
        user_input = 'BACK'
        return True

    def do_left(self, arg):
        global user_input
        user_input = 'LEFT'
        return True

    def do_right(self, arg):
        global user_input
        user_input = 'RIGHT'
        return True

    def do_look(self, arg):
        print('haha you looked')
        print('\n')


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
            'study': Room(location, worldRooms[location]['DESC'], front=False, back=False),
            'library': Room(location, worldRooms[location]['DESC'], front=False, back=False), #has special case of 'up'
            'secretattic': Room(location, worldRooms[location]['DESC'], front=False, back=False, left=False, right=False), #ADD DOWN=FALSE TO CLASS
            'kitchen': Room(location, worldRooms[location]['DESC'], back=False, left=False, right=False),
            'mainhallfromwinga': Room(location, worldRooms[location]['DESC'], front=False, back=False),
            'mainhallfromwingb': Room(location, worldRooms[location]['DESC'], front=False, back=False),
            'mainhallfromwingc': Room(location, worldRooms[location]['DESC'], front=False, back=False),
            'mainhallfromwingd': Room(location, worldRooms[location]['DESC'], front=False, back=False)}
        location_modified = location.lower()
        if ' ' in (location_modified):
            location_modified = location_modified.replace(" ", "")
        self = parameters[location_modified]
        self.nextTurn()

        TextAdventureCmd().cmdloop()

        global user_input
        if user_input == 'FORWARD' or 'BACK' or 'LEFT' or 'RIGHT':
            print(' \n \n')
            if location == 'Main Hall':
                location = (location.replace(" ", "")).lower()
            newlocation = worldRooms[location]['DOORS'][user_input]                     #THIS IS THE PROBLEM SECTION
            prevlocation = location
            location = newlocation
            print(location)

        else:
            print('Sorry, I don\'t recognize that command.  Enter "help" for the list of commands.')

    """
    if location == 'Main Hall':
        location = location
        parameters = {
            'mainhallfromwinga': Hall(location, worldHalls[location]['DESC'], front=False, back=False),
            'mainhallfromwingb': Hall(location, worldHalls[location]['DESC'], front=False, back=False),
            'mainhallfromwingc': Hall(location, worldHalls[location]['DESC'], front=False, back=False),
            'mainhallfromwingd': Hall(location, worldHalls[location]['DESC'], front=False, back=False)}
        location_modified = location.lower()
        if ' ' in (location_modified):
            location_modified = location_modified.replace(" ", "")
        self = parameters[location_modified]
        self.alt2nextTurn()
        print(' ')
        user_input = str(input('Which way would you like to go next? ')).upper()
        print(' \n \n')
        name_4 = str(f'{location} from {prevlocation}')
        newlocation = worldRooms[name_4]['DOORS'][user_input]
        prevlocation = location
        location = newlocation
    """



    if location == 'Wing A' or 'Wing B' or 'Wing C' or 'Wing D':
        location = location
        parameters = {
            'winga': Wing(location, worldWings[location]['DESC']),
            'wingb': Wing(location, worldWings[location]['DESC']),
            'wingc': Wing(location, worldWings[location]['DESC']),
            'wingd': Wing(location, worldWings[location]['DESC'])}
        location_modified = location.lower()
        if ' ' in (location_modified):
            location_modified = location_modified.replace(" ", "")
        self = parameters[location_modified]
        self.altnextTurn()
        print(' ')
        user_input = str(input('Which way would you like to go next? ')).upper()
        print(' \n \n')
        name_5 = str(f'{location} from {prevlocation}')
        newlocation = worldRooms[name_5]['DOORS'][user_input]
        prevlocation = location
        location = newlocation

    else:
        print('Sorry, you are unable to go in that direction.')




"""
while True:
    if location != 'Wing A' or 'Wing B' or 'Wing C' or 'Wing D':
        location = location
        parameters = {
            'start': Room(location, worldRooms[location]['DESC'], back=False, left=False, right=False),
            'grandballroom': Room(location, worldRooms[location]['DESC'], front=False, back=False),
            'somethingroom': Room(location, worldRooms[location]['DESC'], front=False, back=False),
            'artgallery': Room(location, worldRooms[location]['DESC'], back=False, left=False, right=False),
            'locked room': Room(location, worldRooms[location]['DESC'], back=False, left=False, right=False),
            'study': Room(location, worldRooms[location]['DESC'], front=False, back=False),
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
"""



"""
if location == 'Main Hall':
        location = location         #location is Main Hall
        parameters = {
            'mainhallfromwinga': Room(location, worldRooms[location]['DESC'], front=False, back=False),
            'mainhallfromwingb': Room(location, worldRooms[location]['DESC'], front=False, back=False),
            'mainhallfromwingc': Room(location, worldRooms[location]['DESC'], front=False, back=False),
            'mainhallfromwingd': Room(location, worldRooms[location]['DESC'], front=False, back=False)}
        name_2 = str(f'{locaction} from {prevlocation}')
        location = name_2
        location_modified = (prevlocation.replace(" ", "")).lower()
        print(location_modified)                                                   #JUST FOR REFERENCE -- DELETE LATER
        print(location)
        print('this is as far as ive gotten')
        #newlocation = worldRooms[name_3]['DOORS'][user_input]                     #IDK IF I NEED THIS -- IT'S FROM BELOW
        #prevlocation = location                                                   #I REALLY NEED TO TAKE NOTE OF HOW THE WINGS WORK
        #location = newlocation
"""
