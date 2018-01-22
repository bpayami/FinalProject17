#TO-DO LIST
    #GAME CONTENT
        #fill in all parameters into worldRooms dictionary
        #write objects into room descriptions (and move sample items into proper rooms)
        #finish list of objects
        #print little commentaries for take, use, eat commands for certain objects
            #perhaps add into class as an addional desc and a contional statement if current.takeDesc != '': print(current.takeDesc) etc..
                #EXAMPLES
                    #take glass - ow
                    #eat code - WHY WOULD YOU DO THAT YOU IDIOT??! I hope you have a good memory...
                    #etc.
    #CHANGING ROOMS
        #locked closet -- PICK UP PROGRESS AT LINE 581!!!
        #get rid of parameters completely for worldWings and if wings in while loop for simplification purposes?
    #GAME ENDING
        #figure out once inside room
        #figure out ending message
        #animated banner?
    #MISC.
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
    |    Gallery    O______ B ______  |  | ??? |  |  ______ C ______0    Closet     |
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
        'GROUND': ['Welcome Sign', 'Code #1']},
    'Wing A from Start': {
        'DOORS': {'FORWARD': 'Main Hall', 'BACK': 'Start', 'LEFT': 'Grand Ballroom', 'RIGHT': 'Something Room'},
        'DESC': ''},
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
        'GROUND': ['Do Not Take This Sign Sign', 'Something item']},
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
        'GROUND': ['Fountain Pen', 'Code #2']},
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
        'DOORS': {'FORWARD': 'Long Corridor', 'LEFT': 'Wing C', 'RIGHT': 'Wing B'},
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
        'DOORS': {'FORWARD': 'Final Room', 'BACK': 'Wing D'},
        'DESC': ''},
    'Wing D from Long Corridor': {
        'DOORS': {'FORWARD': 'Kitchen', 'LEFT': 'Study', 'RIGHT': 'Library'},
        'DESC': ''},
    'Locked Doors': {
        'DOORS': {'FORWARD': 'Final Room', 'BACK': 'Wing D'},
        'DESC': ''},
    'Final Room': {
        'DOORS': {'BACK': 'Wing B'},
        'DESC': ''},
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


class Room(object):
    """Create a room object
    Each room is assumed to have four walls, with one possible door in each.
    Each wall will either have a door or not. No support for closed/open doors yet
    """

    def __init__(self, name, front=True, back=True, left=True, right=True, locked=False):
        self.name = name
        self.exception = 'Main Hall'
        self.walls = {'front': front, 'back': back, 'left': left, 'right': right}
        self.desc = worldRooms[location]['DESC']
        self.locked = locked


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
    def __init__(self, official, desc, names, takeable=True, edible=False, usable=False, validity=False):
        self.official = official
        self.desc = desc
        self.names = names
        self.takeable = takeable
        self.edible = edible
        self.usable = usable

worldItems = [
    Object('Welcome Sign', 'The sign reads...', ['welcome sign', 'welcome'], takeable=False),
    Object('Do Not Take This Sign Sign','this is a description', ['do not take this sign sign', 'sign']),
    Object('Map', 'this describes the map', ['map']),
    Object('Shattered Glass', 'this describes the glass', ['shattered glass', 'glass'], edible=True, usable=True),
    Object('Frame', 'this describes the frame', ['frame']),
    Object('Code #1', 'this describes the first piece of code', ['code #1', 'piece of code', 'code (1/2)']),
    Object('Code #2', 'this describes the second piece of code', ['code #2', 'piece of code', 'code'])
    ]


