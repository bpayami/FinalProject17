
#ALT. MAP VERSIONS

"""
                            +-------------+
                            |    You      |
T H E   M A P               |    Start    |
      O F                   |    Here...  |
                            |             |
    T H E   M A N S I O N   |             |
                            |             |
              +-------------+------O------+-------------+
              |  You        |     | |     |    You      |
              |  Start      |     | |     |    You      |
              |  Here...    |_____| |_____|    You      |
              |             O_____   _____O             |
              |             |     | |     |             |
              |             |     | |     |             |
+-------------+------O------+_____| |_____+-------O-----+---------------+
|You          |     | |      |  __   __  |      | |     |      You      |
|             |     | |      | |  | |  | |      | |     |               |
|Start        |_____| |______| | +-0-+ | |______| |_____|      You      |
|Here...      O_____   ______  |       |  ____   ____O  You      |
|             |     | |      | | +----+ | |    | |     |               |
|             |     | |      | |_________| |    | |     |               |
|             |     | |      |_____   _____|    | |     |               |
+-------------+------O------+     | |     +-------O-----+---------------+
              |   Start     |     | |     |  You        |
              |   Here...   |_____| |_____|  You        |
              |             O_____   _____O             |
              |             |     | |     |             |
              |             |     | |     |             |
              |             |     | |     |             |
              +-------------+------O------+-------------+
                            |             |
                            |   Start     |                          |   Here...   |
                            |             |
                            |             |
                              |             |
                            +-------------+



                        +-----------+
                        |    You    |
                        |    Start  |
                        |    Here...|
                        |           |
                        |           |
            +-----------+-----O-----+-----------+
            |  You      |    | |    |    You    |
            |  Start    |____| |____|    You    |
            |  Here...  |____   ____|    You    |
            |           |    | |    |           |
            |           |    | |    |           |
+-----------+-----O-----+____| |____+-----O-----+-----------+
|  You      |    | |    |  __                   |  You      |
|  Start    |____| |____| |+--0--+              |  You      |
|  Here...  O____   ____  ||     |              |  You      |
|           |    | |    | |+-----+              |           |
|           |    | |    |                       |           |
+-----------+-----O-----+           +-----O-----+-----------+
            |   You     |           |  You      |
            |   Start   |           |  You      |
            |   Here... |           |  You      |
            |           |           |           |
            |           |           |           |
            +-----------+-----O-----+-----------+
                        |   You     |
                        |   Start   |
                        |   Here... |
                        |           |
                        |           |
                        +-----------+

"""







#OLD MAP

"""
The map looks something like this:
You found a map!  This will definitely be helpful in getting out!

         +---------+----+---------+
         | Kitchen O    O  Study  |
         |         ++  ++         |
+-------++----O----+|  |+----O----++-------+
|       |           |  |           |       |
|Locked |           |  |           | Tea-  |
| Closet|       +----OO----+       |  Room |            N
|       O       |          |       O       |            |
+-------+       |   ????   |       +-------+        W---+---E
|       |       |          |     +——————————+           |
|  Art  |       +----------+     | Secret   |           W
|Gallery|                        |   Attic  |
|       O                        ++   ++————+
+-------++----O----+    +----O----/  /
         |Grand    O    |The     /  /
         | Ballroom|    | Library  /
         +---------+    +---------+
                   |    |
                   |    |
                 +----O----+
                 |  You    |
                 |  Start  |
                 |  Here...|
                 +---------+


         +---------+----+---------+
         | Kitchen O    O  Study  |
         |         ++  ++         |
+-------++----O----+|  |+----O----++-------+
|       |           |  |           |       |
|Locked |           |  |           | Tea-  |
| Closet|       +----OO----+       |  Room |            N
|       O       |          |       O       |            |
+-------+       |   ????   |       +-------+        W---+---E
|       |       |          |     +——————————+           |
|  Art  |       +----------+     | Secret   |           W
|Gallery|                        |   Attic  |
|       O                        ++   ++————+
+-------++----O----+    +----O----/  /
         |Grand    O    |The     /  /
         | Ballroom|    | Library  /
         +---------+    +---------+
                   |    |
                   |    |

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





#EXAMPLE OF CLASS

class worldRooms:
   'Common base class for all rooms in map'

   def __init__(desc, north, south, east, west, ground, ):
      self.name = name
      self.salary = salary

   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

#This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
#This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)







