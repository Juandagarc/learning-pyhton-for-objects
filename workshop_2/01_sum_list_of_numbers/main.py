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


def sum_numbers_in_list(number):
    numbers = str(number)
    sum_of_numbers = int(numbers[0]) + int(numbers[1])
    return int(sum_of_numbers)


def generate_sum_output(array_of_int):
    sum_output = []
    for element in array_of_int:
        sum_output.append(sum_numbers_in_list(element))
    return sum_output


def generate_array():
    array = []
    while True:
        number = input('Insert a number (type "exit" to finish): ')
        if number == 'exit':
            break
        if len(number) == 2 and number.isdigit():
            array.append(int(number))
        else:
            print(Fore.RED + 'Please insert a number of two digits!' + Style.RESET_ALL)
    return array


class ListOfNumbers:
    def __init__(self, original_numbers, after_numbers):
        self.id = len(load_data().get("sum_list_of_numbers", []))
        self.input = original_numbers
        self.list_of_numbers = after_numbers

    def save_data(self):
        data = load_data()

        if "sum_list_of_numbers" not in data:
            data["sum_list_of_numbers"] = []

        existing_data = {item["id"]: item for item in data["sum_list_of_numbers"]}
        if self.id in existing_data:
            existing_data[self.id]["input"] = self.input
            existing_data[self.id]["output"] = self.list_of_numbers
        else:
            data["sum_list_of_numbers"].append({
                "id": self.id,
                "input": self.input,
                "output": self.list_of_numbers
            })
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)
        return 'Data saved successfully!'


def main():
    array = generate_array()
    print(Fore.YELLOW + 'The array is:' + Style.RESET_ALL, array)
    summed_output = generate_sum_output(array)
    print(Fore.YELLOW + 'The sum of the numbers is:' + Style.RESET_ALL, summed_output)

    # Create a ListOfNumbers instance and save data
    list_of_numbers = ListOfNumbers(array, summed_output)
    print(Fore.YELLOW + 'Do you want to save the data? (y/n)' + Style.RESET_ALL)
    choice = input()
    if choice == 'y':
        print(list_of_numbers.save_data())
    else:
        print(Fore.RED + 'Data not saved!' + Style.RESET_ALL)


main()
