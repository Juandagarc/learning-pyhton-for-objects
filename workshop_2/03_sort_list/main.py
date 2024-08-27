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
        self.output = []

    def order_list(self):
        even_list = []
        odd_list = []
        for element in self.input:
            if len(element) % 2 == 0:
                even_list.append(element)
            else:
                odd_list.append(element)

        even_list.sort(key=lambda s: len(s))
        odd_list.sort(key=lambda s: len(s))
        return even_list + odd_list

    def save_data(self):
        data = load_data()

        if "Elements" not in data:
            data["Elements"] = []

        existing_data = {item["id"]: item for item in data["Elements"]}
        if self.id in existing_data:
            existing_data[self.id]["input"] = self.input
            existing_data[self.id]["output"] = self.output
        else:
            data["Elements"].append({
                "id": self.id,
                "input": self.input,
                "output": self.output
            })

        with open(path, 'w') as file:
            json.dump(data, file, indent=4)


def main():
    array = []
    while True:
        number = input('Insert an element (type "exit" to finish): ')
        if number == 'exit':
            break
        else:
            array.append(str(number))

    sorted_list = SortedList(array)
    sorted_list.output = sorted_list.order_list()
    print(Fore.YELLOW + f'The sorted list is: {sorted_list.output}' + Style.RESET_ALL)
    sorted_list.save_data()


main()
