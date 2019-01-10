#from player import Player
#import world




inventory = ['A','B','C']

def get_command():
    return input('Action: ')    

def play():
    player = Player()
		
	#kpad_input = input('Action: ')  # basic commands / movement


while True:
    room = world.tile_at(player.x, player.y)
    print(room.intro_text())
	kpad_input = get_command()
if kpad_input == 'n' or kpad_input == 'n':
    print("Go North!")
    player.move_north()
elif kpad_input =='s' or kpad_input == 's':
    print("Go South!")
    player.move_south()
elif kpad_input =='e' or kpad_input == 'e':
    print("Go East!")
    player.move_east()
elif kpad_input =='w' or kpad_input == 'w':
    print("Go West!")
    player.move_west() 
elif kpad_input == 'i' or kpad_input == 'I':
    print("Inventory:")
    print(inventory)
    player.print_inventory()
else:
    print("Invalid action!")


play() 





 

