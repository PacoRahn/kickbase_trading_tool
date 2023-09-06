import tkinter as tk
from tkinter import ttk

class FootballManagerGUI:
    def __init__(self, root, add_player_callback):
        self.root = root
        self.add_player_callback = add_player_callback

        self.root.title("Football Manager")

        # Create input fields for player values
        self.name_label = tk.Label(root, text="Name:")
        self.name_entry = tk.Entry(root)

        self.value_label = tk.Label(root, text="Value:")
        self.value_entry = tk.Entry(root)

        self.value_increase_label = tk.Label(root, text="Value Increase:")
        self.value_increase_entry = tk.Entry(root)

        self.percentage_label = tk.Label(root, text="Percentage:")
        self.percentage_entry = tk.Entry(root)

        self.score_label = tk.Label(root, text="Score:")
        self.score_entry = tk.Entry(root)

        # Create the "Add Player" button and link it to the add_player function
        self.add_button = tk.Button(root, text="Add Player", command=self.toggle_input_fields)

        # Arrange widgets using grid layout
        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)
        self.value_label.grid(row=1, column=0)
        self.value_entry.grid(row=1, column=1)
        self.value_increase_label.grid(row=2, column=0)
        self.value_increase_entry.grid(row=2, column=1)
        self.percentage_label.grid(row=3, column=0)
        self.percentage_entry.grid(row=3, column=1)
        self.score_label.grid(row=4, column=0)
        self.score_entry.grid(row=4, column=1)
        self.add_button.grid(row=5, columnspan=2)

        # Create an initially hidden frame for input fields
        self.input_frame = tk.Frame(root)
        self.input_frame.grid(row=6, columnspan=2)
        self.input_frame.grid_remove()  # Initially hide the input frame

        # Create a Treeview widget for displaying player data
        self.tree = ttk.Treeview(root, columns=("ID", "Name", "Value", "Value Increase", "Percentage", "Score"))
        self.tree.heading("#1", text="ID")
        self.tree.heading("#2", text="Name")
        self.tree.heading("#3", text="Value")
        self.tree.heading("#4", text="Value Increase")
        self.tree.heading("#5", text="Percentage")
        self.tree.heading("#6", text="Score")
        self.tree.grid(row=7, columnspan=2)

    def toggle_input_fields(self):
        # Toggle the visibility of the input frame when the "Add Player" button is pressed
        if self.input_frame.winfo_ismapped():
            self.input_frame.grid_remove()
        else:
            self.input_frame.grid()

    def add_player(self):
        # Get player values from user input
        name = self.name_entry.get()
        value = float(self.value_entry.get())
        value_increase = float(self.value_increase_entry.get())
        percentage = float(self.percentage_entry.get())
        score = int(self.score_entry.get())

        # Call the add_player_callback with the entered values
        self.add_player_callback(name, value, value_increase, percentage, score)

        # After adding a player, clear the input fields and update the table
        self.name_entry.delete(0, tk.END)
        self.value_entry.delete(0, tk.END)
        self.value_increase_entry.delete(0, tk.END)
        self.percentage_entry.delete(0, tk.END)
        self.score_entry.delete(0, tk.END)
        self.update_table()

    def update_table(self, players):
        # Clear the existing data in the table
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert player data into the table
        for player in players:
            self.tree.insert("", "end", values=(player.id, player.name, player.value, player.value_increase, player.percentage, player.score))

    def run(self):
        self.root.mainloop()