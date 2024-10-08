# colorama is for the color of the text
# Example of using colorama: https://pypi.org/project/colorama/
from colorama import Fore, Style


def show_menu():
    print(Fore.YELLOW + 'choose an option:' + Style.RESET_ALL +
          '\n1. Add word.'
          '\n2. Find word by length.'
          '\n3. Exit')
    return int(input())


def add_word(array, word):
    array.append(word)
    print(Fore.GREEN + 'Word added successfully!' + Style.RESET_ALL)


def get_string_by_length(array, length):
    if len(array) == 0:
        print(Fore.RED + 'your list is empty' + Style.RESET_ALL)
        return
    print('Of your list: ', end='')
    print(array)
    words = []
    for word in array:
        if len(word) == length:
            words.append(word)
    if len(words) == 0:
        print(Fore.RED + 'There is no words with length: ' + str(length) + Style.RESET_ALL)
        return
    else:
        print(Fore.YELLOW + 'the words with ' + str(length) + ' letters are:' + Style.RESET_ALL)
        print(*words, sep=',', end='.\n')


def main():
    main_array = []
    while True:
        choice = show_menu()
        if choice == 1:
            word = str(input('Enter your word: '))
            add_word(main_array, word)
        elif choice == 2:
            length = int(input('Enter your word length: '))
            get_string_by_length(main_array, length)
        elif choice == 3:
            break
        else:
            print(Fore.RED + "Invalid choice!" + Style.RESET_ALL)


main()
