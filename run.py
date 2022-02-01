import sys

list_for_shopping = []
new_list = []


def welcome():
    """
    Get the users name and welcome them to shop app
    """
    while True:
        name = input("Please enter your name:\n ").capitalize().strip()
        if any(char.isdigit() for char in name):
            print("\n** Sorry please enter letters, not numbers **\n")
        elif not name:
            print("** Please enter a valid name **\n") 
            continue
        else:
            print(f"\n** Welcome to Shop app {name}.**")
            break


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
        menu()
        choice = input("Please make a selection from the above menu:\n")    

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
            exit_app()
        elif not choice:
            print("** I'm sorry that is not a valid input please enter 1-6 **")
        else:
            print("** I'm sorry that is not a valid input please enter 1-6 **")


def view_list():
    """Allows users to view their shopping list"""
    if list_for_shopping == []:
        print("\n** Your shopping list is empty **")
    else:
        print("\n** Your shopping list is: \n")
        with open('list_for_shopping.txt', 'rt'):
            for element in list_for_shopping:
                print(element, end='')


def get_data():
    with open('list_for_shopping.txt', 'rt') as my_list:
        for line in my_list:
            list_for_shopping.append(line)


def add_item():
    """Allows users to add items to their shopping lists
    after checking if its in the list.
    """
    while True:
        item_required = (
            input("Please enter the item you wish to add:\n")
            .lower()
            .strip()
        )
        if any(char.isdigit() for char in item_required):
            print("\n** Sorry please enter a word not numbers **\n")
            continue
        elif item_required + '\n' in list_for_shopping:
            print(f"\n** {item_required} is already in your list **")
            break
        elif not item_required:
            print("\n** Please enter a valid input **\n")
        else:
            print(f"\n** {item_required} has been added to your list **")
            list_for_shopping.append(item_required + '\n')
            save_list()
            break


def check_list():
    """Allows users to check to see if an item is in their list"""
    while True:
        check_item = input("which item do you want to check\n").lower().strip()
        if any(char.isdigit() for char in check_item):
            print("\n** Sorry please enter a word not numbers **\n")
            continue
        elif check_item + '\n' in list_for_shopping:
            print(f"\n** {check_item} is on your list")
            print("If you wish to remove chose option 4 **\n")
            break
        elif not check_item:
            print("\n** Please enter a valid input **\n")
        else:
            print(f"\n** {check_item} is not on your list")
            print("If you wish to add it chose option 2 **\n")
            break


def remove_item():
    """Allows a user to remove an item from the list"""
    while True:
        item_to_remove = (
             input("Which item would you like to remove?\n")
             .lower()
             .strip()
        )
        if any(char.isdigit() for char in item_to_remove):
            print("\n** Sorry please only input letters not numbers **\n")
            continue
        elif not item_to_remove:
            print("\n** Please enter a valid input **\n")
        elif item_to_remove + '\n' not in list_for_shopping:
            print(f"\n** Sorry {item_to_remove} is not in your list **")
            break
        else:
            list_for_shopping.remove(item_to_remove + '\n')
            print(f"\n** {item_to_remove} has been removed from your list **")
            save_list()
            break


def clear_your_list():
    """Allows a user to clear the list"""
    list_for_shopping.clear()
    print("\n** Your shopping list has been cleared **\n")
    save_list()


def save_list():
    list = new_list + list_for_shopping
    with open('list_for_shopping.txt', 'w') as output_file:
        for x in list:
            if x != '\n':
                output_file.write(x)

    new_list.clear()
    list_for_shopping.clear()
    get_data()


def exit_app():
    """
    Allows a message to be printed and then exit the program
    so gives the user feedback
    """
    print("\n** Thank you for using Shop-app,")
    print("If you wish to use Shop-app again please click run program")
    print("Goodbye **\n")
    sys.exit()


def main():
    """
    Run all programme functions
    """
    welcome()
    get_data()
    menu_selection()


print("### WELCOME TO SHOP APP ###\n")
main()