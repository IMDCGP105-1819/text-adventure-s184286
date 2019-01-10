# incomplete --> create list, append items, confirm to add more, confirm to continue, print list, exit program.

item = []
item.append(input("What is your item to add? "))

input("would you like to add another item, y/n ?")



answer = input("would you like to continue ? Y/N ")
if answer == 'y' or answer == 'Y':
    item.append(input("What is your item to add? "))
if answer == 'n'  or answer == 'N':
    print ("ok...")  


input("..enter to print")

print(item)


"""
answer = input("would you like to continue ? Y/N ")
if answer == 'y' or answer == 'Y':
    print("ok..")
if answer == 'n'  or answer == 'N':
    print ("Game Over..Goodbye!")  

    """