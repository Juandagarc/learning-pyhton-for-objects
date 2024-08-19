# colorama is for the color of the text
# Example of using colorama: https://pypi.org/project/colorama/
from colorama import Fore, Style

subjects = []
grades = []
averages = []
total_average = 0


def show_menu():
    print("1. Add subject")
    print("2. Show subjects")
    print("3. Exit")
    return int(input(Fore.MAGENTA + "Enter choice: " + Style.RESET_ALL))


def add_subject():
    subject = input("Enter subject: ")
    subject_grade = []
    for i in range(4):
        grade = float(input("Enter grade NO." + str(i + 1) + ": "))
        subject_grade.append(grade)
    print("Saving subject...")
    averages.append((sum(subject_grade) / 20) * 5)
    subjects.append(subject)
    grades.append(subject_grade)
    print(Fore.GREEN + "Subject saved!" + Style.RESET_ALL)


def show_subjects():
    if len(subjects) == 0:
        print(Fore.YELLOW + "No subjects saved!" + Style.RESET_ALL)
        return
    print("Subjects:")
    print(Fore.MAGENTA + f"{'Subject:':<15} {'Grades:':<25} {'Average:':<15}" + Fore.RESET)
    for subject in subjects:
        print(f"{subject:<15} {str(grades[subjects.index(subject)]):<25} {str(averages[subjects.index(subject)]):<15}",
              end="")
        if averages[subjects.index(subject)] >= 3:
            print(Fore.GREEN + " Approved" + Style.RESET_ALL)
        else:
            print(Fore.RED + " Failed" + Style.RESET_ALL)
    print(Fore.YELLOW + 'Total average: ' + Style.RESET_ALL + str(sum(averages) / len(averages)))
    if sum(averages) / len(averages) >= 3:
        print(Fore.GREEN + "You approved the semester" + Style.RESET_ALL)
    else:
        print(Fore.RED + "You failed the semester" + Style.RESET_ALL)


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
