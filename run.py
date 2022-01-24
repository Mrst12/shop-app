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
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            sys.exit()
        else:
            print("I'm sorry that is not a valid input please enter 1-6")

def view_list():
    for item in list_for_shopping:
        print(item)


def add_item():
    item_required = input("Please enter the item you wish to add:\n").lower().strip()
    list_for_shopping.append(item_required)
    print(list_for_shopping)


def main():
    """
    Run all programme functions
    """
    welcome()
    menu()
    menu_selection()


print("### WELCOME TO SHOP APP ###")
main()