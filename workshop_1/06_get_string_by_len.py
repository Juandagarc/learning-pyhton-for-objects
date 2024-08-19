# colorama is for the color of the text
# Example of using colorama: https://pypi.org/project/colorama/
from colorama import Fore, Style


def show_menu():
    print(Fore.YELLOW + 'choose an option:' + Style.RESET_ALL +
          '\n1. Add word.'
          '\n2. Show the longer and shorter word'
          '\n3. Find word by length.'
          '\n4. Exit')
    return int(input())


def add_word(array, word):
    array.append(word)
    print(Fore.GREEN + 'Word added successfully!' + Style.RESET_ALL)


def show_shorter_larger_word(array):
    if len(array) == 0:
        print(Fore.RED + 'your list is empty' + Style.RESET_ALL)
        return
    else:
        print('Of your list: ', end='')
        print(array)
        shorter_word = array[0]
        larger_word = array[0]
        for word in array:
            if len(word) < len(shorter_word):
                shorter_word = word
            if len(word) > len(larger_word):
                larger_word = word
        print(Fore.YELLOW +
              'The shorter word is: ' + shorter_word +
              '\nThe larger word is: ' + larger_word
              + Style.RESET_ALL)


def get_string_by_length(array, length):
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
            show_shorter_larger_word(main_array)
        elif choice == 3:
            length = int(input('Enter your word length: '))
            get_string_by_length(main_array, length)
        elif choice == 4:
            break
        else:
            print(Fore.RED + "Invalid choice!" + Style.RESET_ALL)


main()
