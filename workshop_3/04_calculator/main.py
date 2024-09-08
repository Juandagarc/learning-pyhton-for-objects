# colorama is for the color of the text
# Example of using colorama: https://pypi.org/project/colorama/
from colorama import init, Fore, Style

# Math module is used to perform mathematical operations
import math

init(autoreset=True)


class ScientificCalculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        self.result = a - b
        return self.result

    def multiply(self, a, b):
        self.result = a * b
        return self.result

    def divide(self, a, b):
        if b == 0:
            print(Fore.RED + "Error: Division by zero is not allowed.")
            return None
        self.result = a / b
        return self.result

    def power(self, base, exponent):
        self.result = math.pow(base, exponent)
        return self.result

    def square_root(self, number):
        if number < 0:
            print(Fore.RED + "Error: Square root of a negative number is not allowed.")
            return None
        self.result = math.sqrt(number)
        return self.result

    def logarithm(self, number, base=10):
        if number <= 0:
            print(Fore.RED + "Error: Logarithm of a non-positive number is not defined.")
            return None
        self.result = math.log(number, base)
        return self.result

    def natural_log(self, number):
        if number <= 0:
            print(Fore.RED + "Error: Natural logarithm of a non-positive number is not defined.")
            return None
        self.result = math.log(number)
        return self.result

    def sine(self, angle):
        self.result = math.sin(math.radians(angle))
        return self.result

    def cosine(self, angle):
        self.result = math.cos(math.radians(angle))
        return self.result

    def tangent(self, angle):
        self.result = math.tan(math.radians(angle))
        return self.result

    def factorial(self, number):
        if number < 0:
            print(Fore.RED + "Error: Factorial of a negative number is not defined.")
            return None
        self.result = math.factorial(int(number))
        return self.result

    def degrees_to_radians(self, degrees):
        self.result = math.radians(degrees)
        return self.result

    def radians_to_degrees(self, radians):
        self.result = math.degrees(radians)
        return self.result

    def exponential(self, number):
        self.result = math.exp(number)
        return self.result

    def display_result(self):
        print(Fore.CYAN + f"Result: {self.result}" + Style.RESET_ALL)


def main():
    # example of using the ScientificCalculator class
    calculator = ScientificCalculator()
    print(Fore.GREEN + "Scientific Calculator" + Style.RESET_ALL)

    print(Fore.YELLOW + "Addition of: 5 + 10" + Style.RESET_ALL)
    calculator.add(5, 10)
    calculator.display_result()

    print(Fore.YELLOW + "Square root of: 16" + Style.RESET_ALL)
    calculator.square_root(16)
    calculator.display_result()

    print(Fore.YELLOW + "logarithm of: 100 (base 10)" + Style.RESET_ALL)
    calculator.logarithm(100)
    calculator.display_result()

    print(Fore.YELLOW + "sine of: 90" + Style.RESET_ALL)
    calculator.sine(90)
    calculator.display_result()


main()
