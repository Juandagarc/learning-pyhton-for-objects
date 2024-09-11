def multiple_numbers(number_1, number_4):
    if number_1 % number_4 == 0:
        print(f"{number_1} is multiple of {number_4}")
    else:
        print(f"{number_1} is not multiple of {number_4}")


def addition_numbers(number_2, number_3):
    addition = number_2 + number_3
    print(f"The addition of {number_2} and {number_3} is {addition}")


def main():
    while True:
        number = int(input("Enter a number with 4 digits: "))
        if number < 1000 or number > 9999:
            print("The number must have 4 digits")
        else:
            break
    number_1 = number // 1000
    number_2 = number // 100 % 10
    number_3 = number // 10 % 10
    number_4 = number % 10
    print('multiple_numbers(number 1, number 4):')
    multiple_numbers(number_1, number_4)
    print('addition_numbers(number 2, number 3):')
    addition_numbers(number_2, number_3)


main()
