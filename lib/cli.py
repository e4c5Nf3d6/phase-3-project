# lib/cli.py

from helpers import (
    exit_program,
    helper_1
)


def main():
    m = "main"
    while m == "main":
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            m = "sub"
            while m == "sub":
                submenu()
                choice = input("> ")
                if choice == "0":
                    m = "main"
                elif choice == "1":
                    helper_1()
                elif choice == "2":
                    helper_1()
                else:
                    print("Invalid choice")
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Submenu")

def submenu():
    print("Please select an option:")
    print("0. Go back to main menu")
    print("1. Option 1")
    print("2. Option 2")


if __name__ == "__main__":
    main()
