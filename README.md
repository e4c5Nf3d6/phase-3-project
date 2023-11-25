# Paintings CLI

## CLI

### cli.py

- main
- artists
- explore_artist
- paintings
- explore_painting
- movements
- explore_movement

### seed.py

Running `python seed.py` will seed the database with some initial data. This data includes a comprehensive list of art movements, several painters, and paintings by some of those painters. The tables will be dropped and recreated every time this command is run.

## Functions

### menus.py

menus.py contains the funtions that display the menus to the user when they are interacting with the CLI. Each function prints the menu title as well as all choices available to the user. It includes the following functions:
- main_menu
- artist_menu
- artist_options_menu
- paintings_menu
- paintings_options_menu
- movements_menu
- movements_options_menu

### general_helpers.py

helpers.py contains all helper functions that are not specific to paintings, artists, or movements.

- `exit_program` prints "Goodbye!" and exits the CLI.
- `divider` prints a line and a space.
- `spacer` prints a space.
- `error` calls `spacer` and then prints "Invalid choice" in red.

### movement_helpers.py

movement_helpers.py contains functions executed by user choices in the movements and explore movement menus. All functions that take in a movement as a parameter are a part of the explore movement menu; the movement chosen when entering that menu is automatically passed in to these functions.

<!-- def list_movements():
    movements = sorted(Movement.get_all(), key=lambda x: x.name.lower())
    if movements:
        for movement in movements:
            cprint(f"{movements.index(movement) + 1}. {movement.name}", "green")
    else:
        cprint("No movements found", "red") -->

<!-- def choose_movement(prompt="Choose a movement: "):
    movements = sorted(Movement.get_all(), key=lambda x: x.name.lower())
    if movements:
        for movement in movements:
            print(f"{movements.index(movement) + 1}. {movement.name}")
        spacer()
        id = input(prompt)
        try:
            if int(id) <= 0:
                raise ValueError
            return movements[int(id) - 1]
        except:
            error()
    else:
        spacer()
        cprint("No movements found", "red") -->

<!-- def create_movement():
    name = input("Enter the movement's name: ")
    year_founded = input("Enter the movement's founding year: ")
    spacer()
    try:
        movement = Movement.create(name, year_founded)
        cprint(f'{movement.name} movement successfully created', "green")
        return movement
    except Exception as exc:
        cprint(f"Error creating movement: {exc}", "red") -->

<!-- def update_movement(movement):
    original_name = movement.name
    try:
        name = input("Enter the movement's new name: ")
        movement.name = name
        year_founded = input("Enter the movement's new founding year: ")
        movement.year_founded = year_founded

        movement.update()
        spacer()
        cprint(f"{movement.name} movement successfully updated", "green")
    except Exception as exc:
        movement.name = original_name
        spacer()
        cprint(f"Error updating movement: {exc}", "red") -->

<!-- def delete_movement(movement):
    confirmation_text = colored(
        "Deleting a movement will delete all associated artists and paintings. Are you sure you want to proceed? Y/N: ", 
        "yellow", 
        attrs=["bold"]
    )
    spacer()
    confirmation = input(confirmation_text)
    spacer()
    if confirmation == "y" or confirmation == "Y":
        artists = Artist.find_by_movement(movement.id)
        for artist in artists:
            paintings = Painting.find_by_artist(artist.id)
            for painting in paintings:
                painting.delete()
            artist.delete()
        movement.delete()
        cprint(f'{movement.name} movement successfully deleted', "green")
        return("deleted")
    else:
        cprint("Deletion aborted", "green") -->

<!-- def list_artists_by_movement(movement):
    artists = sorted(Artist.find_by_movement(movement.id), key=lambda x: x.name.lower())
    if artists:
        for artist in artists:
            cprint(artist.name, "green")
    else:
        cprint(f'No {movement.name} artists found', "red") -->

<!-- def choose_artist_by_movement(movement):
    artists = sorted(Artist.find_by_movement(movement.id), key=lambda x: x.name.lower())
    if artists:
        for artist in artists:
            print(f"{artists.index(artist) + 1}. {artist.name}")
        spacer()
        id = input("Choose an artist: ")
        try:
            if int(id) == 0:
                raise ValueError
            return artists[int(id) - 1]
        except:
            error()
    else:
        cprint(f"No {movement.name} artists found", "red") -->

### artist_helpers.py

artist_helpers.py contains functions executed by user choices in the artists and explore artists menus. All functions that take in an artist as a parameter are called from the explore artist menu; the artist chosen when entering that menu is automatically passed in to these functions.

