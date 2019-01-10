# create class of inventory items, 

class Weapon_obj:
    def __str__(self):
        return self.name


class item_1(Weapon_obj):
    def __init__(self):
        self.name = "item_1"
        self.description = "A fist-sized item_1, suitable for bludgeoning."
        self.damage = 5


class item_2(Weapon_obj):
    def __init__(self):
        self.name = "item_2"
        self.description = "A small item_2 with some rust. " \
                           "Somewhat more dangerous than a item_1."
        self.damage = 10


class item_3(Weapon_obj):
    def __init__(self):
        self.name = "Rusty sword"
        self.description = "This sword is showing its age, " \
                           "but still has some fight in it."
        self.damage = 20


def play():
    inventory = [item_2(),'Gold(5)','Crusty Bread']
    print("..iText adventure")
    input("enter to continue..")
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
            for Weapon_obj in inventory:
                print('* ' + str(Weapon_obj))
        else:
            print("Invalid action!")


def get_player_command():
    return input('Action: ')


play()
