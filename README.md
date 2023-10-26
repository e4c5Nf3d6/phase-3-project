
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

### menus.py

menus.py contains the funtions that display the menus to the user when they are interacting with the CLI. Each function prints the menu title as well as all choices available to the user. It includes the following functions:
- main_menu
- artist_menu
- artist_options_menu
- paintings_menu
- paintings_options_menu
- movements_menu
- movements_options_menu

### seed.py

Running `python seed.py` will seed the database with some initial data. This data includes a comprehensive list of art movements, several painters, and some paintings by some of those painters. The tables will be dropped and recreated every time this command is run.

## Functions

### helpers.py

- exit_program
    - prints goodbye and exits

- choose_medium
    - prints choice for each medium in Painting.mediums
    - prompts user to choose
    - returns medium or None

### artist_helpers.py

`artist_helpers.py` contains all functions executed by user choices in the artist menu. Any functions that take in an artists as a parameter are a part of the explore artist menu; the artist chosen when entering that menu is automatically passed in to these functions.

- `list_artists` prints each artist.
- `find_artist_by_name` prompts the user to enter an artist's name. If any artists have names that match the input, those artists are printed. If not, the function prints a message that no matching artist was found.
- `find_artist_by_id` prompts the user to enter an artist's id. If an artist has an id that matches the input, that artist is printed. If not, the function prints a message that no matching artist was found. (The function takes an optional parameter, result, that has a default value of "print". If the value "return" is passed in, the function returns the artist instead of printing and returns `None` if there is no match.)
- `create_artist` prompts the user to enter an artist's name and a movement id. If both are valid, the function creates and prints the artist. Otherwise, the function prints an error message.
- `update_artist` prompts the user to enter an artist's id. If a matching artist exists in the database, the function prompts the user to input a new name and a new movement id. If both are valid, it updates and prints artist. Otherwise, it prints an error message. If no matching artist exists, it prints a message that no matching artist was found.
- `delete_artist` prompts the user to enter an artist's id. If a matching artist exists in the database, the function prompts the user to confirm the deletion. If confirmed, the artist and all associated paintings are deleted and deletion messages are printed. If not confirmed, a message is printed that the deletion was aborted. If no matching artist exists, it prints a message that no matching artist was found.
- `list_paintings_by_artist` takes in an artist as a parameter. If any paintings are associated with that artists, they are printed. If not, a message that none were found is printed.
- `display_artist_movement` takes in an artist as a parameter and prints the associated movement.
- `list_artists_in_same_movement`takes in an artist as a parameter. If any other artists are associated with the movement with which the artist is associated, they are printed. If not, a message that no other artists were found is printed.
- `list_artist_mediums`takes in an artist as a parameter. If any paintings are associated with the artist, a list of mediums are printed. If not, a message that none were found is printed.

### paintings_helpers.py

`painting_helpers.py`contains all functions executed by user choices in the paintings menu. Any functions that take in a painting as a parameter are a part of the explore painting menu; the painting chosen when entering that menu is automatically passed in to these functions.

- `list_paintings` prints each painting.
- `find_painting_by_name`prompts the user for a painting's name. If any paintings match, it prints all matching paintings. If not, it prints a message that no matching painting was found. 
- `find_painting_by_id` prompts the user to enter a painting's id. If a painting has an id that matches the input, that painting is printed. If not, the function prints a message that no matching painting was found. (The function takes an optional parameter, result, that has a default value of "print". If the value "return" is passed in, the function returns the painting instead of printing and returns `None` if there is no match.)
- `create_painting` prompts the user to enter a painting name and year, prompts them to choose a medium, and prompts them to enter an artist_id. If all inputs are valid, the function creates and prints a painting. If not, it prints an error message.
- `update_painting` prompts the user to enter a painting's id. If a matching painting exists, the function prompts the user to enter a new painting name and year, prompts them to choose a new medium, and prompts them to enter a new artist_id. If all inputs are valid, the function updates and prints the painting. If not, it prints an error message. If a matching painting does not exist, a message that no matching painting was found is printed.
- `delete_painting`prompts the user to enter a painting's id. If a matching painting exists in the database, the function prompts the user to confirm the deletion. If confirmed, the painting is deleted and a deletion message is printed. If not confirmed, a message is printed that the deletion was aborted. If no matching painting exists, it prints a message that no matching painting was found.
- `display_artist` takes in a painting as a parameter and prints the associated artist.
- `list_paintings_by_same_artist` takes in painting as a parameter. If any other paintings are associated with the artist with which the painting is associated, they are printed. If not, a message that no other paintings were found is printed.
- `list_paintings_by_medium` prompts the user to choose a medium. If the choice is valid, the function prints each painting with the chosen medium or a message that none were found. If not, it prints a message that the choice was invalid.
- `list_paintings_by_year` prints all paintings in chronological order.

### movement_helpers.py

`movement_helpers.py`contains all functions executed by user choices in the movements menu. Any functions that take in a movement as a parameter are a part of the explore movement menu; the movement chosen when entering that menu is automatically passed in to these functions.

- `list_movements` prints each movement.
- `find_movement_by_name` prompts the user to enter a movement's name. If a matching movement is found, it is printed. If not, a message that no matching movement was found is printed. (The function takes an optional parameter, result, that has a default value of "print". If the value "return" is passed in, the function returns the movement instead of printing and returns `None` if there is no match.)
- `find_movement_by_id` prompts the user to enter a movement's id. If a matching movement is found, it is printed. If not, a message that no matching movement was found is printed.
- `create_movement` prompts the user to enter a name and year_founded. If both are valid, a movement is created and printed. If not, an error message is displayed.
- `update_movement` prompts the user to enter a movement's id. If a matching movement exists, the function prompts the user to enter a new movement name and year_founded. If both are valid, the function updates and prints the movement. If not, it prints an error message. If a matching movement does not exist, a message that no matching movement was found is printed.
- `delete_movement` prompts the user to enter a movement's id. If a matching movement exists, the function prompts the user to confirm the deletion. If the deletion is confirmed, the movement is deleted along with associated artists and paintings and deletion messages are printed. If it is not confirmed, a message that the deletion was aborted is printed. If no matching movement exists, a message that no matching movement was found is printed.
- `list_artists_by_movement` takes in a movement as a parameter. If any artists are associated with that movement, they are printed. If not, a message that no associated artists were found is printed.
- `list_paintings_by_movement` takes in a movement as a parameter. If any paintings are associated with any artists that are associated with that movement, they are printed. If not, a message that no associated paintings were found is printed.
- `list_movements_by_year` prints all movements in chronological order.

## Models

### artist.py

### painting.py

### movement.py

---
