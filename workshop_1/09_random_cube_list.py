# colorama is for the color of the text
# Example of using colorama: https://pypi.org/project/colorama/
from colorama import Fore, Style
import random


def generate_random_list():
    random_list = []
    for element in range(0, 15):
        random_list.append(random.randrange(1, 15))

    return random_list


def generate_cube_list(array):
    cube_list = []
    for element in array:
        cube_list.append(Fore.MAGENTA + str(element) + Style.RESET_ALL)
        cube_list.append(str(pow(element, 2)))
        cube_list.append(str(pow(element, 3)) + '\n')

    return cube_list


def show_random_list():
    random_list = generate_random_list()
    print(Fore.YELLOW + 'Of the random list: ' + Style.RESET_ALL, end='')
    print(*random_list)
    print(Fore.YELLOW + 'The cube list is:\n ' + Style.RESET_ALL, end='')
    print(*generate_cube_list(random_list))


show_random_list()
