
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

- list_artists
    - prints each artist

- find_artist_by_name
    - prompts the user to enter an artist name
    - prints all artists that match
    - prints artist not found if none match

- find_artist_by_id:
    - optional parameter
    - prompts the user to enter an artist id
    - prints (or returns) the artist that matches
    - prints artist not found if none match

- create_artist:
    - prompts the user to enter an artist name
    - prompts the user to enter a movement id
    - creates and prints an artist if both are valid, else prints error

- update_artist
    - prompts the user to enter an artist id
    - if artist exists, prompts user to input a name and movement id, else prints error
    - if both are valid, updates and prints artist, else prints error

- delete_artist
    - prompts the user to enter an artist id
    - prints error if artist doesn't exist
    - prompts user to confirm deletion if artist exists
    - deletes artist and all associated paintings if confirmed and prints deletion messages, else prints deletion aborted

- list_paintings_by_artist
    - takes in artist as parameter
    - if paintings by artist exist, prints each
    - else prints none found

- display_artist_movement
    - takes in artist
    - displays associated movement

- list_artists_in_same_movement
    - takes in artist
    - if others, prints
    - else prints no others

- list_artist_mediums
    - prints mediums used by artist
    - else prints none

### paintings_helpers.py

- list_paintings
    prints all paintings

- find_painting_by_name
    - prompts user for painting name
    - prints all matching paintings if any else none found

- find_painting_by_id
    - optional parameter
    - prompts for painting id
    - prints painting if found else not found

- create_painting
    - prompts user for name, year, choose medium, artist_id
    - if all valid, creates and prints painting, else error

- update_painting
    - prompts for painting id
    - if exists prompts for new name, year, choose medium, artist_id
    - if valid, updates and prints painting else prints error
    - if not exists, prints not found

- delete_painting
    - prompts for painting id
    - if not exists, prints not found
    - if exists, asks for confirmation
    - if confirmed, deletes painting and prints deletion confirmation
    - if not confirmed, prints abort message

- display_artist
    - takes in painting
    - prints associated artist

- list_paintings_by_same_artist
    - takes in painting
    - prints all other paintings by associated artist if any, else none found

- list_paintings_by_medium
    - prompts user to choose medium
    - if valid, prints all paintings with that medium if any else none found
    - if not valid prints invalid choice

- list_paintings_by_year
    - prints paintings in chronological order

### movement_helpers.py

- list_movements
    - lists all movements

- find_movement_by_name
    - optional parameter
    - prompts user for movement name
    - prints or returns movement if exists, else not found

- find_movement_by_id
    - prompts user for movement id
    - prints movement if found else not found

- create_movement
    - prompts user for movement name and year_founded
    - creates movement and prints if valid, else error

- update_movement
    - prompts user for movement id
    - if not valid, print error
    - if valid, prompts user to enter new name and year_founded
    - if new name valid, update and print movement else error

- delete_movement
    - prompts user for movement id
    - if exists, asks for confirmation, else print not found
    - if confirmed, deletes movement and associated artists and paintings and prints deletion confirmations
    - if not confirmed, prints abort message

- list_artists_by_movement
    - takes in a movement
    - prints all associated artists if any else none

def list_paintings_by_movement(movement):
    - takes in a movement
    - prints all associated paintings if any else none

## Models

### artist.py

### painting.py

### movement.py

---
