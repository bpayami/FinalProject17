
import cmd

#visual 'map' of the game that the user can call to see from within the cmd loop
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
                    |     Grand     |______| |______|    Trophy     |
                    |    Ballroom   O______ A ______O     Room      |
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

#dictionary containing information for all rooms in world
worldRooms = {
    'Start': {
        'DOORS': {'FORWARD': 'Wing A'},
        'DESC': 'You wake up in a room with no memory of how you got there. The last thing you remember was freaking out over midterms -- so how did you end up here?\nYou slowly stagger to your feet and try to get your bearings.  Surveying the room for any hints as to where you could be you notice a welcome sign\non the other side of the room-- Hmmm... you wonder what it says',
        'GROUND': ['Welcome Sign']},
    'Wing A from Start': {
        'DOORS': {'FORWARD': 'Main Hall', 'BACK': 'Start', 'LEFT': 'Grand Ballroom', 'RIGHT': 'Trophy Room'}},
    'Grand Ballroom': {
        'DOORS': {'LEFT': 'Wing B', 'RIGHT': 'Wing A'},
        'DESC': 'Wow what a gorgeous room!  It has tall ceilings, an expansive dance floor, and a glittering chandelier!  Near the edge of the dancefloor you notice some shattered glass and in the opposite corner there is an abandoned pair of heels.  There\'s also what seems to be a trapdoor in the far corner in the room.',
        'GROUND': ['Shattered Glass', 'Trapdoor', 'Dancefloor', 'Chandelier', 'High Heels']},
    'Wing A from Grand Ballroom': {
        'DOORS': {'FORWARD': 'Trophy Room', 'BACK': 'Grand Ballroom', 'LEFT': 'Main Hall', 'RIGHT': 'Start'},},
    'Wing B from Grand Ballroom': {
        'DOORS': {'FORWARD': 'Study', 'BACK': 'Grand Ballroom', 'LEFT': 'Art Gallery', 'RIGHT': 'Main Hall'}},
    'Trophy Room': {
        'DOORS': {'LEFT': 'Wing A', 'RIGHT': 'Wing C'},
        'DESC': 'Looking around in awe, you notice that the trophy room is more like a Magnet Memorabilia Hall of Fame! The room is full of glass shelves with various items and objects on display.  A couple displays that catch your eye is a rubber band, a virendragon plush, a copy of Arthur\'s speakeasy performance, and a Purdue University acceptance letter.',
        'GROUND': ['Rubber Band', 'Virendragon', 'Arthur\'s Speakeasy Performance', 'Purdue Acceptance Letter']},
    'Wing A from Trophy Room': {
        'DOORS': {'FORWARD': 'Grand Ballroom', 'BACK': 'Trophy Room', 'LEFT': 'Start', 'RIGHT': 'Main Hall'}},
    'Wing C from Trophy Room': {
        'DOORS': {'FORWARD': 'Library', 'BACK': 'Trophy Room', 'LEFT': 'Main Hall', 'RIGHT': 'Locked Closet'}},
    'Art Gallery': {
        'DOORS': {'FORWARD': 'Wing B'},
        'DESC': 'You can\'t help but feel on edge as you enter into the room, not knowing what to expect. Near the very entrance you see a sign with text written on it. On one of the side tables you see, a moose costume?? You continue around the room to take in all the artwork. You see a Harambe tribute that truly does him justice. You also see a closed curtain with three different spotlights shining down on it. And wait... is that the Mona Lisa?!?',
        'GROUND': ['Do Not Take This Sign Sign', 'Moose Costume', 'Mona Lisa', 'Harambe Tribute', 'Code #1', 'Curtain']},
    'Wing B from Art Gallery': {
        'DOORS': {'FORWARD': 'Main Hall', 'BACK': 'Art Gallery', 'LEFT': 'Study', 'RIGHT': 'Grand Ballroom'}},
    'Study': {
        'DOORS': {'LEFT': 'Wing D', 'RIGHT': 'Wing B'},
        'DESC': 'In the center of the room is a desk with a spinny chair (yay!)  On top of the desk sits a mug and you hear the satisfying sound of the printer finish printing something.  There\'s also a pile of documents and handwritten responses sitting on the desk... Are they DBQ\'s??',
        'GROUND': ['DBQ\'s', 'Mug', 'Printer', 'Quiz Cover Sheet', 'Spinny Chair']},
    'Wing B from Study': {
        'DOORS': {'FORWARD': 'Grand Ballroom', 'BACK': 'Study', 'LEFT': 'Main Hall', 'RIGHT': 'Art Gallery'}},
    'Wing D from Study': {
        'DOORS': {'FORWARD': 'Library', 'BACK': 'Study', 'LEFT': 'Kitchen', 'RIGHT': 'Long Corridor'}},
    'Library': {
        'DOORS': {'LEFT': 'Wing C', 'RIGHT': 'Wing D'},
        'DESC': 'Your inner book-lover can\'t help but be in awe of the massive bookselves that line the room from floor to ceiling.  You can\'t help but wish you had the time to read them all.  You also notice an eerily familiar statue in the center of the library... \nYou definitely know it from somewhere-- why can\'t you place it?',
        'GROUND': ['Statue', 'Bookshelf', 'Cookbook By Mr. Nowakoski', 'Varoun And The Sea Of Stories', 'The Communist Manifesto', 'Women Snd Economics', 'The Crucible', 'The Answer To The Great Pants Debate', 'To Build A Fire', 'How To Survive Magnet Guide']},
    'Wing C from Library': {
        'DOORS': {'FORWARD': 'Trophy Room', 'BACK': 'Library', 'LEFT': 'Locked Closet', 'RIGHT': 'Main Hall'}},
    'Wing D from Library': {
        'DOORS': {'FORWARD': 'Study', 'BACK': 'Library', 'LEFT': 'Long Corridor', 'RIGHT': 'Kitchen'}},
    'Kitchen': {
        'DOORS': {'FORWARD': 'Wing D'},
        'DESC': 'The delightful smell of food fills the air, making you hungry. The chef flashes a grin, as he slides a box marked "Not Human Organs" under a table with his foot.  Averting, your eyes you notice that there\'s a fridge, toaster, microwave, and cupboard in different corners of the room.  There\'s also a bag of popcorn on the counter -- your favorite!',
        'GROUND': ['Pink Goldfish', 'Fridge', 'Toaster', 'Toast', 'Box', 'Bag Of Popcorn', 'Key']},
    'Wing D from Kitchen': {
        'DOORS': {'FORWARD': 'Long Corridor', 'BACK': 'Kitchen', 'LEFT': 'Library', 'RIGHT': 'Study'}},
    'Main Hall from Wing A': {
        'DOORS': {'LEFT': 'Wing B', 'RIGHT': 'Wing C'},
        'DESC': 'You are now standing in the main hall leading to the other wings of the mansion.'},
    'Main Hall from Wing B': {
        'DOORS': {'LEFT': 'Wing D', 'RIGHT': 'Wing A'},
        'DESC': 'You are now standing in the main hall leading to the other wings of the mansion.'},
    'Main Hall from Wing C': {
        'DOORS': {'LEFT': 'Wing A', 'RIGHT': 'Wing D'},
        'DESC': 'You are now standing in the main hall leading to the other wings of the mansion.'},
    'Main Hall from Wing D': {
        'DOORS': {'FORWARD': 'Long Corridor', 'LEFT': 'Wing C', 'RIGHT': 'Wing B'},
        'DESC': 'You are now standing in the main hall leading to the other wings of the mansion.'},
    'Wing A from Main Hall': {
        'DOORS': {'FORWARD': 'Start', 'LEFT': 'Trophy Room', 'RIGHT': 'Grand Ballroom'}},
    'Wing B from Main Hall': {
        'DOORS': {'FORWARD': 'Art Gallery', 'LEFT': 'Grand Ballroom', 'RIGHT': 'Study'}},
    'Wing C from Main Hall': {
        'DOORS': {'FORWARD': 'Locked Closet', 'LEFT': 'Library', 'RIGHT': 'Trophy Room'}},
    'Wing D from Main Hall': {
        'DOORS': {'FORWARD': 'Kitchen', 'LEFT': 'Study', 'RIGHT': 'Library'}},
    'Locked Closet': {
        'DOORS': {'FORWARD': 'Locked Room', 'BACK': 'Wing C'},
        'DESC': 'This room is locked and you need a key to enter.'},
    'Locked Room': {
        'DOORS': {'FORWARD': 'Wing C'},
        'DESC': 'you see doors foo',
        'GROUND': ['Code #2', 'Door B', 'Door C', 'Door D']},
    'Wing C from Locked Closet': {
        'DOORS': {'FORWARD': 'Main Hall', 'LEFT': 'Trophy Room', 'RIGHT': 'Library', 'BACK': 'Locked Closet'}},
    'Long Corridor': {
        'DOORS': {'FORWARD': 'Final Room', 'BACK': 'Wing D'},
        'DESC': 'These doors are locked and you need both escape codes in order to proceed!'},
    'Wing D from Long Corridor': {
        'DOORS': {'FORWARD': 'Kitchen', 'LEFT': 'Study', 'RIGHT': 'Library'},
        'DESC': ''},
    'Locked Doors': {
        'DOORS': {'FORWARD': 'Final Room', 'BACK': 'Wing D'},
        'DESC': ' yeet yahhh '},
    'Final Room': {
        'DOORS': {'BACK': 'Wing B'},
        'DESC': ' need this?? '},
    }

