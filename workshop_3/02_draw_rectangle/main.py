# colorama is for the color of the text
# Example of using colorama: https://pypi.org/project/colorama/
from colorama import Fore, Style


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw_rectangle(self):
        for i in range(self.height):
            for j in range(self.width):
                if i == 0 or i == self.height - 1:
                    print(Fore.YELLOW + '*' + Style.RESET_ALL, end='')
                else:
                    if j == 0 or j == self.width - 1:
                        print(Fore.YELLOW + '*' + Style.RESET_ALL, end='')
                    else:
                        print(' ', end='')
            print()


def main():
    print(Fore.CYAN + 'Draw a rectangle' + Style.RESET_ALL)
    width = int(input('Insert the width of the rectangle: '))
    height = int(input('Insert the height of the rectangle: '))
    rectangle = Rectangle(width, height)
    rectangle.draw_rectangle()


main()
