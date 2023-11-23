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