class TextAdventureCmd(cmd.Cmd):
    prompt = '\n> '

    def default(self, arg):
        print('I do not understand that command. Type "help" for a list of commands.')

    def do_quit(self, arg):
        """Quit the game."""
        global quit
        quit = 'True'
        return True

    def do_forward(self, arg):
        """Move in the forward direction, if possible."""
        global user_input
        user_input = 'FORWARD'
        return True

    def do_back(self,arg):
        """Move in the back direction, if possible."""
        global user_input
        user_input = 'BACK'
        return True

    def do_left(self, arg):
        """Move in the left direction, if possible."""
        global user_input
        user_input = 'LEFT'
        return True

    def do_right(self, arg):
        """Move in the right direction, if possible."""
        global user_input
        user_input = 'RIGHT'
        return True

    #methods with shortened names:
    do_f = do_forward
    do_b = do_back
    do_l = do_left
    do_r = do_right


    def do_look(self, item):
        """look <item> - Look at an item within the room."""

        choice = item.lower()
        current = ''

        for item in worldItems:
            if choice in item.names:
                current = item
            if choice not in item.names:
                validity = 'no'

        for item in worldItems:
            if choice in item.names:
                validity = 'yes'
                current.validity = True

        for item in worldItems:
            if choice in item.names:
                if current.official in worldRooms[location]['GROUND']:
                    print(current.desc)
                if current.official not in worldRooms[location]['GROUND']:
                    print('You do not see that item.')

        if validity != 'yes':
            print('You do not see that item.')


    def do_take(self, item):
        """take <item> - Take an item within the room."""

        choice = item.lower()
        current = ''

        for item in worldItems:
            if choice in item.names:
                current = item
            if choice not in item.names:
                validity = 'no'

        for item in worldItems:
            if choice in item.names:
                validity = 'yes'
                current.validity = True

        for item in worldItems:
            if choice in item.names:
                if current.official in worldRooms[location]['GROUND']:
                    if current.takeable == True:
                        inventory.append(current.official)
                        print(f'"{current.official}" has been added to your inventory.')
                    else:
                        print('You can not take that item.')
                if current.official not in worldRooms[location]['GROUND']:
                    print('That item is not here to take.')

        if validity != 'yes':
            print('That item is not here to take.')


    def do_drop(self, item):
        """drop <item> - Drop an item and remove it from your inventory."""

        choice = item.title()

        if choice in inventory:
            inventory.remove(choice)
            print(inventory)
        else:
            print('You do not have that item in your inventory to remove.')


    def do_eat(self, item):
        """eat <item> - Eat an item that is in your inventory."""

        #from take function
        choice = item.lower()
        current = ''

        for item in worldItems:
            if choice in item.names:
                current = item

        if choice.title() in inventory:
            if current.edible == True:
                inventory.remove(choice.title())
                print(f'You just ate "{choice}."')
            else:
                print('You can not eat that item.')
        else:
            print('That item is not in your inventory to eat.')


    def do_use(self, item):
        """use <item> - Use an item that is in your inventory."""

        #from take function
        choice = item.lower()
        current = ''

        for item in worldItems:
            if choice in item.names:
                current = item

        if choice.title() in inventory:
            if current.usable == True:
                inventory.remove(choice.title())
                print(f'You just used your "{choice}."')
            else:
                print('You can not use that item.')
        else:
            print('That item is not in your inventory to use.')


    def do_inventory(self, arg):
        """This will show your current inventory."""
        print(inventory)

    def do_map(self, arg):
        """View the map of the mansion."""
        map()



#Begginning Fancy Stuff
title = 'I still have to think of a title'
print(title)
print(f'=' * len(title))
print(' ')
print('(Type "help" for commands.)\n')


#Beginning Conditions
location = 'Start'
inventory = ['Key']



