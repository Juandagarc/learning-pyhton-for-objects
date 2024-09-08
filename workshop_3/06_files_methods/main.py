# colorama is for the color of the text
# Example of using colorama: https://pypi.org/project/colorama/
from colorama import init, Fore, Style

# Json module is used to load data from file
import json

init(autoreset=True)


class FileManager:
    def __init__(self, filepath):
        self.filepath = filepath

    def create_file(self, action='w'):
        try:
            with open(self.filepath, action) as file:
                print(Fore.GREEN + f"File created or opened successfully: {self.filepath}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error creating or opening file: {e}" + Style.RESET_ALL)

    def write_to_file(self, content):
        try:
            with open(self.filepath, 'w') as file:
                json.dump(content, file, indent=4)
                print(Fore.GREEN + "Content written to file successfully." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error writing to file: {e}" + Style.RESET_ALL)

    def read_from_file(self):
        try:
            with open(self.filepath, 'r') as file:
                content = json.load(file)
                print(Fore.CYAN + "File content:" + Style.RESET_ALL)
                print(json.dumps(content, indent=4))
        except Exception as e:
            print(Fore.RED + f"Error reading file: {e}" + Style.RESET_ALL)


# Example usage
filepath = 'example_file.json'
manager = FileManager(filepath)

# Create a file (or open if it already exists)
manager.create_file('w')

# Write JSON content to the file
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "is_active": True
}
manager.write_to_file(data)

# Read JSON content from the file
manager.read_from_file()
