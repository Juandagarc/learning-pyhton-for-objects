import os
import subprocess
from colorama import Fore, Style, init

# Initialize colorama
init()


def run_script(script_path):
    try:
        subprocess.run(['python', script_path], check=True)
        print(Fore.GREEN + "Script executed successfully!" + Style.RESET_ALL)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error running {script_path}: {e}" + Style.RESET_ALL)


def display_menu():
    print(Fore.CYAN + "Menu of the workshop:" + Style.RESET_ALL)
    print(Fore.YELLOW + "1. 01_design_classes" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. 02_draw_rectangle" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. 03_employ_class" + Style.RESET_ALL)
    print(Fore.YELLOW + "4. 04_calculator" + Style.RESET_ALL)
    print(Fore.YELLOW + "5. 05_save_list" + Style.RESET_ALL)
    print(Fore.YELLOW + "6. 06_files_methods" + Style.RESET_ALL)
    print(Fore.RED + "0. exit" + Style.RESET_ALL)


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    while True:
        display_menu()
        choice = input(Fore.GREEN + "Choose an option (0-6): " + Style.RESET_ALL)

        if choice == '0':
            print(Fore.BLUE + "Bye!" + Style.RESET_ALL)
            break

        script_paths = {
            '1': '../01_design_classes/main.py',
            '2': '../02_draw_rectangle/main.py',
            '3': '../03_employ_class/main.py',
            '4': '../04_calculator/main.py',
            '5': '../05_save_list/main.py',
            '6': '../06_files_methods/main.py',
        }

        if choice in script_paths:
            script_path = os.path.join(base_dir, script_paths[choice])
            run_script(script_path)
        else:
            print(Fore.RED + "Invalid option." + Style.RESET_ALL)


if __name__ == "__main__":
    main()
