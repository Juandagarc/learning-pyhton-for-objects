import json


class Generator:
    def __init__(self, data, path):
        self.__data = data
        self.__path = path

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def set_path(self, path):
        self.__path = path

    def get_path(self):
        return self.__path

    def generate_json(self):
        try:
            # Read existing data into the file if there is already data
            try:
                with open(self.get_path(), 'r') as file_json:
                    existing_data = json.load(file_json)
            except (json.JSONDecodeError, FileNotFoundError):
                existing_data = []  # If the file is empty or does not exist, we start with an empty list

            # Add the new book to the list of existing data
            existing_data.append(self.get_data())

            # Write the entire list back to file
            with open(self.get_path(), 'w') as file_json:
                json.dump(existing_data, file_json, indent=4)

            print("Archivo generado con exito.")
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")