#dictionary containing information for just the wings -- often referred to in order to convert player perspective to proper directions
worldWings = {
    'Wing A': {
        'DESC': 'You are standing in the middle of the wing, looking at the rooms you can next travel to.',
        'NORTH': 'Main Hall from Wing A',
        'EAST': 'Trophy Room',
        'SOUTH': 'Start',
        'WEST': 'Grand Ballroom'},
    'Wing B': {
        'DESC': 'You are standing in the middle of the wing, looking at the rooms you can next travel to.',
        'NORTH': 'Study',
        'EAST': 'Main Hall from Wing B',
        'SOUTH': 'Grand Ballroom',
        'WEST': 'Art Gallery'},
    'Wing C': {
        'DESC': 'You are standing in the middle of the wing, looking at the rooms you can next travel to.',
        'NORTH': 'Library',
        'EAST': 'Locked Closet',
        'SOUTH': 'Trophy Room',
        'WEST': 'Main Hall from Wing C'},
    'Wing D': {
        'DESC': 'You are standing in the middle of the wing, looking at the rooms you can next travel to.',
        'NORTH': 'Kitchen',
        'EAST': 'Library',
        'SOUTH': 'Main Hall from Wing D',
        'WEST': 'Study'}
    }

#class used for all rooms (except for the wings)
class Room(object):

    def __init__(self, name, desc, front=True, back=True, left=True, right=True, locked=False):
        self.name = name
        self.exception = 'Main Hall'
        self.walls = {'front': front, 'back': back, 'left': left, 'right': right}
        self.desc = desc
        self.locked = locked

    #general function to print room location, description, and other rooms relative to it
    def nextTurn(self):

        #prints the name of the room
        if self.name not in ['Main Hall from Wing A', 'Main Hall from Wing B', 'Main Hall from Wing C', 'Main Hall from Wing D']:
            print(self.name)
            print("=" * len(self.name))
        else: #this prints just the location name rather than the reference name of 'location from Wing __'
            print(self.exception)
            print("=" * len(self.exception))


        #prints the description of the room
        print(self.desc)

        """
        #prints the available doors
        for k, v in self.walls.items():
            if v:
                print(f"You see a door to the {k}.")
        """

        #just for formatting reasons :)
        print(' ')

        #prints which room is in which direction
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

