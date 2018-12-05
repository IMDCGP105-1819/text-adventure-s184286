

print(r"""
._____________              __                    __
|__\__    ___/___ ___  ____/  |_     ____   _____/  |_
|  | |    |_/ __ \\  \/  /\   __\   /    \_/ __ \   __\
|  | |    |\  ___/ >    <  |  |    |   |  \  ___/|  |
|__| |____| \___  >__/\_ \ |__| /\ |___|  /\___  >__|
                \/      \/      \/      \/     \/
""")

greeting = "Welcome to iText Adventures Games.."

print(greeting)

def hello(name):
    print("Hello, "+ name)

player_name = input("Player 1, What is your name? ")

hello(player_name)


answer = input("would you like to continue ? Y/N ")
if answer == 'y' or answer == 'Y':
    print("ok..")
    input("..press enter to continue")
if answer == 'n'  or answer == 'N':
    print ("Game Over..Goodbye!")

# object class & defined functions


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
# Game Loop

def play():
    inventory = ['A','B','C']
    print("Escape from Text Adventure!")
    while True:
        action_input = get_player_command()
        if action_input in ['n', 'N']:
            print("Go North!")
        elif action_input in ['s', 'S']:
            print("Go South!")
        elif action_input in ['e', 'E']:
            print("Go East!")
        elif action_input in ['w', 'W']:
            print("Go West!")
        elif action_input in ['i', 'I']:
            print("Inventory:")
            for item in inventory:
                print('* ' + str(item))
        else:
            print("Invalid action!")


def get_player_command():
    return input('Action: ')


play()


# world

# player

# items

# inventory
