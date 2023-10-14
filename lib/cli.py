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
            m = "artists"
            while m == "artists":
                artists()
                choice = input("> ")
                if choice == "0":
                    m = "main"
                elif choice == "1":
                    helper_1()
                elif choice == "2":
                    helper_1()
                else:
                    print("Invalid choice")
        elif choice == "2":
            m = "paintings"
            while m == "paintings":
                paintings()
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
    print("Main Menu")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Artists")
    print("2. Paintings")

def artists():
    print("Artist Menu")
    print("Please select an option:")
    print("0. Go back to main menu")
    print("1. Artist Option 1")
    print("2. Artist Option 2")

def paintings():
    print("Paintings Menu")
    print("Please select an option:")
    print("0. Go back to main menu")
    print("1. Painting Option 1")
    print("2. Painting Option 2")


if __name__ == "__main__":
    main()
