



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
canContinue = False

def play():
    inventory = ['A','B','C']
    print("Escape from Text Adventure!")
    while (canContinue == False):
        action_input = get_player_command()
        if action_input in ['n', 'N']:
            print("Go North!")
			canContinue = True
        elif action_input in ['s', 'S']:
            print("Go South!")
			canContinue = True
        elif action_input in ['e', 'E']:
            print("Go East!")
			canContinue = True
        elif action_input in ['w', 'W']:
            print("Go West!")
			canContinue = True
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




class Player:
    def __init__(self):
        self.inventory = [items.Weapon1(),
                          items.Weapon2(),
                          '',
                          '']

    def print_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print('* ' + str(item))
        best_weapon = self.most_powerful_weapon()
        print("Your best weapon is your {}".format(best_weapon))

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass

        return best_weapon

# items

class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name


class Weapon1(Weapon):
    def __init__(self):
        self.name = "Weapon1"
        self.description = "......."
        self.damage = 5


class Weapon2(Weapon):
    def __init__(self):
        self.name = "Weapon2"
        self.description = "....... " \
                           "......."
        self.damage = 10


class Weapon3(Weapon):
    def __init__(self):
        self.name = "Weapon3"
        self.description = "......... " \
                           "........"
        self.damage = 20

# inventory

inventory = ['A','B','C']
