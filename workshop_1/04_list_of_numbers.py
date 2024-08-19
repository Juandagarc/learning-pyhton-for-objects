# colorama is for the color of the text
# Example of using colorama: https://pypi.org/project/colorama/
from colorama import Fore, Style


def generate_list():
    array = []
    length = int(input('Enter the list length: '))
    for element in range(length):
        array.append(int(input(Fore.MAGENTA + ' Enter your list No. ' + str(element + 1)
                               + ' for the list: ' + Style.RESET_ALL)))
    return array


def generate_array_of_cubes(element):
    array = []
    for exponent in range(1, 4):
        array.append(pow(element, exponent))
    return array


def print_lists(array):
    print(Fore.YELLOW + 'Output:' + Style.RESET_ALL)
    for element in range(len(array)):
        print(*generate_array_of_cubes(array[element]), sep='-')


def main():
    main_array = generate_list()
    print_lists(main_array)


main()
