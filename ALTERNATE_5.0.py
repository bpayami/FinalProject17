#TO-DO LIST
    #Fix long corridor in association with Wing D
    #Figure out locked closet and locked door -perhaps checks inventory for code or true/false for open/close
    #add something into class Room to print what objects are in the room (reference ground in dictionary) -- or just write into description
    #look function
    #take function
    #drop function
    #eat function?
    #use function?
    #help function
    #write in story line
    #randomized monster?

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
        'GROUND': ['Welcome Sign']},
    'Wing A from Start': {
        'DOORS': {'FORWARD': 'Main Hall', 'BACK': 'Start', 'LEFT': 'Grand Ballroom', 'RIGHT': 'Something Room'},
        'DESC': ''
        'GROUND': ['Do Not Take This Sign Sign']},
    'Grand Ballroom': {
        'DOORS': {'LEFT': 'Wing B', 'RIGHT': 'Wing A'},
        'DESC': '',
        'GROUND': ['Shattered Glass']},
    'Wing A from Grand Ballroom': {
        'DOORS': {'FORWARD': 'Something Room', 'BACK': 'Grand Ballroom', 'LEFT': 'Main Hall', 'RIGHT': 'Start'},
        'DESC': ''},
    'Wing B from Grand Ballroom': {
        'DOORS': {'FORWARD': 'Study', 'BACK': 'Grand Ballroom', 'LEFT': 'Art Gallery', 'RIGHT': 'Main Hall'},
        'DESC': ''},
    'Something Room': {
        'DOORS': {'LEFT': 'Wing A', 'RIGHT': 'Wing C'},
        'DESC': '',
        'GROUND': ['Something item']},
    'Wing A from Something Room': {
        'DOORS': {'FORWARD': 'Grand Ballroom', 'BACK': 'Something Room', 'LEFT': 'Start', 'RIGHT': 'Main Hall'},
        'DESC': ''},
    'Wing C from Something Room': {
        'DOORS': {'FORWARD': 'Library', 'BACK': 'Something Room', 'LEFT': 'Main Hall', 'RIGHT': 'Locked Closet'},
        'DESC': ''},
    'Art Gallery': {
        'DOORS': {'FORWARD': 'Wing B'},
        'DESC': '',
        'GROUND': ['Frame']},
    'Wing B from Art Gallery': {
        'DOORS': {'FORWARD': 'Main Hall', 'BACK': 'Art Gallery', 'LEFT': 'Study', 'RIGHT': 'Grand Ballroom'},
        'DESC': ''},
    'Locked Closet': {
        'DOORS': {'FORWARD': 'Wing C'},
        'DESC': '',
        'SHOP': [''],
        'GROUND': ['Code Sequence #2', 'Shop Howto']},
    'Wing C from Locked Closet': {
        'DOORS': {'FORWARD': 'Main Hall', 'BACK': 'Locked Closet', 'LEFT': 'Something Room', 'RIGHT': 'Library'},
        'DESC': ''},
    'Study': {
        'DOORS': {'LEFT': 'Wing D', 'RIGHT': 'Wing B'},
        'DESC': '',
        'GROUND': ['Fountain Pen']},
    'Wing B from Study': {
        'DOORS': {'FORWARD': 'Grand Ballroom', 'BACK': 'Study', 'LEFT': 'Main Hall', 'RIGHT': 'Art Gallery'},
        'DESC': ''},
    'Wing D from Study': {
        'DOORS': {'FORWARD': 'Library', 'BACK': 'Study', 'LEFT': 'Kitchen', 'RIGHT': 'Long Corridor'},
        'DESC': ''},
    'Library': {
        'DOORS': {'LEFT': 'Wing C', 'RIGHT': 'Wing D'},
        'DESC': '',
        'UP': 'Secret Attic',  #SPECIAL CASE -- MIGHT NEED TWEAKING
        'GROUND': ['Gold-Binded Book']},
    'Secret Attic': {
        'DESC': '',
        'DOWN': 'Library',     #SPECIAL CASE -- MIGHT NEED TWEAKING
        'GROUND': ['Map']},
    'Wing C from Library': {
        'DOORS': {'FORWARD': 'Something Room', 'BACK': 'Library', 'LEFT': 'Locked Closet', 'RIGHT': 'Main Hall'},
        'DESC': ''},
    'Wing D from Library': {
        'DOORS': {'FORWARD': 'Study', 'BACK': 'Library', 'LEFT': 'Long Corridor', 'RIGHT': 'Kitchen'},
        'DESC': ''},
    'Kitchen': {
        'DOORS': {'FORWARD': 'Wing D'},
        'DESC': '',
        'SHOP': ['', '', ''],
        'GROUND': ['Box', 'Shop Howto']},
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
    'Wing A from Main Hall': {
        'DOORS': {'FORWARD': 'Start', 'LEFT': 'Something Room', 'RIGHT': 'Grand Ballroom'},
        'DESC': ''},
    'Wing B from Main Hall': {
        'DOORS': {'FORWARD': 'Art Gallery', 'LEFT': 'Grand Ballroom', 'RIGHT': 'Study'},
        'DESC': ''},
    'Wing C from Main Hall': {
        'DOORS': {'FORWARD': 'Locked Closet', 'LEFT': 'Library', 'RIGHT': 'Something Room'},
        'DESC': ''},
    'Wing D from Main Hall': {
        'DOORS': {'FORWARD': 'Kitchen', 'LEFT': 'Study', 'RIGHT': 'Library'},
        'DESC': ''},
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

