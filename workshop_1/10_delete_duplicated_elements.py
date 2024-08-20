# colorama is for the color of the text
# Example of using colorama: https://pypi.org/project/colorama/
from colorama import Style, Fore

Lista = ["casa", "programación", "utp", "universidad", "utp", "casa", "casa", "thj", "vbh", "456", "987"]


def delete_duplicated_elements(array):
    return list(dict.fromkeys(array))


def delete_elements_without_vocals(array):
    vocals = ['a', 'e', 'i', 'o', 'u']
    return [element for element in array if any(vocal in element for vocal in vocals)]


def order_list(array):
    return sorted(array)


def main():
    duplicated_elements = delete_duplicated_elements(Lista)
    elements_without_vocals = delete_elements_without_vocals(duplicated_elements)
    order_list(elements_without_vocals)

    print(Fore.YELLOW + "Original list: " + Style.RESET_ALL, Lista)
    print(Fore.MAGENTA + "Step 1" + Style.RESET_ALL)
    print(Fore.YELLOW + "List without duplicates: " + Style.RESET_ALL, duplicated_elements)
    print(Fore.MAGENTA + "Step 2" + Style.RESET_ALL)
    print(Fore.YELLOW + "List without vocals: " + Style.RESET_ALL, elements_without_vocals)
    print(Fore.MAGENTA + "Step 3" + Style.RESET_ALL)
    print(Fore.YELLOW + "List ordered: " + Style.RESET_ALL, order_list(elements_without_vocals))


main()