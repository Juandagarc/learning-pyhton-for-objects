# colorama is for the color of the text
# Example of using colorama: https://pypi.org/project/colorama/
from colorama import Fore, Style

# this mention an array of 10 strings, not need to be inserted by user.
words = ['apple', 'banana', 'cherry', 'date', 'eggplant', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon']


def get_size_of_strings(array):
    string_size = 0
    for element in array:
        string_size += len(element)
    return str(string_size)


def get_letters_without_vocals():
    words_without_vocals = []
    vocals = ['a', 'e', 'i', 'o', 'u']
    for word in words:
        for vocal in vocals:
            word = word.replace(vocal, '')
        words_without_vocals.append(word)
    print(Fore.YELLOW + 'Words with vocals:' + Style.RESET_ALL)
    print(*words, sep=',', end='.\n')
    print(Fore.MAGENTA + 'Length:' + Style.RESET_ALL + get_size_of_strings(words))
    print(Fore.YELLOW + 'Words without vocals:' + Style.RESET_ALL)
    print(*words_without_vocals, sep=',', end='.\n')
    print(Fore.MAGENTA + 'Length:' + Style.RESET_ALL + get_size_of_strings(words_without_vocals))


get_letters_without_vocals()
