# Paintings CLI

## CLI

### cli.py

- `main` utilizes a while loop to keep the user in the main menu until they choose to enter a submenu or exit the program. It calls `main_menu` to print the user's options and prompts the user to choose an option. If the choice is valid, it calls the approprate function. If the choice is invalid, it prints an error message.

- `movements` utilizes a while loop to keep the user in the movements menu until they choose to enter a submenu or return to the main menu. It calls `movements_menu` to print the user's options and prompts the user to choose an option. If the choice is valid, it calls the approprate function. If the choice is invalid, it prints an error message.

- `explore_movement` utilizes a while loop to keep the user in the explore movement menu until they choose to return to the previous menu or enter a sebmenu. It calls `movement_options_menu` to print the movement's details and the user's options and prompts the user to choose an option. If the choice is valid, it calls the approprate function. If the choice is invalid, it prints an error message.

- `artists` utilizes a while loop to keep the user in the artists menu until they choose to enter a submenu or return to the main menu. It calls `artists_menu` to print the user's options and prompts the user to choose an option. If the choice is valid, it calls the approprate function. If the choice is invalid, it prints an error message.

- `explore_artist` utilizes a while loop to keep the user in the explore artist menu until they choose to return to the previous menu or enter a sebmenu. It calls `artist_options_menu` to print the artist's details and the user's options and prompts the user to choose an option. If the choice is valid, it calls the approprate function. If the choice is invalid, it prints an error message.

- `paintings` utilizes a while loop to keep the user in the paintings menu until they choose to enter a submenu or return to the main menu. It calls `paintings_menu` to print the user's options and prompts the user to choose an option. If the choice is valid, it calls the approprate function. If the choice is invalid, it prints an error message.

- `explore_painting` utilizes a while loop to keep the user in the explore painting menu until they choose to return to the previous menu. It calls `painting_options_menu` to print the painting's details and the user's options and prompts the user to choose an option. If the choice is valid, it calls the approprate function. If the choice is invalid, it prints an error message.

### seed.py

Running `python seed.py` will seed the database with some initial data. This data includes a fairly comprehensive list of art movements, several artists, and paintings by some of those artists. The movements, artists, and paintings tables are dropped and recreated every time this command is run.

## Functions

### menus.py

menus.py contains the funtions that display the menus to the user when they are interacting with the CLI. Each function prints the menu title as well as all choices available to the user. It includes the following functions:
- main_menu
- movements_menu
- movements_options_menu also takes in a movement as a parameter and prints the movement's details.
- artist_menu
- artist_options_menu also takes in an artist as a parameter and prints the artist's details.
- paintings_menu
- paintings_options_menu also takes in a painting as a parameter and prints the painting's details

### general_helpers.py

helpers.py contains all helper functions that are not specific to paintings, artists, or movements.

- `exit_program` prints "Goodbye!" and exits the CLI.
- `divider` prints a line and a space.
- `spacer` prints a space.
- `error` calls `spacer` and then prints "Invalid choice" in red.

### movement_helpers.py

movement_helpers.py contains functions executed by user choices in the movements and explore movement menus. All functions that take in a movement as a parameter are a part of the explore movement menu; the movement chosen when entering that menu is automatically passed in to these functions.

- `list_movements` prints an ordered list of movements, sorted by name, if any movements exist. If no movements exist, it prints a message that no movements were found.

- `choose_movement` takes in an optional prompt parameter with the default value "Choose a movement: ". If any movements exist, it prints an ordered list of movements, sorted by name. It then prompts the user to choose a movement using the prompt parameter. If the choice is valid, the movement is returned. If not, an error is printed. If no movements exist, it prints a message that no movements were found.

- `create_movement` prompts the user to input a movement name and founding year. If the values provided are valid, it creates an instance of the movement class, prints a success message, and returns the instance. If they are not valid, it prints an error message.

- `update_movement` takes in a movement. It prompts the user for a new name and new founding year. If the values provided are valid, it updates the movement and prints a success message. If they are not valid, it prints an error message. 

- `delete_movement` takes in a movement. It prompts the user to confirm that they want to delete the movement as well as associated artists and paintings. If the user confirms the deletion, the movement is deleted along with associated artists and paintings and a success message is printed. If the user does not confirm the deletion, an abortion message is printed.

