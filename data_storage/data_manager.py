import json

def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            if not data:  # Check if the loaded data is empty
                return []  # Return an empty list if the data is empty
            return data
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist
