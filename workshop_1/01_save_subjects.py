# colorama is for the color of the text
# Example of using colorama: https://pypi.org/project/colorama/
from colorama import Fore, Style

subjects = []


def show_menu():
    print("1. Add subject")
    print("2. Show subjects")
    print("3. Exit")
    return int(input(Fore.MAGENTA + "Enter choice: " + Style.RESET_ALL))


def add_subject():
    subject = input("Enter subject: ")
    print("Saving subject...")
    subjects.append(subject)
    print(Fore.GREEN + "Subject saved!" + Style.RESET_ALL)


def show_subjects():
    if len(subjects) == 0:
        print(Fore.YELLOW + "No subjects saved!" + Style.RESET_ALL)
        return
    print("Subjects:")
    for subject in subjects:
        print(subject)


def main():
    while True:
        choice = show_menu()
        if choice == 1:
            add_subject()
        elif choice == 2:
            show_subjects()
        elif choice == 3:
            break
        else:
            print(Fore.RED + "Invalid choice!" + Style.RESET_ALL)


main()
