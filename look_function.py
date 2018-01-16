#TO-DO LIST
 +    #finish list of objects
 +    #Fix long corridor in association with Wing D
 +    #secret attic
 +    #Figure out locked closet and locked door -perhaps checks inventory for code or true/false for open/close
 +    #add something into class Room to print what objects are in the room (reference ground in dictionary) -- or just write into description
 +    #ALL OF THESE WILL BE RATHER SIMPLE ONCE SHORT NAME / OFFICIAL NAME ISSUE IS RESOLVED
 +        #take function - started but fix
 +        #drop function
 +        #eat function?
 +        #use function?
 +    #write in story line
 +    #randomized monster?
 +    #perhaps have map printed in beginning? Have map print periodically?
 +
 +import cmd
 +
 +def map():
 +    print("""
 +
 +
 +                                    +---------------+
 +                                    |               |
 +        T H E   M A P               |               |
 +              O F                   |               |
 +                                    |    Kitchen    |
 +            T H E   M A N S I O N   |               |
 +                                    |               |
 +                                    |               |
 +                    +---------------+-------O-------+---------------+
 +                    |               |      | |      |               |
 +                    |               |      | |      |               |
 +                    |               |______| |______|               |
 +                    |     Study     O______ D ______O    Library    |
 +                    |               |      | |      |               |
 +                    |               |      | |      |               |
 +                    |               |      | |      |               |
 +    +---------------+-------O-------+______| |______+-------O-------+---------------+
 +    |               |      | |      |  ____   ____  |      | |      |               |
 +    |               |      | |      | |    | |    | |      | |      |               |
 +    |      Art      |______| |______| |  +--0--+  | |______| |______|    Locked     |
 +    |    Gallery    O______ B ______  |  | ??? |  |  ______ C ______O    Closet     |
 +    |               |      | |      | |  +-----+  | |      | |      |               |
 +    |               |      | |      | |___________| |      | |      |               |
 +    |               |      | |      |______   ______|      | |      |               |
 +    +---------------+-------O-------+      | |      +-------O-------+---------------+
 +                    |               |      | |      |               |
 +                    |               |      | |      |               |
 +                    |  Grand        |______| |______|  Something    |
 +                    |   Ballroom    O______ A ______O   Room        |
 +                    |               |      | |      |               |
 +                    |               |      | |      |               |
 +                    |               |      | |      |               |
 +                    +---------------+-------O-------+---------------+
 +                                    |               |
 +                                    |               |
 +                                    |   Start       |
 +                                    |     Here...   |
 +                                    |               |
 +                                    |               |
 +                                    |               |
 +                                    +---------------+
 +
 +    """)
 +
 +worldRooms = {
 +    'Start': {
 +        'DOORS': {'FORWARD': 'Wing A'},
 +        'DESC': 'You wake up in a room with no memory of how you got there. ...',
 +        'GROUND': ['Welcome Sign']},
 +    'Wing A from Start': {
 +        'DOORS': {'FORWARD': 'Main Hall', 'BACK': 'Start', 'LEFT': 'Grand Ballroom', 'RIGHT': 'Something Room'},
 +        'DESC': ''},
 +    'Grand Ballroom': {
 +        'DOORS': {'LEFT': 'Wing B', 'RIGHT': 'Wing A'},
 +        'DESC': '',
 +        'GROUND': ['Shattered Glass']},
 +    'Wing A from Grand Ballroom': {
 +        'DOORS': {'FORWARD': 'Something Room', 'BACK': 'Grand Ballroom', 'LEFT': 'Main Hall', 'RIGHT': 'Start'},
 +        'DESC': ''},
 +    'Wing B from Grand Ballroom': {
 +        'DOORS': {'FORWARD': 'Study', 'BACK': 'Grand Ballroom', 'LEFT': 'Art Gallery', 'RIGHT': 'Main Hall'},
 +        'DESC': ''},
 +    'Something Room': {
 +        'DOORS': {'LEFT': 'Wing A', 'RIGHT': 'Wing C'},
 +        'DESC': '',
 +        'GROUND': ['Do Not Take This Sign Sign', 'Something item']},
 +    'Wing A from Something Room': {
 +        'DOORS': {'FORWARD': 'Grand Ballroom', 'BACK': 'Something Room', 'LEFT': 'Start', 'RIGHT': 'Main Hall'},
 +        'DESC': ''},
 +    'Wing C from Something Room': {
 +        'DOORS': {'FORWARD': 'Library', 'BACK': 'Something Room', 'LEFT': 'Main Hall', 'RIGHT': 'Locked Closet'},
 +        'DESC': ''},
 +    'Art Gallery': {
 +        'DOORS': {'FORWARD': 'Wing B'},
 +        'DESC': '',
 +        'GROUND': ['Frame']},
 +    'Wing B from Art Gallery': {
 +        'DOORS': {'FORWARD': 'Main Hall', 'BACK': 'Art Gallery', 'LEFT': 'Study', 'RIGHT': 'Grand Ballroom'},
 +        'DESC': ''},
 +    'Locked Closet': {
 +        'DOORS': {'FORWARD': 'Wing C'},
 +        'DESC': '',
 +        'SHOP': [''],
 +        'GROUND': ['Code Sequence #2', 'Shop Howto']},
 +    'Wing C from Locked Closet': {
 +        'DOORS': {'FORWARD': 'Main Hall', 'BACK': 'Locked Closet', 'LEFT': 'Something Room', 'RIGHT': 'Library'},
 +        'DESC': ''},
 +    'Study': {
 +        'DOORS': {'LEFT': 'Wing D', 'RIGHT': 'Wing B'},
 +        'DESC': '',
 +        'GROUND': ['Fountain Pen']},
 +    'Wing B from Study': {
 +        'DOORS': {'FORWARD': 'Grand Ballroom', 'BACK': 'Study', 'LEFT': 'Main Hall', 'RIGHT': 'Art Gallery'},
 +        'DESC': ''},
 +    'Wing D from Study': {
 +        'DOORS': {'FORWARD': 'Library', 'BACK': 'Study', 'LEFT': 'Kitchen', 'RIGHT': 'Long Corridor'},
 +        'DESC': ''},
 +    'Library': {
 +        'DOORS': {'LEFT': 'Wing C', 'RIGHT': 'Wing D'},
 +        'DESC': '',
 +        'UP': 'Secret Attic',  #SPECIAL CASE -- MIGHT NEED TWEAKING
 +        'GROUND': ['Gold-Binded Book']},
 +    'Secret Attic': {
 +        'DESC': '',
 +        'DOWN': 'Library',     #SPECIAL CASE -- MIGHT NEED TWEAKING
 +        'GROUND': ['Map']},
 +    'Wing C from Library': {
 +        'DOORS': {'FORWARD': 'Something Room', 'BACK': 'Library', 'LEFT': 'Locked Closet', 'RIGHT': 'Main Hall'},
 +        'DESC': ''},
 +    'Wing D from Library': {
 +        'DOORS': {'FORWARD': 'Study', 'BACK': 'Library', 'LEFT': 'Long Corridor', 'RIGHT': 'Kitchen'},
 +        'DESC': ''},
 +    'Kitchen': {
 +        'DOORS': {'FORWARD': 'Wing D'},
 +        'DESC': '',
 +        'SHOP': ['', '', ''],
 +        'GROUND': ['Box', 'Shop Howto']},
 +    'Wing D from Kitchen': {
 +        'DOORS': {'FORWARD': 'Long Corridor', 'BACK': 'Kitchen', 'LEFT': 'Library', 'RIGHT': 'Study'},
 +        'DESC': ''},
 +    'Main Hall from Wing A': {
 +        'DOORS': {'LEFT': 'Wing B', 'RIGHT': 'Wing C'},
 +        'DESC': ''},
 +    'Main Hall from Wing B': {
 +        'DOORS': {'LEFT': 'Wing D', 'RIGHT': 'Wing A'},
 +        'DESC': ''},
 +    'Main Hall from Wing C': {
 +        'DOORS': {'LEFT': 'Wing A', 'RIGHT': 'Wing D'},
 +        'DESC': ''},
 +    'Main Hall from Wing D': {
 +        'DOORS': {'LEFT': 'Wing C', 'RIGHT': 'Wing B'},
 +        'DESC': ''},
 +    'Wing A from Main Hall': {
 +        'DOORS': {'FORWARD': 'Start', 'LEFT': 'Something Room', 'RIGHT': 'Grand Ballroom'},
 +        'DESC': ''},
 +    'Wing B from Main Hall': {
 +        'DOORS': {'FORWARD': 'Art Gallery', 'LEFT': 'Grand Ballroom', 'RIGHT': 'Study'},
 +        'DESC': ''},
 +    'Wing C from Main Hall': {
 +        'DOORS': {'FORWARD': 'Locked Closet', 'LEFT': 'Library', 'RIGHT': 'Something Room'},
 +        'DESC': ''},
 +    'Wing D from Main Hall': {
 +        'DOORS': {'FORWARD': 'Kitchen', 'LEFT': 'Study', 'RIGHT': 'Library'},
 +        'DESC': ''},
 +    'Long Corridor': {
 +        'DESC': '',
 +        'FORWARD': 'Locked Room',
 +        'BACK': 'Wing B'},
 +    'Locked Room': {
 +        'DESC': '',
 +        'FORWARD': '',
 +        'BACK': ''},
 +    }
 +
 +worldWings = {
 +    'Wing A': {
 +        'DESC': 'write desc',
 +        'NORTH': 'Main Hall from Wing A',
 +        'EAST': 'Something Room',
 +        'SOUTH': 'Start',
 +        'WEST': 'Grand Ballroom'},
 +    'Wing B': {
 +        'DESC': 'write desc',
 +        'NORTH': 'Study',
 +        'EAST': 'Main Hall from Wing B',
 +        'SOUTH': 'Grand Ballroom',
 +        'WEST': 'Art Gallery'},
 +    'Wing C': {
 +        'DESC': 'write desc',
 +        'NORTH': 'Library',
 +        'EAST': 'Locked Closet',
 +        'SOUTH': 'Something Room',
 +        'WEST': 'Main Hall from Wing C'},
 +    'Wing D': {
 +        'DESC': 'write desc',
 +        'NORTH': 'Kitchen',
 +        'EAST': 'Library',
 +        'SOUTH': 'Main Hall from Wing D',
 +        'WEST': 'Study'}
 +    }
 +
 +currentItem = {}
 +
 +
 +class Room(object):
 +    """Create a room object
 +
 +    Each room is assumed to have four walls, with one possible door in each.
 +    Each wall will either have a door or not. No support for closed/open doors yet
 +    """
 +
 +    def __init__(self, name, desc, front=True, back=True, left=True, right=True):
 +        self.name = name
 +        self.exception = 'Main Hall'
 +        self.walls = {'front': front, 'back': back, 'left': left, 'right': right}
 +        self.desc = desc
 +
 +
 +    def nextTurn(self):
 +        #prints room name
 +        # print(self.name)
 +        # print("=" * len(self.name))
 +
 +        if self.name not in ['Main Hall from Wing A', 'Main Hall from Wing B', 'Main Hall from Wing C', 'Main Hall from Wing D']:
 +            print(self.name)
 +            print("=" * len(self.name))
 +        else:
 +            print(self.exception)
 +            print("=" * len(self.exception))
 +
 +
 +        #prints description
 +        print(self.desc)
 +
 +        #prints available doors
 +        for k, v in self.walls.items():
 +            if v:
 +                print(f"You see a door to the {k}.")
 +
 +        print(' ')
 +
 +        #prints which direction is which room
 +        for k, v in self.walls.items():
 +            if v == True:
 +                if k == 'front':
 +                    print(f'Forward: '+ worldRooms[self.name]['DOORS']['FORWARD'])
 +                elif k == 'back':
 +                    print(f'Back: ' + worldRooms[self.name]['DOORS']['BACK'])
 +                elif k == 'left':
 +                    print(f'Left: ' + worldRooms[self.name]['DOORS']['LEFT'])
 +                elif k == 'right':
 +                    print(f'Right: ' + worldRooms[self.name]['DOORS']['RIGHT'])
 +                else:
 +                    break
 +
 +class Wing(object):
 +    """Blah blah blah description"""
 +
 +    def __init__(self, name, desc, north=True, south=True, east=True, west=True):
 +        self.name = name
 +        self.walls = {'north': north, 'south': south, 'east': east, 'west': west}
 +        self.desc = desc
 +
 +    def altnextTurn(self):
 +        #prints room name
 +        print(self.name)
 +        print("=" * len(self.name))
 +
 +        #prints description
 +        print(self.desc)
 +        print(' ')
 +
 +        #mimicing available rooms
 +        for k,v in self.walls.items():
 +            if v == True:
 +                if prevlocation not in ['Main Hall from Wing A', 'Main Hall from Wing B', 'Main Hall from Wing C', 'Main Hall from Wing D']:
 +                    name_2 = (f'{self.name} from {prevlocation}')
 +                else:
 +                    name_2 = (f'{self.name} from Main Hall')
 +                list1 = (worldRooms[name_2]['DOORS']).keys()
 +                for n in list1:
 +                    print((str(f"{n}: {worldRooms[name_2]['DOORS'][n]}")).title())
 +            break
 +
 +class Object(object):
 +    def __init__(self, official, desc, names, takeable=True, edible=False):
 +        self.official = official
 +        self.desc = desc
 +        self.names = names
 +
 +worldItems = [
 +    Object('Welcome Sign', 'The sign reads...', ['sign', 'welcome sign', 'welcome', 'sign']),
 +    Object('Do Not Take This Sign Sign','this is a description', ['do not take this sign sign', 'sign']),
 +    Object('Map', 'this describes the map', ['map'])
 +    ]
 +
 +
 +class TextAdventureCmd(cmd.Cmd):
 +    prompt = '\n> '
 +
 +    def default(self, arg):
 +        print('I do not understand that command. Type "help" for a list of commands.')
 +
 +
 +    def do_quit(self, arg):
 +        """Quit the game."""
 +        global quit
 +        quit = 'True'
 +        return True
 +
 +
 +    def do_forward(self, arg):
 +        """Move in the forward direction, if possible."""
 +        global user_input
 +        user_input = 'FORWARD'
 +        return True
 +
 +    def do_back(self,arg):
 +        """Move in the back direction, if possible."""
 +        global user_input
 +        user_input = 'BACK'
 +        return True
 +
 +    def do_left(self, arg):
 +        """Move in the left direction, if possible."""
 +        global user_input
 +        user_input = 'LEFT'
 +        return True
 +
 +    def do_right(self, arg):
 +        """Move in the right direction, if possible."""
 +        global user_input
 +        user_input = 'RIGHT'
 +        return True
 +
 +    #methods with shortened names:
 +    do_f = do_forward
 +    do_b = do_back
 +    do_l = do_left
 +    do_r = do_right
 +
 +
 +    def do_look(self, item):
 +        """look <item> - Look at an item within the room."""
 +
 +        choice = item.lower()
 +        current = ''
 +
 +        for item in worldItems:
 +            if choice in item.names:
 +                current = item
 +
 +        while True:
 +            if choice not in item.names:
 +                print('You do not see that item.')
 +                break
 +            if choice in item.names:
 +                if current.official not in worldRooms[location]['GROUND']:
 +                    print('You do not see that item.')
 +                break
 +            else:
 +                print(current.desc)
 +                break
 +
 +
 +
 +    def do_take(self, item):
 +        """take <item> - Take an item within the room."""
 +        item = item.title()
 +
 +        direct_name = worldRooms[location]['GROUND']
 +        ground_objects = worldRooms[location]['GROUND']
 +        for n in ground_objects:
 +            indirect_name = worldItems[n]['ALTNAMES']
 +
 +        if item not in direct_name and item not in indirect_name:
 +            print('That item is not here to take.')
 +
 +        if worldItems[direct_name]['TAKEABLE'] == False:
 +                print('You can not take that item.')
 +
 +        else:
 +            if item in direct_name:
 +                inventory.append(item.lower())
 +                print(f'The ' + item.lower() + ' has been added to your inventory')
 +            if item in indirect_name:
 +                print('this is not working quite yet')
 +
 +    def do_inventory(self, arg):
 +        """This will show your current inventory"""
 +        print(inventory)
 +
 +#Begginning Fancy Stuff
 +title = 'I still have to think of a title'
 +print(title)
 +print(f'=' * len(title))
 +print(' ')
 +print('(Type "help" for commands.)')
 +print(' ')
 +
 +
 +#prints turn for Start
 +location = 'Start'
 +inventory = []
 +
 +
 +
 +while True:
 +    if location != 'Wing A' or 'Wing B' or 'Wing C' or 'Wing D':
 +        location = location
 +        parameters = {
 +            'start': Room(location, worldRooms[location]['DESC'], back=False, left=False, right=False),
 +            'grandballroom': Room(location, worldRooms[location]['DESC'], front=False, back=False),
 +            'somethingroom': Room(location, worldRooms[location]['DESC'], front=False, back=False),
 +            'artgallery': Room(location, worldRooms[location]['DESC'], back=False, left=False, right=False),
 +            'locked room': Room(location, worldRooms[location]['DESC'], back=False, left=False, right=False),
 +            'study': Room(location, worldRooms[location]['DESC'], front=False, back=False),
 +            'library': Room(location, worldRooms[location]['DESC'], front=False, back=False), #has special case of 'up'
 +            'secretattic': Room(location, worldRooms[location]['DESC'], front=False, back=False, left=False, right=False), #ADD DOWN=FALSE TO CLASS
 +            'kitchen': Room(location, worldRooms[location]['DESC'], back=False, left=False, right=False),
 +            'mainhallfromwinga': Room(location, worldRooms[location]['DESC'], front=False, back=False),
 +            'mainhallfromwingb': Room(location, worldRooms[location]['DESC'], front=False, back=False),
 +            'mainhallfromwingc': Room(location, worldRooms[location]['DESC'], front=False, back=False),
 +            'mainhallfromwingd': Room(location, worldRooms[location]['DESC'], front=False, back=False)}
 +        location_modified = location.lower()
 +        if ' ' in (location_modified):
 +            location_modified = location_modified.replace(" ", "")
 +        self = parameters[location_modified]
 +        self.nextTurn()
 +
 +        TextAdventureCmd().cmdloop()
 +
 +        if quit == 'True':
 +            print('\n\nThanks for playing!')
 +            break
 +
 +        if user_input == 'FORWARD' or 'BACK' or 'LEFT' or 'RIGHT':
 +            print(' \n \n')
 +            newlocation = worldRooms[location]['DOORS'][user_input]
 +            prevlocation = location
 +            location = newlocation
 +
 +        else:
 +            print('Sorry, I don\'t recognize that command.  Enter "help" for the list of commands.')
 +
 +
 +    if location == 'Wing A' or 'Wing B' or 'Wing C' or 'Wing D':
 +        location = location
 +        parameters = {
 +            'winga': Wing(location, worldWings[location]['DESC']),
 +            'wingb': Wing(location, worldWings[location]['DESC']),
 +            'wingc': Wing(location, worldWings[location]['DESC']),
 +            'wingd': Wing(location, worldWings[location]['DESC'])}
 +        location_modified = location.lower()
 +        if ' ' in (location_modified):
 +            location_modified = location_modified.replace(" ", "")
 +        self = parameters[location_modified]
 +        self.altnextTurn()
 +        print(' ')
 +        user_input = str(input('Which way would you like to go next? ')).upper()
 +        if user_input not in ['FORWARD', 'BACK', 'LEFT', 'RIGHT']:
 +            if user_input == 'F':
 +                user_input = 'FORWARD'
 +            if user_input == 'B':
 +                user_input = 'BACK'
 +            if user_input == 'L':
 +                user_input = 'LEFT'
 +            if user_input == 'R':
 +                user_input = 'RIGHT'
 +        print(' \n \n')
 +        if prevlocation not in ['Main Hall from Wing A', 'Main Hall from Wing B', 'Main Hall from Wing C', 'Main Hall from Wing D']:
 +            name_5 = str(f'{location} from {prevlocation}')
 +        else:
 +            name_5 = (f'{location} from Main Hall')
 +        newlocation = worldRooms[name_5]['DOORS'][user_input]
 +        prevlocation = location
 +        location = newlocation
 +        if location == 'Main Hall':
 +            location = str(f'{location} from {prevlocation}')
 +
 +    else:
 +        print('Sorry, you are unable to go in that direction.')
 +