#class used for just the wings -- has special accomodation to convert perspective to proper directions
class Wing(object):

    def __init__(self, name, desc, north=True, south=True, east=True, west=True):
        self.name = name
        self.walls = {'north': north, 'south': south, 'east': east, 'west': west}
        self.desc = desc

    #general function to print room location, description, and other rooms relative to it -- but modified to be compatible with the wings
    def altnextTurn(self):

        #prints name of the room
        print(self.name)
        print("=" * len(self.name))

        #prints the room description
        print(self.desc)
        print(' ')

        #prints available rooms / display which toom is in which direction
        for k,v in self.walls.items():
            if v == True:
                if prevlocation not in ['Main Hall from Wing A', 'Main Hall from Wing B', 'Main Hall from Wing C', 'Main Hall from Wing D']:
                    name_2 = (f'{self.name} from {prevlocation}')  #in order to match the dictionary worldRooms the loaction name must be altered
                else:
                    name_2 = (f'{self.name} from Main Hall')
                list1 = (worldRooms[name_2]['DOORS']).keys() #based on which cardinal direction is set to true, the list of possibile rooms is checked
                for n in list1:
                    print((str(f"{n}: {worldRooms[name_2]['DOORS'][n]}")).title())
            break

#class used for all objects
class Object(object):
    def __init__(self, official, desc, names, takemg='', dropmg = '', eatmg='', takeable=True, edible=False, usable=False, validity=False, lookdeadly=False, takedeadly=False):
        self.official = official
        self.desc = desc
        self.names = names
        self.takemg = takemg
        self.dropmg = dropmg
        self.eatmg = eatmg
        self.takeable = takeable
        self.edible = edible
        self.usable = usable
        self.lookdeadly = lookdeadly
        self.takedeadly = takedeadly

