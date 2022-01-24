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

    


def main():
    """
    Run all programm functions
    """
    welcome()
    menu()


print("### WELCOME TO SHOP APP ###")
main()