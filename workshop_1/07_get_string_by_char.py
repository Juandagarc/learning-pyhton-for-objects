# colorama is for the color of the text
# Example of using colorama: https://pypi.org/project/colorama/
from colorama import Fore, Style


def show_menu():
    print(Fore.YELLOW + 'choose an option:' + Style.RESET_ALL +
          '\n1. Add word.'
          '\n2. Find word by char.'
          '\n3. Exit')
    return int(input())


def add_word(array, word):
    array.append(word)
    print(Fore.GREEN + 'Word added successfully!' + Style.RESET_ALL)


def get_string_by_char(array, char):
    if len(array) == 0:
        print(Fore.RED + 'your list is empty' + Style.RESET_ALL)
        return
    print('Of your list: ', end='')
    print(array)
    words = []
    even_or_odd = ''
    for word in array:
        if char in word:
            if len(word) % 2 == 0:
                even_or_odd = 'even'
            else:
                even_or_odd = 'odd'
            words.append(word + '(' + even_or_odd + ')')
    if len(words) == 0:
        print(Fore.RED + 'There is no words with char: ' + str(char) + Style.RESET_ALL)
        return
    else:
        print(Fore.YELLOW + 'the words with ' + str(char) + ' are:' + Style.RESET_ALL)
        print(*words, sep=',', end='.\n')


def main():
    main_array = []
    while True:
        choice = show_menu()
        if choice == 1:
            word = str(input('Enter your word: '))
            add_word(main_array, word)
        elif choice == 2:
            char = input('Enter your char: ')
            get_string_by_char(main_array, char)
        elif choice == 3:
            break
        else:
            print(Fore.RED + "Invalid choice!" + Style.RESET_ALL)


main()
