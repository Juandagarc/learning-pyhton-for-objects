import json
from colorama import init, Fore, Style

init(autoreset=True)


class ListProcessor:
    def __init__(self, initial_list):
        self.original_list = initial_list

    def save_to_file(self, filename, data):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(Fore.GREEN + f"Saved data to {filename}" + Style.RESET_ALL)

    def process_list(self):
        # 1. Save the initial list
        self.save_to_file('initial_list.json', self.original_list)

        # 2. Separate integers and strings
        integers = [item for item in self.original_list if isinstance(item, int)]
        strings = [item for item in self.original_list if isinstance(item, str)]

        self.save_to_file('integers_list.json', integers)
        self.save_to_file('strings_list.json', strings)

        # 3. Replace odd numbers with 'reemplazo'
        replaced_list = ['reemplazo' if isinstance(item, int) and item % 2 != 0 else item for item in
                         self.original_list]
        self.save_to_file('replaced_list.json', replaced_list)

        # 4. Print half of the list
        half_index = len(self.original_list) // 2
        print(Fore.CYAN + "Half of the list:" + Style.RESET_ALL, self.original_list[:half_index])


# Example usage
my_list = [1, 1991, "taller", 200, 3, "programación", 700, "utp", "POO"]
processor = ListProcessor(my_list)
processor.process_list()
