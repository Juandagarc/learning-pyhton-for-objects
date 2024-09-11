def save_to_file(text, file_name):
    try:
        with open(file_name, "w") as file:
            file.write(text)
        print(f"Text saved to {file_name}")
    except FileNotFoundError:
        with open(file_name, "a") as file:
            file.write(text)


class CaesarCipher:
    def __init__(self, key, message, abc, ABC):
        self.key = key
        self.message = message
        self.abc = abc
        self.ABC = ABC

    def encrypt(self):
        encrypted_message = ""
        for letter in self.message:
            if letter in self.abc:
                encrypted_message += self.abc[(self.abc.index(letter) - self.key) % len(self.abc)]
            elif letter in self.ABC:
                encrypted_message += self.ABC[(self.ABC.index(letter) - self.key) % len(self.ABC)]
            else:
                encrypted_message += letter
        return encrypted_message

    def decrypt(self):
        decrypted_message = ""
        for letter in self.message:
            if letter in self.abc:
                decrypted_message += self.abc[(self.abc.index(letter) + self.key) % len(self.abc)]
            elif letter in self.ABC:
                decrypted_message += self.ABC[(self.ABC.index(letter) + self.key) % len(self.ABC)]
            else:
                decrypted_message += letter
        return decrypted_message


def main():
    abc = "abcdefghijklmnopqrstuvwxyz"
    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while True:
        key = int(input("Enter the key: "))
        if type(key) != int:
            print("Invalid key")
        else:
            if key > 26:
                key = key % 26
                break
            elif key < 0:
                key = key % 26
                break
            else:
                break
    message = input("Enter the message: ")
    cipher = CaesarCipher(key, message, abc, ABC)
    while True:
        option = input("Encrypt or decrypt (E/D): ")
        if option.upper() == "E":
            text = cipher.encrypt()
            print(f"Encrypted message: {text}")
            save_to_file(text, "encrypted.txt")
            break
        elif option.upper() == "D":
            text = cipher.decrypt()
            print(f"Decrypted message: {text}")
            save_to_file(text, "decrypted.txt")
            break
        else:
            print("Invalid option")


main()
