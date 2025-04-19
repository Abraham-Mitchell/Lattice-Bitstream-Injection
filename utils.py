import json

def reformat_json(file_path, indent=4):
    """Reads a JSON file, reformats it with proper indentation, and overwrites it."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)  # Load JSON data

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=indent)  # Overwrite with formatted JSON

        print(f"Reformatted JSON saved to {file_path}")
    except Exception as e:
        print(f"Error: {e}")