- `list_artists_by_movement` takes in a movement. If any associated artists exist, it prints them in an ordered list, sorted by name. If no associated artists exist, it prints a message that no associated artists were found.

- `choose_artist_by_movement` takes in a movement. If any associated artists exist, it prints them in an ordered list, sorted by name. It then prompts the user to choose an artist. If the choice is valid, the artist is returned. If not, an error message is printed. If no associated artists exist, it prints a message that no associated artists were found.

### artist_helpers.py

artist_helpers.py contains functions executed by user choices in the artists and explore artists menus. All functions that take in an artist as a parameter are called from the explore artist menu; the artist chosen when entering that menu is automatically passed in to these functions.

- `list_artists` prints an ordered list of artists, sorted by name, if any artists exist. If no artists exist, it prints a message that no artists were found.

- `choose_artist` takes in an optional prompt parameter with the default value "Choose an artist: ". If any artists exist, it prints an ordered list of artists, sorted by name. It then prompts the user to choose an artist using the prompt parameter. If the choice is valid, the artist is returned. If not, an error is printed. If no artists exist, it prints a message that no artists were found.

- `create_artist` takes in an optional movement_id parameter with a default value of None. It prompts the user to enter a name. If no movement_id was passed in, it then prompts the user to choose a movement for the artist using `choose_movement`. If the values are valid, it creates an instance of the Artist class, prints a success message, and returns the instance. If any of the values are invalid, it prints an error message.

- `update_artist` takes in an artist. It prompts the user to enter a new name and to choose a new movement. If the values provided are valid, it updates the artist and prints a success message. If they are not valid, it prints an error message. 

- `delete_artist` takes in an artist. It prompts the user to confirm that they want to delete the artist as well as associated paintings. If the user confirms the deletion, the artist is deleted along with associated paintings and a success message is printed. If the user does not confirm the deletion, an abortion message is printed.

- `list_paintings_by_artist` takes in an artist. If any associated paintings exist, it prints them in an ordered list, sorted by name. If no associated painting exist, it prints a message that no associated paintings were found.

- `choose_painting_by_artist` takes in an artist. If any associated paintings exist, it prints them in an ordered list, sorted by name. It then prompts the user to choose a painting. If the choice is valid, the painting is returned. If not, an error message is printed. If no associated paintings exist, it prints a message that no associated paintings were found.

### paintings_helpers.py

painting_helpers.py contains functions executed by user choices in the paintings and explore painting menus. All functions that take in a painting as a parameter are a part of the explore painting menu; the painting chosen when entering that menu is automatically passed in to these functions.

- `choose_medium` takes in an optional prompt parameter with the default value "Choose a medium: ". It prints an ordered list of mediums in `Painting.mediums` and prompts the user to choose one. It returns the medium if the choice is valid and prints an error if it is not.

- `list_paintings` prints an ordered list of paintings, sorted by name, if any paintings exist. If no paintings exist, it prints a message that no paintings were found.

- `choose_painting` takes in an optional prompt parameter with the default value "Choose a painting: ". If any paintings exist, it prints an ordered list of painting, sorted by name. It then prompts the user to choose a painting using the prompt parameter. If the choice is valid, the painting is returned. If not, an error is printed. If no paintings exist, it prints a message that no paintings were found.

- `create_painting` takes in an optional artist_id parameter with a default value of None. It prompts the user to enter a name and a year and to choose a medium using `choose_medium`. If no artist_id was passed in, it then prompts the user to choose an artist for the painting using `choose_artist`. If the values are valid, it creates an instance of the Painting class, prints a success message, and returns the instance. If any of the values are invalid, it prints an error message.

- `update_painting` takes in a painting. It prompts the user to enter a new name and year and to choose a new medium and artist. If the values provided are valid, it updates the painting and prints a success message. If they are not valid, it prints an error message. 

- `delete_painting` takes in a painting. It prompts the user to confirm that they want to delete the painting. If the user confirms the deletion, the painting is deleted and a success message is printed. If the user does not confirm the deletion, an abortion message is printed.

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
