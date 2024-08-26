# colorama is for the color of the text
# Example of using colorama: https://pypi.org/project/colorama/
from colorama import Fore, Style

# Json module is used to load data from file
import json

path = 'data.json'


def load_data():
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


class SortedList:

    def __init__(self, original_elements):
        self.id = len(load_data().get("Elements", []))
        self.input = original_elements