while True:
    if location != 'Wing A' or 'Wing B' or 'Wing C' or 'Wing D' or 'Locked Closet':
        location = location
        parameters = {
            'start': Room(location, back=False, left=False, right=False),
            'grandballroom': Room(location, front=False, back=False),
            'somethingroom': Room(location, front=False, back=False),
            'artgallery': Room(location, back=False, left=False, right=False),
            'lockedcloset': Room(location, front=False, back=False, left=False, right=False, locked=True),
            'study': Room(location, front=False, back=False),
            'library': Room(location, front=False, back=False), #has special case of 'up'
            'secretattic': Room(location, front=False, back=False, left=False, right=False), #ADD DOWN=FALSE TO CLASS
            'kitchen': Room(location, back=False, left=False, right=False),
            'longcorridor': Room('Locked Doors', left=False, right=False),
            'lockeddoors': Room(location, left=False, right=False),
            'finalroom': Room(location, front=False, back=False, left=False, right=False, locked=True),
            'mainhallfromwinga': Room(location, front=False, back=False),
            'mainhallfromwingb': Room(location, front=False, back=False),
            'mainhallfromwingc': Room(location, front=False, back=False),
            'mainhallfromwingd': Room(location, front=False, back=False)}
        location_modified = location.lower()
        if ' ' in (location_modified):
            location_modified = location_modified.replace(" ", "")
        self = parameters[location_modified]
        self.nextTurn()
        print(location)

        TextAdventureCmd().cmdloop()

        if quit == 'True':
            print('\n\nThanks for playing!')
            break

        if user_input == 'FORWARD' or 'BACK' or 'LEFT' or 'RIGHT':
            print(' \n \n')
            newlocation = worldRooms[location]['DOORS'][user_input]
            prevlocation = location
            location = newlocation

        else:
            print('Sorry, I don\'t recognize that command.  Enter "help" for the list of commands.')


    if location == 'Final Room':
        print(location)
        print("=" * len(location))

        finalRoom = Room(location, worldRooms[location]['DESC'], front=False, back=False, left=False, right=False, locked=True)
        fr = finalRoom
        if fr.locked == True:
            if 'Code #1' and 'Code #2' in inventory:
                print('Congratulations!  You have found both of the code sequences! Enter "look codes" to see the sequences again.')
                while True:
                    displayCodes = (input(f'{inventory} \n\n> ')).lower()
                    if displayCodes == 'look codes':
                        print("""     * Code #1 -- 42 72 69 65 6c 6c 61\n     * Code #2 -- 41 70 72 69 6c""")
                        while True:
                            code1 = input('\nEnter code sequence #1:  ')
                            if code1 == '42 72 69 65 6c 6c 61':
                                print('   processing...\n   processing...\n')
                                code2 = input('Enter code sequence #2:  ')
                                if code2 == '41 70 72 69 6c':
                                    print('   processing...\n   processing...\n')
                                    print('You\'ve entered the proper codes to escape!!\nto be continued...')
                                    break
                                else:
                                    print('Hmm... you must have entered the code wrong.  Try entering it again.\n')
                                    continue
                            else:
                                print('Hmm... you must have entered the code wrong.  Try entering it again.\n')
                                continue

                    else:
                        print('\nSorry, I don\'t recognize that command.  Try entering "look codes" again.')
                        continue

            else:
                print('This room is locked and you are unable to enter without the needed escape codes. Keep looking for the codes!\n')
                prevlocation = 'Long Corridor'
                location = 'Wing D'

    if location == 'Locked Closet':
        print(location)
        print("=" * len(location))

        lockedCloset = Room(location, worldRooms[location]['DESC'], front=False, back=False, left=False, right=False, locked=True)
        lc = lockedCloset
        if lc.locked == True:
            if 'Key' in inventory:
                while True:
                    useKey = (input('You need to use a key to unlock this door. \n\n> ')).lower()
                    if useKey == 'usekey':
                        print('You have unlocked this door in theory...\n\n')

                        """
                        while True:
                            code1 = input('\nEnter code sequence #1:  ')
                            if code1 == '42 72 69 65 6c 6c 61':
                                print('   processing...\n   processing...\n')
                                code2 = input('Enter code sequence #2:  ')
                                if code2 == '41 70 72 69 6c':
                                    print('   processing...\n   processing...\n')
                                    print('You\'ve entered the proper codes to escape!!\nto be continued...')
                                    break
                                else:
                                    print('Hmm... you must have entered the code wrong.  Try entering it again.\n')
                                    continue
                            else:
                                print('Hmm... you must have entered the code wrong.  Try entering it again.\n')
                                continue
                        """

                    else:
                        print('\nSorry, I don\'t recognize that command.  Try entering "use key" again.')
                        continue

            else:
                print('You need a key to unlock this door.\n')
                prevlocation = 'Locked Closet'
                location = 'Wing C'


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
        if user_input not in ['FORWARD', 'BACK', 'LEFT', 'RIGHT']:
            if user_input == 'F':
                user_input = 'FORWARD'
            if user_input == 'B':
                user_input = 'BACK'
            if user_input == 'L':
                user_input = 'LEFT'
            if user_input == 'R':
                user_input = 'RIGHT'
            if user_input not in ['FORWARD', 'BACK', 'LEFT', 'RIGHT']:
                user_input = str(input('\nSorry, you can\'t go that way.  Which way would you like to go next? ')).upper()
                if user_input not in ['FORWARD', 'BACK', 'LEFT', 'RIGHT']:
                    if user_input == 'F':
                        user_input = 'FORWARD'
                    if user_input == 'B':
                        user_input = 'BACK'
                    if user_input == 'L':
                        user_input = 'LEFT'
                    if user_input == 'R':
                        user_input = 'RIGHT'
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
