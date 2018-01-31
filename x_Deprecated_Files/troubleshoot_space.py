DESC = 'desc'
FORWARD = 'forward'
GROUND = 'ground'

worldRooms = {
    'Start': {
        DESC: 'You wake up in a room with no memory of how you got there. ...',
        FORWARD: 'Wing A',
        GROUND: ['', '']},
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


        #
        for k, v in self.walls.items():
            if v:
                print(f"You see a door to the {k}.")
                print(' ')

        for k, v in self.walls.items():
            if v == True:
                if k == 'front':
                    print(f'Forward: ' + worldRooms[self.name][FORWARD])
                elif k == 'back':
                    print(f'Back: ' + worldRooms[self.name][BACK])
                elif k == 'left':
                    print(f'Left: ' + worldRooms[self.name][LEFT])
                elif k == 'right':
                    print(f'Right: ' + worldRooms[self.name][RIGHT])


#TODO: Add this in for clarity and shortened code


#TODO: Begginning Fancy Stuff
#game title
#type help for names'


#worldRooms['Start'][DESC]
start = Room('Start', worldRooms['Start'][DESC], back=False, left=False, right=False)
start.nextTurn()

