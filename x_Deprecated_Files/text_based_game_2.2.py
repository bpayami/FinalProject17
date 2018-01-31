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



#Dictionary:

worldRooms = {
    'Start': {
        'DOORS': {'FORWARD': 'Wing A'},
        'DESC': 'You wake up in a room with no memory of how you got there. ...',
        'GROUND': ['', '']},
    'Wing A from Start': {
        'DOORS': {'FORWARD': 'HALLWAY JUNCTION THING A', 'BACK': 'Start', 'LEFT': 'Grand Ballrooom', 'RIGHT': 'Something Room'},
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

#Dictionary -- Wings with Cardinal Directions

worldWings = {
    'Wing A': {
        'NORTH': 'HALLWAY JUNCTION THING A',
        'EAST': 'Something Room',
        'SOUTH': 'Start',
        'WEST': 'Grand Ballroom'},
    'Wing B': {
        'NORTH': 'Study',
        'EAST': 'HALLWAY JUNCTION THING B',
        'SOUTH': 'Grand Ballroom',
        'WEST': 'Art Gallery'},
    'Wing C': {
        'NORTH': 'Library',
        'EAST': 'Locked Closet',
        'SOUTH': 'Something Room',
        'WEST': 'HALLWAY JUNCTION THING C'},
    'Wing D': {
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
                #^^ PICK UP RIGHT HERE THIS WAS WORKING IF YOU DELETE THE DICTIONARY AND RESTORE TO FORMAT OF RIGHT

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
                print(prevlocation)
                list1 = (worldRooms[prevlocation]['DOORS']).keys()
                door = (worldRooms[prevlocation]['DOORS']).values()
                things = (worldRooms[prevlocation]['DOORS']).items()
                for door in list1:
                    print(f'{things}')
            break

"""
        #mimicing available rooms
        for k,v in self.walls.items():
            if v == True:
                if location == 'Wing A':
                    if prevlocation == 'Start':
                        print('yasss booo!')                                           #PICK UP HERE TO WORK
                        list1 = ((worldRooms['Start']['DOORS']).keys()).title()
                        list2 = (worldRooms['Start']['DOORS']).values()
                        for thing in list1:
                            print(f'{thing}: ' + f'{list2}')
                        break
                    #elif prevlocation == 'Grand Ballroom':
                    #    print('')
                    #    break
                    #elif prevlocation == 'Something Room':
                    #    print('')
                    #    break
"""



#Begginning Fancy Stuff
title = 'I still have to think of a title'
print(title)
print(f'=' * len(title))
print(' ')
print('(Type "help" for commands.)')
print(' ')



#prints turn for Start
location = 'Start'
start = Room(location, worldRooms[location]['DESC'], back=False, left=False, right=False)
start.nextTurn()
print(' ')

user_input = str(input('Where would you like to travel? ')).upper()
#this will print 'FORWARD'
#it then needs to reference the direction in the given room


for room in worldRooms[location]:
    newlocation = worldRooms[location]['DOORS'][user_input]

prevlocation = location
location = newlocation
print(location)
print(' ')

wingA = Wing(location, 'do i need an actual string here?')
wingA.altnextTurn()

#print(prevlocation)
#print(newlocation)

#direction = Room({current_room}, worldRooms[{current_room}][DESC], back=False, left=False, right=False)
#direction.nextTurn()



"""

IDK IF ILL NEED THIS BUT THIS IS FROM WINGS CLASS

#prints which direction is which room
        for k, v in self.walls.items():
            if v == True:
                if k == 'north':
                    print(f'North: '+ worldRooms[self.name]['FORWARD'])  #this needs to reference new dictionary
                elif k == 'east':
                    print(f'East: ' + worldRooms[self.name]['BACK'])
                elif k == 'south':
                    print(f'South: ' + worldRooms[self.name]['LEFT'])
                elif k == 'west':
                    print(f'West: ' + worldRooms[self.name]['RIGHT'])
                else:
                    break
                #^^ PICK UP RIGHT HERE THIS WAS WORKING IF YOU DELETE THE DICTIONARY AND RESTORE TO FORMAT OF RIGHT

"""