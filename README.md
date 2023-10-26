
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
- choose_medium

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

### movement_helpers.py

## Models

### artist.py

### painting.py

### movement.py

---
