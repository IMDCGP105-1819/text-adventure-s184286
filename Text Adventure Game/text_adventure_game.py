

class myObject(object):                                     # define my base object
    """my base class for all items

    Attributes:
    name: A strng representing the object or item name
    """

    def __init__(self,name, description):                   # define class constructor 
        """ Return a name for the constructed object"""
        """ Return a description for the constructed object"""
        self.name = name 
        self.description = description

p1 =str(input("To begin, please enter your Name:"))					# create username via input and pass value by ref to player object
player = myObject(p1, 'you are Player_1...')                      # created player object
Map = myObject('Map', 'would you like to view the Game Map ?')     # created map object

Room_0= myObject('Room_0', 'location =  @ The Lobby')           # created room from object 
Room_1= myObject('Room_1', 'location =  @ Room _1')
Room_2= myObject('Room_2', 'location =  @ Room _2')
Room_3= myObject('Room_3', 'location =  @ Room _3')
Room_4= myObject('Room_4', 'location =  @ Room _4')
Room_5= myObject('Room_5', 'location =  @ Room _5')
Room_6= myObject('Room_6', 'location =  @ Room _6')
Room_7= myObject('Room_7', 'location =  @ Room _7')
Room_8= myObject('Room_8', 'location =  @ Room _8')
Room_9= myObject('Room_9', 'location =  @ Room _9')
Room_10= myObject('Room_10', 'location =  @ Room _10')
Room_11= myObject('Room_11', 'location =  @ Room _11')
Room_12= myObject('Room_12', 'location =  @ Room _12')
Room_13= myObject('Room_13', 'location =  @ Room _13')
Room_14= myObject('Room_14', 'location =  @ Room _14')
Room_15= myObject('Room_15', 'location =  @ Room _15')
Room_16= myObject('Room_16', 'location =  @ Room _16')

Command_1 = myObject('Move up','..go north direction')			# create  list of essential commands..
Command_2 = myObject('Move down','..go south direction')
Command_3 = myObject('Move right','..go east direction')
Command_4 = myObject('Move left','..go west direction')    
Command_5 = myObject('pick up item','..add item to inventory')
Command_6 = myObject('drop', '..drop or use item in hand')



print(r"""


._____________              __                    __   
|__\__    ___/___ ___  ____/  |_     ____   _____/  |_ 
|  | |    |_/ __ \\  \/  /\   __\   /    \_/ __ \   __\
|  | |    |\  ___/ >    <  |  |    |   |  \  ___/|  |  
|__| |____| \___  >__/\_ \ |__| /\ |___|  /\___  >__|  
                \/      \/      \/      \/     \/      
 
 
""")

print("welcome to iText.net Game_Lobby, a interactive Text Adventure Game Simulation")       # begin game
input("Press Enter to continue...")


print(player.name,player.description)
input("Press Enter to continue...")


print(Map.description)
input("Press Enter to continue...")



print(r"""


        |--------|
        |   R0   |                  
        |  Lobby |                
|-------|--------|--------|--------|
|   R1  |   R2   |   R3   |   R4   |
|       |  item  |        |        |
|-------|--------|--------|--------|
|   R5  |   R6   |   R7   |   R8   |
|       |  iBot  |        |   Key  |
|-------|--------|--------|--------|
|   R9  |   R10  |   R11  |   R12  |
|       |        |        |        |
|-------|--------|--------|--------|
|   R13 |   R14  |   R15  |   R16  |
|       |  Door  |        |   End  |
|-------|--------|--------|--------| 


Start
R0, R2, R6, 
R8, R14,R16			
End

""")


input("Press Enter to continue...")

print("Would you like to view a list of available commands?")
input("Press Enter to continue...")

print(Command_1.name, Command_1.description)
print(Command_2.name, Command_2.description)
print(Command_3.name, Command_3.description)
print(Command_4.name, Command_4.description)
print(Command_5.name, Command_5.description)
print(Command_6.name, Command_6.description)

input("Press Enter to continue...")



print ("Game Over")                     # terminate code here and exit game.
input("Press Enter to exit...")









