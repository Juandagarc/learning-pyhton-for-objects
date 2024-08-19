# colorama is for the color of the text
# Example of using colorama: https://pypi.org/project/colorama/
from colorama import Fore, Style


def show_menu():
    print(Fore.YELLOW + 'choose an option:' + Style.RESET_ALL +
          '\n1. Add word.'
          '\n2. Show the longer and shorter word'
          '\n3. Exit')
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
            break
        else:
            print(Fore.RED + "Invalid choice!" + Style.RESET_ALL)


main()