<!-- def list_artists():
    artists = sorted(Artist.get_all(), key=lambda x: x.name.lower())
    if artists:
        for artist in artists:
            cprint(f"{artists.index(artist) + 1}. {artist.name}", "green")
    else:
        cprint("No artists found", "red") -->

<!-- def choose_artist(prompt="Choose an artist: "):
    artists = sorted(Artist.get_all(), key=lambda x: x.name.lower())
    for artist in artists:
        print(f"{artists.index(artist) + 1}. {artist.name}")
    spacer()
    id = input(prompt)
    try:
        if int(id) <= 0:
            raise ValueError
        return artists[int(id) - 1]
    except:
        error()   -->

<!-- def create_artist(movement_id=None):
    name = input("Enter the artist's name: ")
    spacer()
    if not movement_id:
        try:
            movement_id = choose_movement("Choose the artist's movement: ").id
            spacer()
        except:
            return None
    try:
        artist = Artist.create(name, movement_id)
        cprint(f'{artist.name} created successfully', "green")
        return artist
    except Exception as exc:
        cprint(f"Error creating artist: {exc}", "red") -->

<!-- def update_artist(artist):
    try:
        name = input("Enter the artist's new name: ")
        movement = choose_movement("Choose the artist's new movement: ")

        if movement:
            artist.name = name
            artist.movement_id = movement.id

            artist.update()
            spacer()
            cprint(f"{artist.name} updated successfully", "green")
    except Exception as exc:
        spacer()
        cprint(f"Error updating artist: {exc}", "red") -->

<!-- def delete_artist(artist):
    confirmation_text = colored(
        "Deleting an artist will delete all associated paintings. Are you sure you want to proceed? Y/N: ", 
        "yellow", 
        attrs=["bold"]
    )
    spacer()
    confirmation = input(confirmation_text)
    spacer()
    if confirmation == "y" or confirmation == "Y":
        paintings = Painting.find_by_artist(artist.id)
        for painting in paintings:
            painting.delete()
        artist.delete()
        cprint(f'{artist.name} deleted', "green")
        return "deleted"
    else:
        cprint('Deletion aborted', "green") -->

<!-- def list_paintings_by_artist(artist):
    paintings = sorted(Painting.find_by_artist(artist.id), key=lambda x: x.name.lower())
    spacer()
    if paintings:
        for painting in paintings:
            cprint(f"{painting.name}, {painting.year}", "green")
    else:
        cprint(f'No paintings by {artist.name} found', "red") -->

<!-- def choose_painting_by_artist(artist):
    paintings = sorted(Painting.find_by_artist(artist.id), key=lambda x: x.name.lower())
    if paintings:
        for painting in paintings:
            print(f"{paintings.index(painting) + 1}. {painting.name}")
        spacer()
        id = input("Enter the painting's ID: ")
        try:
            if int(id) <= 0:
                raise ValueError
            return paintings[int(id) - 1]
        except:
            error()
    else:
        spacer()
        cprint(f"No paintings by {artist.name} found", "red") -->

### paintings_helpers.py

painting_helpers.py contains functions executed by user choices in the paintings and explore painting menus. All functions that take in a painting as a parameter are a part of the explore painting menu; the painting chosen when entering that menu is automatically passed in to these functions.

<!-- def choose_medium(prompt="Choose a medium: "):
    for medium in Painting.mediums:
        print(f"{Painting.mediums.index(medium) + 1}. {medium}")
    spacer()
    choice = input(prompt)
    try:
        if int(choice) <= 0:
            raise ValueError
        medium = Painting.mediums[int(choice) - 1]
        return medium
    except:
        error() -->

<!-- def list_paintings():
    paintings = sorted(Painting.get_all(), key=lambda x: x.name.lower())
    if paintings:
        for painting in paintings:
            cprint(f"{paintings.index(painting) + 1}. {painting.name}, {Artist.find_by_id(painting.artist_id).name}", "green")
    else:
        cprint("No paintings found", "red") -->

<!-- def choose_painting():
    paintings = sorted(Painting.get_all(), key=lambda x: x.name.lower())
    if paintings:
        for painting in paintings:
            print(f"{paintings.index(painting) + 1}. {painting.name}, {Artist.find_by_id(painting.artist_id).name}")
        spacer()
        id = input("Choose a painting: ")
        try:
            if int(id) <= 0:
                raise ValueError
            return paintings[int(id) - 1]
        except:
            error()
    else:
        cprint("No paintings found", "red") -->

