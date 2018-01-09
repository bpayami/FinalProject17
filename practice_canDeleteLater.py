"""
def new_Turn(loc):

    def displayLocation(loc):
        loc = 'Start'
        print(loc)
        print('=' * len(loc))

    def displayDescription():
        print(' ')
        print(worldRooms[loc][DESC])

    def displayDirections():
        print(f'Forward: ' + worldRooms[loc][FORWARD])
"""

def new_Turn():
    def display_Location():
        aspect = 'location'

    def display_Description():
        Description aspect
        aspect = "this is the so called description"

    def display_Directions():
        direction spam
        spam = "forward, etc."

    spam = 'Start'
    display_Location()
    print("After local assignment:", aspect)
    display_Description()
    print("After nonlocal assignment:", aspect)
    display_Directions()
    print("After global assignment:", aspect)

new_Turn()
print("In global scope:", aspect)

"""
The output of the example code is:

After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
"""

