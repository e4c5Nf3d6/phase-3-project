from termcolor import cprint

from models.painting import Painting

def exit_program():
    cprint("Goodbye!", "green")
    spacer()
    exit()
    
def divider():
    print("_______________________________________________")
    print("")

def spacer():
    print(" ")

def choose_medium(prompt="Choose a medium: "):
    for medium in Painting.mediums:
        print(f"{Painting.mediums.index(medium) + 1}. {medium}")
    spacer()
    choice = input(prompt)
    try:
        medium = Painting.mediums[int(choice) - 1]
        return medium
    except:
        return None