#list containing information (filled in paramaters) that correspond with the Object class
worldItems = [
    #items in start
    Object('Welcome Sign', 'The sign reads, "Welcome to the game, Missing from Magnet! The objective is to find the two needed codes to escape. You can type "help" for a list\nof commands or type "map" to reference the map. Best of luck!', ['welcome sign', 'welcome'], takeable=False),
    #items in grand ballroom
    Object('Trapdoor', 'You cautiously approach the trapdoor, debating whether you should open it or not. Mustering up some courage you lift the door of the trap door and are rewarded with a hand grabbing your ankle and dragging you down with it! \nLol you dead.', ['trapdoor'], takeable=False, lookdeadly=True),
    Object('Shattered Glass', 'Why is there just a pile of broken glass on the floor?', ['shattered glass', 'glass'], edible=True, takemg='Ouch.', eatmg='\nSeriously? What is wrong with you? Did you seriously just eat shards of glass?!? \n\n...What? \nOh.. You have the Sanservino midterm next. -- Proceed as you were.'),
    Object('Dancefloor', 'Looking at the dancefloor, you are suddenly reminded of your inability to dance...\nYou die immediately of extreme cringe.', ['dancefloor', 'dance', 'floor'], takeable=False, lookdeadly=True),
    Object('Chandelier', 'Wow, the crystals on the chandelier are stunning!', ['chandelier'], takeable=False),
    Object('High Heels', 'You take a closer look and realize that SCORE! These EXPENSIVE, these is RED BOTTOMS, these is BLOODY SHOES!', ['high heels', 'heels', 'red bottoms', 'louboutins'], takemg='Same girl, same.'),
    #items in trophy room
    Object('Rubber Band', 'Upon closer inspection you realize that the rubber band is THE very rubber band that Limo used to shoot down a wasp in the AIT bridge in a \nSINGLE. SHOT.\n...we are just mere mortals', ['rubber band']),
    Object('Virendragon', 'You pick up the virendragon plush and are startled to find that this is no ordinary plush --\nIn fact, when you squeeze the plush, it lets out a vicious roar:\n\nREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE!!!!!', ['virendragon', 'virendragon plush', 'plush'], dropmg='Why would you get rid of such a magnificent plush?'),
    Object('Arthur\'s Speakeasy Performance', 'Sorry, legends only.', ['arthur\'s speakeasy performance', 'speakeasy', 'speakeasy performance', 'performance'], takeable=False, takemg='Sorry, legends only.'),
    Object('Purdue Acceptance Letter', 'YEAHHHHHHH PURDUEEEEEEE', ['purdue acceptance letter', 'purdue', 'purdue acceptance', 'acceptance letter', 'letter', 'purdue letter']),
    #items in art gallery
    Object('Do Not Take This Sign Sign','The sign reads, "Do not take this sign."', ['do not take this sign sign', 'sign']),
    Object('Moose Costume', 'You lift up the moose costume and hold it up against yourself-- It appears to be exactly your size! \n& bonus: it looks super fuzzy warm :)', ['moose costume', 'moose', 'costume'], takedeadly=True, takemg='From the distance you hear an ominous music draw closer and closer -- louder and louder\nYou can finally start making some of the words out... \n\n     DRESS UP LIKE A MOOSE DURING HUNTING SEASOOOOOOOON \n\n\nDumb ways to dieeeeeeeee\nso many dumb ways to dieeeeeeeee\nDumb ways to die-ie-ieeeeeeeee\nso many dumb ways to dieeeee'),
    Object('Mona Lisa', 'Could it be?? There\'s always been rumors that the real Mona Lisa had been secretly stolen but the painting right before you is enough to put all those rumors to rest...', ['mona lisa', 'painting'], takemg='\nWoah, when you move the painting you notice a folded piece of paper hidden in a crack in the wall!'),
    Object('Harambe Tribute', 'You spend a moment to take it all in and silently brush a tear from the corner of your eye...\nHe will forever live on in our hearts.', ['harambe tribute', 'harambe', 'tribute'], takeable=False),
    Object('Curtain', 'When you move the curtain aside you are quite surprised to find a life size oil painting of Blaise\'s "octodab"!\n#iconic', ['curtain'], takeable=False),
    Object('Code #1', 'The piece of paper reads: \n * Code #1 -- 42 72 69 65 6c 6c 61', ['code #1', 'folded piece of paper', 'piece of paper', 'paper'], edible=True, eatmg='WHY WOULD YOU DO THAT YOU IDIOT??! I hope you have a good memory...'),
    #items in study
    Object('DBQ\'s', 'Wait... what\'s that on the desk?? Is that the DBQ\'s from freshmen year that Mr. McMenamin STILL hasn\'t graded??', ['dbq\'s', 'dbq', 'dbqs'], takeable=False, takemg='You can\'t take these yet! They still haven\'t been graded!'),
    Object('Mug', 'You pick up the mug and turn it around to see what it says.  It reads:\n\n          WORLD\'S BEST BOSS', ['mug'], takeable=False, takemg='You\'re not Michael Scott!!'),
    Object('Printer', 'It looks like someone must have left something on the printer. You look at the top page and it says:\n\n          "QUIZ COVER SHEET"\n\n...Well it was left here after all.. Would just a peek hurt?', ['printer'], takeable=False),
    Object('Quiz Cover Sheet', 'After a quick glance over each shoulder and and quick breath, you lift up the cover sheet to see what\'s underneath.  \nScrawled in Sharpie on the page underneath is,\n\n          yOu PlAyEd YoUrSeLf SoN!!!', ['quiz cover sheet', 'quiz', 'cover sheet', 'cover', 'sheet'], takeable=False),
    Object('Spinny Chair', 'Come on, who can resisted spinning in a spinny chair?', ['spinny chair', 'chair'], takeable=False),
    #items in kitchen
    Object('Pink Goldfish', 'You have just discovered Mr. Moskowitz\'s secret stash of pink goldfish!!', ['pink goldfish', 'cupboard', 'goldfish'], edible=True, eatmg='Oooooo I\'m telling Mr. Moskowitz that you ate his goldfish!'),
    Object('Fridge', 'Don\'t you know that there\'s never anything that you want when you check the fridge?! Game or not, you\'re about to dramatically starve to death', ['fridge'], takeable=False, lookdeadly=True),
    Object('Toaster', 'You look inside the toaster and find toast!', ['toaster'], takeable=False),
    Object('Toast', 'Although you go to Magnet, you apparently still thought it was a good idea to take the toast out with a fork!', ['toast'], lookdeadly=True, takedeadly=True, takemg='Although you go to Magnet, you apparently still thought it was a good idea to take the toast out with a fork!'),
    Object('Box', 'Duhhhh, he pushed it under the table for a reason dummy! You can\'t look!', ['box'], takeable=False),
    Object('Bag Of Popcorn', 'Just an unpopped bag of popcorn.', ['bag of popcorn', 'popcorn', 'popcorn bag', 'bag']),
    Object('Key', 'You open the microwave and find a key sitting inside!  It\'s a good thing you didn\'t turn it on to try to pop the popcorn!', ['key', 'microwave']),
    #items in library
    Object('Statue', 'You get closer to the statue and suddenly realize why it looks so familiar!! It\'s King Neptune from the Spongebob Squarepants movie! The statue has a paper bag over its head and you decide to lift it up. The second you do a bliding light emits from the baldness of his crownless head and you fall to the floor while hearing echoing screams of "BALD, BALD, BALD, MYYYY EYESSSSSSSSS"', ['statue', 'familiar statue', 'statue of king neptune', 'king neptune'], takeable=False, lookdeadly=True),
    Object('Bookshelf', 'Wow, there sure are a lot of books! You see Cookbook By Mr. Nowakowski, Varoun And The Sea Of Stories, Women And Economics, The Crucible, The Answer To The Great Pants Debate, To Build A Fire, and the How To Survive Magnet Guide.', ['bookshelf', 'bookshelves'], takeable=False),
    Object('Cookbook By Mr. Nowakoski', 'A limited edition, first edition copy of former executive chef, Mr. Peter Nowakoski\'s cookbook that has a recipe for every occasion!', ['cookbook by mr. nowakoski', 'cookbook by mr nowakoski', 'cookbook'], takemg='Good choice!'),
    Object('Varoun And The Sea Of Stories', 'Flashbacks to freshmen year...', ['varoun and the sea of stories', 'varoun', 'sea of stories']),
    Object('Women And Economics', 'Umm, yes please!', ['women and economics']),
    Object('The Crucible', 'You open the massive literature textbook to the Crucible, but when you start to crack open the book you swear you hear a voice! Startled, you slam the book closed and tentatively begin to crack the book back open.  You hear a rasping voice wheeze out, "more weighhhhhht!"', ['the crucible', 'crucible']),
    Object('The Answer To The Great Pants Debate', 'I\'m sorry but this knowledge is too powerful...', ['the answer to the great pants debate', 'answer', 'debate', 'great pants debate', 'the great pants debate']),
    Object('To Build A Fire', 'Moral of the story:  Gotta get back to the boys!', ['to build a fire']),
    Object('How To Survive Magnet Guide', 'HA! Yeahhhhh this doesn\'t exist.', ['how to survive magnet guide', 'survival guide', 'guide'], edible=True, eatmg='That might be its most useful use yet!'),
    #locked room
    Object('Code #2', 'You stuck with your gut and chose right! Your reward is the second needed code sequence.\n\nDon\'t forget to type "take code" to add it to your inventory.', ['door a', 'a', 'code #2', 'code']),
    Object('Door B', 'Story Time!:  “Once there was an Ugly Barnacle. He was so ugly, that everyone died! The End.”\n\n...You\'re that Ugly Barnacle.', ['door b', 'b'], takeable=False, lookdeadly=True),
    Object('Door C', 'Some believe that by choosing "C" you have a higher chance of guessing correctly! ...Well today\'s not that day.', ['door c', 'c'], takeable=False, lookdeadly=True),
    Object('Door D', 'You open the door to only to find yourself staring at your reflection in the mirror! You die partly from shock and partly from sheer ugliness.', ['door d', 'd'], takeable=False, lookdeadly=True),
    ]


