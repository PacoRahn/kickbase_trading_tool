# main.py

import tkinter as tk
from entities.player import Player
from data_storage.data_manager import save_data, load_data
from gui.gui import FootballManagerGUI

# Initialize players with data from the JSON file or an empty list if it doesn't exist
players = load_data('data_storage/player_data.json')

# Function to add a player and save data
def add_player(name, value, value_increase, percentage, score):
    # Create a Player object with the entered values
    player = Player(len(players) + 1, name, value, value_increase, percentage, 0, "", "", score)

    # Append the player to the players list
    players.append(player)

    # Update the table
    gui.update_table(players)

    # Save the updated data
    save_data(players, 'data_storage/player_data.json')



# Create the main application window
root = tk.Tk()

# Create an instance of the FootballManagerGUI class and pass the add_player function
gui = FootballManagerGUI(root, add_player)

# Run the GUI
gui.run()
