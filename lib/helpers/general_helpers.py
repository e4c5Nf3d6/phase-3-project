from termcolor import cprint

def exit_program():
    cprint("Goodbye!", "green")
    spacer()
    exit()
    
def divider():
    print("_______________________________________________")
    print("")

def spacer():
    print(" ")

def error():
    spacer()
    cprint("Invalid choice", "red")