#master command loop that allows a variety of user inputted commands
class TextAdventureCmd(cmd.Cmd):
    prompt = '\n> '

    def default(self, arg):
        print('I do not understand that command. Type "help" for a list of commands.')

    def do_quit(self, arg):
        """Quit the game."""
        global quit
        quit = 'True'
        return True #by returning True (and this applies to all functions containing 'return True' that are withing this command loop) it exits the command loop and then runs code from the middle of the while loop that follows

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
        global endgame

        choice = item.lower()
        current = ''

        #checks if user inputted item is within the list of items
        for item in worldItems:
            if choice in item.names:
                current = item
            if choice not in item.names:
                validity = 'no'

        #sets validity as positive if the object is in the list of items
        for item in worldItems:
            if choice in item.names:
                validity = 'yes'
                current.validity = True

        #checks each item in the list to see whether the item is plausible based on its criteria
        for item in worldItems:
            if choice in item.names:
                if current.official in worldRooms[location]['GROUND']:  #checks if item is in current room
                    print(current.desc)                                 #prints item description
                    if current.lookdeadly == True:                      #if looking at the item is deadly, user is deffered from game
                        endgame = 'True'
                        return True
                if current.official not in worldRooms[location]['GROUND']:  #if the item is plausible but not in the current room, it prints message
                    print('You do not see that item.')

        #this will print a message if the user enters an item that doesn't exist or an improper input
        if validity != 'yes':
            print('You do not see that item.')


    def do_take(self, item):
        """take <item> - Take an item within the room."""
        global endgame

        #changes user input
        choice = item.lower()
        current = ''

       #checks to see if item is in list of items, and if not, the item's validity is set to "no"
        for item in worldItems:
            if choice in item.names:
                current = item
            if choice not in item.names:
                validity = 'no'

        #changes valid items to be positive
        for item in worldItems:
            if choice in item.names:
                validity = 'yes'
                current.validity = True

        #checks each item in list of items and goes through checklist of criteria
        for item in worldItems:
            if choice in item.names:
                if current.official in worldRooms[location]['GROUND']:          #checks if item is in current room in order to proceed
                    if current.takeable == True:                                #checks if item is takeable
                        if current.takedeadly == True:                          #if taking the item is deadly, the game is ended
                            print(current.takemg)
                            endgame = 'True'
                            return True
                        inventory.append(current.official)                      #if not, the item is added to the player's inventory
                        print(f'"{current.official}" has been added to your inventory.')
                        if current.takemg != '':                                #if the item has a special 'take description' it will be displayed
                            print(current.takemg)
                    else:                                                       #if item is not takeable, message is displayed
                        if current.takemg != '':
                            print(current.takemg)
                        else:
                            print('You can not take that item.')
                if current.official not in worldRooms[location]['GROUND']:      #if item is not in current room, message is displayed
                    print('That item is not here to take.')

        if validity != 'yes':                                                   #if the item does not exist or is entered wrong, message is displayed
            print('That item is not here to take.')


    def do_drop(self, item):
        """drop <item> - Drop an item and remove it from your inventory."""

        #changes user input
        choice = item.title()
        current = ''

        #checks if item is in list of items
        for item in worldItems:
            if choice.lower() in item.names:
                current = item

        if choice in inventory:                                                 #checks if item is in inventory
            inventory.remove(choice)                                            #if yes, the item is removed
            print(inventory)                                                    #the current inventory is displayed
            if current.dropmg != '':                                            #checks if there is a special 'drop message'
                print(current.dropmg)
        else:
            print('You do not have that item in your inventory to remove.')     #if item is not inventory, displays message


    def do_eat(self, item):
        """eat <item> - Eat an item that is in your inventory."""

        #changes user input format
        choice = item.lower()
        current = ''

        #checks to see if reference name is in list of items
        for item in worldItems:
            if choice in item.names:
                current = item

        if choice.title() in inventory:                                         #checks to see if item is in inventory
            if current.edible == True:                                          #checks to see if the item is edible
                inventory.remove(choice.title())                                #if yes, the item is removed from the player's inventory
                print(f'You just ate "{choice}."')                              #prints message
                if current.eatmg != '':                                         #checks to see if there is special 'eat message'
                    print(current.eatmg)                                        #and if so, prints the message
            else:
                print('You can not eat that item.')                             #if item is not edible, displays message
        else:
            print('That item is not in your inventory to eat.')                 #pretty self explanatory lol


    def do_use(self, item):
        """use <item> - Use an item that is in your inventory."""

        #changes user input
        choice = item.lower()
        current = ''

        #checks to relate reference name back to official name within list of items
        for item in worldItems:
            if choice in item.names:
                current = item

        if choice.title() in inventory:                                         #checks to see if item is in inventory
            if current.usable == True:                                          #if usable is true, message is displayed
                print(f'You just used your {choice}.')
            else:
                print('You can not use that item.')                             #if usable is false, message is displayed
        else:
            print('That item is not in your inventory to use.')                 #if item is not in inventory, message is displayed


    def do_inventory(self, arg):
        """This will show your current inventory."""
        print(inventory)

    def do_map(self, arg):
        """View the map of the mansion."""
        map()