<!-- def create_painting(artist_id=None):
    name = input("Enter the painting's name: ")
    year = input("Enter the painting's year: ")
    spacer()
    medium = choose_medium("Choose the painting's medium: ")

    if not medium:
        return None
    
    if not artist_id:
        try:
            artist_id = choose_artist("Choose the painting's artist: ").id
        except:
            return None
        
    spacer()
    try:
        painting = Painting.create(name, year, medium, artist_id)
        cprint(f'{painting.name} successfully created', "green")
        return painting
    except Exception as exc:
        cprint(f"Error creating painting: {exc}", "red") -->

<!-- def update_painting(painting):
    original_name = painting.name
    original_year = painting.year
    original_medium = painting.medium
    try:
        name = input("Enter the painting's new name: ")
        year = input("Enter the painting's new year: ")
        spacer()
        medium = choose_medium("Choose the painting's new medium: ")

        if not medium:
            return None
        
        artist = choose_artist("Choose the painting's new artist: ")

        if artist:
            painting.name = name
            painting.year = year       
            painting.medium = medium
            painting.artist_id = artist.id

            painting.update()
            spacer()
            cprint(f"{painting.name} successfully updated", "green")
    
    except Exception as exc:
        painting.name = original_name
        painting.year = original_year
        painting.medium = original_medium
        spacer()
        cprint(f"Error updating painting: {exc}", "red") -->

<!-- def delete_painting(painting):
    confirmation_text = colored(
        "Are you sure you want to proceed? Y/N: ", 
        "yellow", 
        attrs=["bold"]
    )
    spacer()
    confirmation = input(confirmation_text)
    spacer()
    if confirmation == "y" or confirmation == "Y":
        painting.delete()
        cprint(f'{painting.name} successfully deleted', "green")
        return "deleted"
    else:
        cprint("Deletion aborted", "green") -->

## Models

### movement.py

movement.py contains the Movement class.

- `__init__` is the constructor used to initialize an instance of the Movement class. It takes in a name and a year_founded and sets the instance's attributes. It also sets an id attribute to `None`.

- `__repr__` returns a string representation of an instance of the Movement class.

- Class Variables
    - `all` is a dictionary to which instances of the Movement class are saved with their ID as a key.

- Instance Attributes  
    - `id` is the movement's ID.     
    - `name` is a property. For `name` to be set, it must be a non-empty string.
    - `year_founded` is a property. for `year_founded` to be set, it must be an integer between 0 and 2023.
        
 - Class Methods
    - `create_table` creates a movements table if one does not exist.
    - `drop_table` drops the movements table if it exists.
    - `create` takes in a name and a year_founded, initializes a new Movement instance, saves it using the `save` instance method, and returns the movement.

    - `instance_from_db` takes in a row from the movements table and checks `Movement.all` for a key that matches the row's primary key. If the movement exists in the dictionary, it updates the Movement instance's attributes to match the row's values. If the movement does not exist in the dictionary, the method creates a new instance and saves it to `Movement.all`. It then returns the Movement instance.
    - `get_all` fetches all rows from the movements table and uses `instance_from_db` to convert them into instances. If there are any instances, it returns them in a list. If not, it returns `None`.
    - `find_by_id` takes in an ID, fetches the matching row from the movements table, and converts it to an instance using `instance_from_db`. If the instance exists, it is returned. If not, the method returns `None`.
    - `find_by_name` takes in a name and fetches all matching rows from the movements table. It then converts them to instances using `instance_from_db`. If there are any instances, they are returned in a list. If not, the method returns `None`.

- Instance Methods
    - `save` inserts the values of the attributes of an instance into a new row of the movements table, gets the ID of the new row and sets it as the instance's ID, then adds the instance to `Movement.all` as a value with the key of that ID.
    - `update` updates the row of the movements table that has a primary key that matches the instance's id, setting the values in the row to the values of the instance's attributes.
    - `delete` removes the row of the moveements table that has a primary key that matches the instance's id, sets the instances ID to `None`, and removes the instance from `Movement.all`.

### artist.py

artist.py contains the Artist class.

- `__init__` is the constructor used to initialize an instance of the Artist class. It takes in a name and a movement_id and sets the instance's attributes. It also sets an id attribute to `None`.

- `__repr__` returns a string representation of an instance of the Artist class.

- Class Variables
    - `all` is a dictionary to which instances of the Artist class are saved with their ID as a key.

- Instance Attributes  
    - `id` is the artist's ID.
    - `name` is a property. For `name` to be set, it must be a non-empty string.
    - `movement_id` is a property. For `movement_id` to be set, it must reference a movement in the database.
        
