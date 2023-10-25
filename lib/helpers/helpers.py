from lib.models.painting import Painting

def exit_program():
    print("Goodbye!")
    exit()

def choose_medium():
    for i in range(len(Painting.mediums)):
        print(f"{i + 1}. {Painting.mediums[i]}")
    choice = input("> ")
    try:
        medium = Painting.mediums[int(choice) - 1]
        return medium
    except:
        return None