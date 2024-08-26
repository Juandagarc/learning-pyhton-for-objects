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


def generate_array():
    array = []
    while True:
        number = input('Insert an element (type "exit" to finish): ')
        if number == 'exit':
            break
        else:
            array.append(str(number))
    return array


class ListOfElements:

    def __init__(self, original_elements):
        self.id = len(load_data().get("Elements", []))
        self.input = original_elements
        self.searched = ''
        self.found = ''

    def search_element(self):
        self.searched = input('Insert an element to search: ')
        self.found = self.input.count(self.searched)
        print(f'The element {self.searched} was found {self.found} times in the list.')
        if self.found % 2 == 0:
            self.found = 'even'
        else:
            self.found = 'odd'
        print(f'the element {self.searched} is {self.found}')

    def save_data(self):
        data = load_data()

        if "Elements" not in data:
            data["Elements"] = []

        existing_data = {item["id"]: item for item in data["Elements"]}
        if self.id in existing_data:
            existing_data[self.id]["input"] = self.input
            existing_data[self.id]["searched"] = self.searched
            existing_data[self.id]["found"] = self.found
        else:
            data["Elements"].append({
                "id": self.id,
                "input": self.input,
                "searched": self.searched,
                "found": self.found
            })

        with open(path, 'w') as file:
            json.dump(data, file, indent=4)


def main():
    elements = generate_array()
    print(Fore.YELLOW + "Your list is: " + Style.RESET_ALL, elements)
    list_of_elements = ListOfElements(elements)
    list_of_elements.search_element()
    list_of_elements.save_data()


main()