- Class Methods
    - `create_table` creates an artists table if one does not exist.
    - `drop_table` drops the artists table if it exists.
    - `create` takes in a name and a movement_id, initializes a new Artist instance, saves it using the `save` instance method, and returns the artist.
    - `instance_from_db` takes in a row from the artists table and checks `Artist.all` for a key that matches the row's primary key. If the artist exists in the dictionary, it updates the artist instance's attributes to match the row's values. If the artist does not exist in the dictionary, the method creates a new instance and saves it to `Artist.all`. It then returns the Artist instance.
    - `get_all` fetches all rows from the artists table and uses `instance_from_db` to convert them into instances. If there are any instances, it returns them in a list. If not, it returns `None`.
    - `find_by_id` takes in an ID, fetches the matching row from the artists table, and converts it to an instance using `instance_from_db`. If the instance exists, it is returned. If not, the method returns `None`.
    - `find_by_name` takes in a name and fetches all matching rows from the artists table. It then converts them to instances using `instance_from_db`. If there are any instances, they are returned in a list. If not, the method returns `None`.
    - `find_by_movement` takes in a movement_id and fetches all matching rows from the artists table. It then converts them to instances using `instance_from_db`. If there are any instances, they are returned in a list. If not, the method returns `None`.

- Instance Methods
    - `save` inserts the values of the attributes of an instance into a new row of the artists table, gets the ID of the new row and sets it as the instance's ID, then adds the instance to `Artist.all` as a value with the key of that ID.
    - `update` updates the row of the artists table that has a primary key that matches the instance's id, setting the values in the row to the values of the instance's attributes.
    - `delete` removes the row of the artists table that has a primary key that matches the instance's id, sets the instances ID to `None`, and removes the instance from `Artist.all`.

### painting.py

painting.py contains the Painting class.

- `__init__` is the constructor used to initialize an instance of the Painting class. It takes in a name, year, medium, and an artist_id and sets the instance's attributes. It also sets an id attribute to `None`.

- `__repr__` returns a string representation of an instance of the Painting class.

- Class Variables
    - `all` is a dictionary to which instances of the Painting class are saved with their ID as a key.
    - `mediums` is a list of accepted mediums for an instance of the Painting class.

- Instance Attributes  
    - `id` is the painting's ID.
    - `name` is a property. For `name` to be set, it must be a non-empty string.
    - `year` is a property. for `year` to be set, it must be an integer between 0 and 2023.
    - `medium` is a property. for `medium` to be set, it must be in `Painting.mediums`.
    - `artist_id` is a property. For `artist_id` to be set, it must reference an artist in the database.
        
 - Class Methods
    - `create_table` creates a paintings table if one does not exist.
    - `drop_table` drops the paintings table if it exists.
    - `create` takes in a name, year, medium, and an artist_id, initializes a new Painting instance, saves it using the `save` instance method, and returns the painting.

    - `instance_from_db` takes in a row from the paintings table and checks `Painting.all` for a key that matches the row's primary key. If the painting exists in the dictionary, it updates the painting instance's attributes to match the row's values. If the painting does not exist in the dictionary, the method creates a new instance and saves it to `Painting.all`. It then returns the Painting instance.
    - `get_all` fetches all rows from the paintings table and uses `instance_from_db` to convert them into instances. If there are any instances, it returns them in a list. If not, it returns `None`.
    - `find_by_id` takes in an ID, fetches the matching row from the paintings table, and converts it to an instance using `instance_from_db`. If the instance exists, it is returned. If not, the method returns `None`.
    - `find_by_name` takes in a name and fetches all matching rows from the paintings table. It then converts them to instances using `instance_from_db`. If there are any instances, they are returned in a list. If not, the method returns `None`.
    - `find_by_artist` takes in an artist_id and fetches all matching rows from the paintings table. It then converts them to instances using `instance_from_db`. If there are any instances, they are returned in a list. If not, the method returns `None`.

- Instance Methods
    - `save` inserts the values of the attributes of an instance into a new row of the paintings table, gets the ID of the new row and sets it as the instance's ID, then adds the instance to `Painting.all` as a value with the key of that ID.
    - `update` updates the row of the paintings table that has a primary key that matches the instance's id, setting the values in the row to the values of the instance's attributes.
    - `delete` removes the row of the paintings table that has a primary key that matches the instance's id, sets the instances ID to `None`, and removes the instance from `Painting.all`.

---
