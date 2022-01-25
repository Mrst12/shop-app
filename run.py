import sys

list_for_shopping = ["bread", "milk"]


def welcome():
    """
    Get the users name and welcome them to shop app
    """
    name = input("Please enter your name:\n ").capitalize().strip()
    print(f"Welcome to Shop app {name}.")


def menu():
    """
    Prints a menu so the user can make a selection to continue
    """
    print(''' 
    ### MENU ###

    1. View list
    2. Add item to list
    3. Check if item is already in list
    4. Remove item from list
    5. Clear list
    6. Exit
    ''')

    
def menu_selection():
    """
    Asks the user what they want to do, and directs to the appropriate function
    """
    while True:
        choice = input("Please make a selection from the above menu: \n")

        if choice == "1":
            view_list()
        elif choice == "2":
            add_item()
        elif choice == "3":
            check_list()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            clear_your_list()
        elif choice == "6":
            sys.exit()
        else:
            print("I'm sorry that is not a valid input please enter 1-6")


def view_list():
    """Allows users to view their shopping list"""
    for item in list_for_shopping:
        print(item)


def add_item():
    """Allows users to add items to their shopping lists
    after checking if its in the list.
    """
    while True:
        item_required = input("Please enter the item you wish to add:\n").lower().strip()
        if any(char.isdigit() for char in item_required):
            print("Sorry please enter a word not numbers")
            continue
        elif item_required in list_for_shopping:
                print(f"{item_required} is already in your list")
        else:
            print(f"{item_required} has been added to your list")
            list_for_shopping.append(item_required)
            break


def check_list():
    """Allows users to check to see if an item is in their list"""
    check_item = input("which item do you want to check?\n").lower().strip()
    if check_item in list_for_shopping:
        print(f"{check_item} is on your list if you wish to remove chose option 4\n")
    else:
        print(f"{check_item} is not on your list if you wish to add it chose option 2\n")



def remove_item():
    """Allows a user to remove an item from the list"""
    item_to_remove = input("Which item would you like to remove?\n")
    if item_to_remove not in list_for_shopping:
        print(f"Sorry {item_to_remove} is not in your list")
    else:
        list_for_shopping.remove(item_to_remove)
        print(f"{item_to_remove} has been removed from your list")


def clear_your_list():
    """Allows a user to clear the list"""
    list_for_shopping.clear()
    print("your shopping list has been cleared")

    
def main():
    """
    Run all programme functions
    """
    welcome()
    menu()
    menu_selection()


print("### WELCOME TO SHOP APP ###")
main()