worldItems = {
    'welcome sign': {'DESC': ''},
    'do not take this sign sign': {'DESC': ''},
    'map': {'DESC': 'this describes the map'},
    'shovel': {'DESC': 'this describes the shovel'}
    }

class Room(object):
    """Create a room object

    Each room is assumed to have four walls, with one possible door in each.
    Each wall will either have a door or not. No support for closed/open doors yet
    """

    def __init__(self, name, desc, front=True, back=True, left=True, right=True):
        self.name = name
        self.exception = 'Main Hall'
        self.walls = {'front': front, 'back': back, 'left': left, 'right': right}
        self.desc = desc


    def nextTurn(self):
        #prints room name
        # print(self.name)
        # print("=" * len(self.name))

        if self.name not in ['Main Hall from Wing A', 'Main Hall from Wing B', 'Main Hall from Wing C', 'Main Hall from Wing D']:
            print(self.name)
            print("=" * len(self.name))
        else:
            print(self.exception)
            print("=" * len(self.exception))


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
                if prevlocation not in ['Main Hall from Wing A', 'Main Hall from Wing B', 'Main Hall from Wing C', 'Main Hall from Wing D']:
                    name_2 = (f'{self.name} from {prevlocation}')
                else:
                    name_2 = (f'{self.name} from Main Hall')
                list1 = (worldRooms[name_2]['DOORS']).keys()
                for n in list1:
                    print((str(f"{n}: {worldRooms[name_2]['DOORS'][n]}")).title())
            break

class Object(object):
    """Characters class"""

    def __init__(self, name, takeable=True, edible=False):
        self.name = name

    def desc(self, item):
        print(f"Hi I'm {item}")
        #print(worldRooms[location][ground

    def talk_to(self, some_person):
        print(f"{self.name} talks to {some_person}")

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

    #methods with shortened names:
    do_f = do_forward
    do_b = do_back
    do_l = do_left
    do_r = do_right

    def do_look(self, item):
        item = item.lower()
        if item not in worldRooms[location]['GROUND']:
            print('You do not see that item.')
        else:
            print(worldItems[item]['DESC'])
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
            newlocation = worldRooms[location]['DOORS'][user_input]
            prevlocation = location
            location = newlocation

        else:
            print('Sorry, I don\'t recognize that command.  Enter "help" for the list of commands.')


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
        if prevlocation not in ['Main Hall from Wing A', 'Main Hall from Wing B', 'Main Hall from Wing C', 'Main Hall from Wing D']:
            name_5 = str(f'{location} from {prevlocation}')
        else:
            name_5 = (f'{location} from Main Hall')
        newlocation = worldRooms[name_5]['DOORS'][user_input]
        prevlocation = location
        location = newlocation
        if location == 'Main Hall':
            location = str(f'{location} from {prevlocation}')

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