#Begginning Fancy Stuff
print("""
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

   M I S S I N G   F R O M   M A G N E T

▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

        ~ (Type "help" for commands.) ~

""")


#Beginning Conditions
location = 'Start'
inventory = []
endgame = ''


#slowed printing for game ending
import sys,time,random
typing_speed = 100 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)


#MASTER WHILE LOOP THAT ALLOWS FOR THE GAME TO BE ENDED
    #contains 4 main conditions: if the next location is any regular room, if it is a wing, if it is the locked room, or if it is the final room
while True:
    if location != 'Wing A' or 'Wing B' or 'Wing C' or 'Wing D':
        location = location
        parameters = {
            'start': Room(location, worldRooms[location]['DESC'], back=False, left=False, right=False),
            'grandballroom': Room(location, worldRooms[location]['DESC'], front=False, back=False),
            'trophyroom': Room(location, worldRooms[location]['DESC'], front=False, back=False),
            'artgallery': Room(location, worldRooms[location]['DESC'], back=False, left=False, right=False),
            'locked room': Room(location, worldRooms[location]['DESC'], back=False, left=False, right=False),
            'study': Room(location, worldRooms[location]['DESC'], front=False, back=False),
            'library': Room(location, worldRooms[location]['DESC'], front=False, back=False),
            'secretattic': Room(location, worldRooms[location]['DESC'], front=False, back=False, left=False, right=False),
            'kitchen': Room(location, worldRooms[location]['DESC'], back=False, left=False, right=False),
            'longcorridor': Room('Locked Doors', worldRooms[location]['DESC'], left=False, right=False),
            'lockedcloset': Room(location, worldRooms[location]['DESC'], left=False, right=False),
            'mainhallfromwinga': Room(location, worldRooms[location]['DESC'], front=False, back=False),
            'mainhallfromwingb': Room(location, worldRooms[location]['DESC'], front=False, back=False),
            'mainhallfromwingc': Room(location, worldRooms[location]['DESC'], front=False, back=False),
            'mainhallfromwingd': Room(location, worldRooms[location]['DESC'],front=False, back=False)}
        #this section of code is to convert the official room name to match the keys in the parameter dictionary
        location_modified = location.lower()                                    #makes it lower case
        if ' ' in (location_modified):                                          #checks for a space in the words
            location_modified = location_modified.replace(" ", "")              #and if so, removes it
        self = parameters[location_modified]
        self.nextTurn()                                                         #prints the total description of the next room by calling the Room class

        #enters the player back into the command loop
        TextAdventureCmd().cmdloop()

        #if the player inputted quit, the game is ended
        if quit == 'True':
            print('\n\nThanks for playing!')
            break

        #if either an item was deadly to look at or take, endgame will equal 'True' here and the game will be ended
        if endgame == 'True':
            print('\nThanks for playing -- try again')
            break

        #when the user inputs either forward, back, left, or right the command loop is exited and is checked here where the current, new, and previous location variables are set
            #then when it runs through the loop again, based on the location, the proper code will be run
        if user_input == 'FORWARD' or 'BACK' or 'LEFT' or 'RIGHT':
            print(' \n \n')
            newlocation = worldRooms[location]['DOORS'][user_input]
            prevlocation = location
            location = newlocation

        #default message if user input is not valid
        else:
            print('Sorry, I don\'t recognize that command.  Enter "help" for the list of commands.')


    #special case of code for the final room which requires two codes to unlock
    if location == 'Final Room':
        #prints name of room
        print(location)
        print("=" * len(location))

        finalRoom = Room(location, worldRooms[location]['DESC'], front=False, back=False, left=False, right=False, locked=True)
        fr = finalRoom
        end = ''
        if fr.locked == True:
            #checks if the player has found and taken both codes
            if 'Code #1' and 'Code #2' in inventory:
                #asks player to enter look codes which displays the codes for convenience
                print('Congratulations!  You have found both of the code sequences! Enter "look codes" to see the sequences again.')
                while True:
                    if end == True:
                        quit = 'True'
                        continue
                    displayCodes = (input(f'{inventory} \n\n> ')).lower()
                    if displayCodes == 'look codes':
                        print("""     * Code #1 -- 42 72 69 65 6c 6c 61\n     * Code #2 -- 41 70 72 69 6c""")
                        while True:
                            code1 = input('\nEnter code sequence #1:  ')
                            if code1 == '42 72 69 65 6c 6c 61':
                                slow_type('       processing...\n       processing...\n')
                                code2 = input('Enter code sequence #2:  ')
                                if code2 == '41 70 72 69 6c':
                                    slow_type('       processing...\n       processing...\n')
                                    print("""


                                               .*********        .****.         .*  ...
                                              .***  ..****.      ******        .*****.
          **************.                     .***      .***    .** ***        *****
       *********..  ..*****.                   ****      ****    *****.      .****.                    *...
     *******.            .****                   ******...***. .*****.     .****.           .***     .****
        **.                .***.                   .***************..********..             .***    *****
        .                    .***.                       ****                               .**. .*****
               .*****.         ****                     .***.                     .****************.
            .**********.        .***.                  .****                    .*******....***.      ..
          .****.   *****          .****.            ..****.    *****             ***        ***.    **.**.
        .***.      *****            ..*******........**..     ******                 ***.   ***.    ******       .***.
       .**.        *****                 ..****......         ******   .***.    .*******.   ***.     .****       .***
      .**.        *****.                                       .***********.   *********.  .****.     .*****    .***.
     ***.        *****.                                .......   ***...***.  .***   .***   *****.    .**..***  .***.
    .**.        *****.                    ....       ********.  .***  ***.   .**.   .***  ***..***..***. **** .***
   .**.            **               .. .******     .****  ****  .**.  ***   .***    ****.***.  *****************.
  .***.                 .*****.   .***.*******     ***.   .***  ***. .***   ****.  .********     ...   ...*..
  .**.                .********* .******.  ***    ****    ****..**.  .***  .*********..**.
  ***                 ***    .*********.  .**.   .****   ********.    ********  ...                      .*******.
 .**.                 .***....****.***.   .***  .***************.       ....         ..               .***.      .**
 .**.                  .*********. ***     ********.******..***.                 ..******.           .**.         ***
 ***.              ****       ***..***     .*****.       .*****.                .***...****.        ***           .**.
 ***.              ***.      .*** ***.                .********.                ***.    .***       .**.           .**.
 ***.              ****.    ****  *..                *****. ***.                ***.     ***      .**.          ..***.
 .**.               ***********                    *****.   ****                .***.    ***     .**.      ...*.*****
  ***                .******.                     ****.     ****                 .*****..*** ..****.     ***********
  ***.                                           .****      ***.                    ************..        *******.
  .***.               ..                          .***.    .***.                      .*****...          .**..
   .****.           .**.        .**********..      .**********.                      ****
     ******.    ..*********   .******************       ....                      *****
       .****************.    ******         ..*******.                       .******
         .***********..     ******              .**********...         ..********
                           *****.                   ..*********************.
                           *****.
                          .*****
                          ..  .*        Y O U ' V E  M A D E  I T  O U T  A L I V E  &  W O N  T H E  G A M E ! ! !

                                                                Thanks for playing!
                                    """)
                                    end = True
                                    break
                                #a check for if player does not enter the code right
                                else:
                                    print('Hmm... you must have entered the code wrong.  Try entering it again.\n')
                                    continue
                            #a check for if player does not enter the code right
                            else:
                                print('Hmm... you must have entered the code wrong.  Try entering it again.\n')
                                continue

                    #a check for if player does not enter "look codes" properly
                    else:
                        print('\nSorry, I don\'t recognize that command.  Try entering "look codes" again.')
                        continue

            #returns the player to the previous room if they do not have both codes needed to escape
            else:
                print('This room is locked and you are unable to enter without the needed escape codes. Keep looking for the codes!\n')
                prevlocation = 'Long Corridor'
                location = 'Wing D'


    #special case of code for the locked closet which requires a key to unlock
    if location == 'Locked Room':
        #prints the room name
        print(location)
        print("=" * len(location))

        lockedCloset = Room(location, worldRooms[location]['DESC'], front=False, back=False, left=False, right=False, locked=True)
        lc = lockedCloset
        if lc.locked == True:
            #prompts user to enter "use key" whether they have it or not
            useKey = (input('You need to use a key to unlock this door. Type "use key" to use your key and enter the room. \n\n> ')).lower()
            while True:
                if useKey == 'use key':
                    #if player has the key, the player is allowed to proceed into the room
                    if 'Key' in inventory:
                        #prints the room description
                        print(f'\n\n{location}')
                        print("=" * len(location))
                        print('You have unlocked the door and entered the room!\n')
                        print('As you glance around, you notice that the room is bare except for four doors each labeled a letter: "A", "B", "C", & "D." \nBehind one of the doors is the essential code vital to escape. I guess this is just good practice for having to guess on multiple choice tests!')
                        print(f'\nForward: '+ worldRooms[location]['DOORS']['FORWARD'])
                        #redefines location variables
                        location = 'Locked Room'
                        prevlocation = 'Locked Closet'
                        #enters back into command loop
                        TextAdventureCmd().cmdloop()
                        print('\n\n')
                        location = 'Wing C'
                        break
                    #player is returned to the hallway if they do not have the key
                    else:
                        print('This room is locked and you are unable to enter without the key. Keep looking for the key!\n')
                        prevlocation = 'Locked Closet'
                        location = 'Wing C'
                        break

                #a check for if the player does not enter "use key" correctly
                else:
                    useKey = (input('\nSorry, I don\'t recognize that command.  Try entering "use key" again. \n\n> ')).lower()
                    continue

    #if the player chooses the wrong door within the locked room, the command loop is exited, endgame matches as 'True' and the game is ended
    if endgame == 'True':
        print('\nThanks for playing -- try again')
        break

    #special set of code if the next location the player is trying to travel to is one of the wings
    if location == 'Wing A' or 'Wing B' or 'Wing C' or 'Wing D':
        location = location
        parameters = {
            'winga': Wing(location, worldWings[location]['DESC']),
            'wingb': Wing(location, worldWings[location]['DESC']),
            'wingc': Wing(location, worldWings[location]['DESC']),
            'wingd': Wing(location, worldWings[location]['DESC'])}
        #modifies location name to remove space so it matches the keys in the parameters dictionary
        location_modified = location.lower()
        if ' ' in (location_modified):
            location_modified = location_modified.replace(" ", "")
        self = parameters[location_modified]
        #prints the total description of the wing referencing the Wing class
        self.altnextTurn()
        print(' ')
        #since there are no items in the wings, the user is prompted to choose a direction
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
        #redefines the variable to match the format of the WorldRooms dictionary by making it the "new location from the previous location"
        if prevlocation not in ['Main Hall from Wing A', 'Main Hall from Wing B', 'Main Hall from Wing C', 'Main Hall from Wing D']:
            name_5 = str(f'{location} from {prevlocation}')
        else:
            name_5 = (f'{location} from Main Hall')
        newlocation = worldRooms[name_5]['DOORS'][user_input]
        prevlocation = location
        location = newlocation
        if location == 'Main Hall':
            location = str(f'{location} from {prevlocation}')

    #a check for if the player enters an invalid input
    else:
        print('Sorry, you are unable to go in that direction.')

