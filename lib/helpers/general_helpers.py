from termcolor import cprint

from models.painting import Painting

def exit_program():
    spacer()
    cprint("Goodbye!", "green")
    spacer()
    exit()
    
def divider():
    print("_______________________________________________")
    print("")

def spacer():
    print(" ")

def choose_medium():
    for medium in Painting.mediums:
        print(f"{Painting.mediums.index(medium) + 1}. {medium}")
    choice = input("Enter your choice: ")
    try:
        medium = Painting.mediums[int(choice) - 1]
        return medium
    except:
        return None