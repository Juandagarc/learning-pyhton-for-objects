import json


def show_data(data):
    for i in data:
        print(f"\n\tBook {data.index(i) + 1}")
        for key in i:
            print(f"\t\t{key}: {i[key]}")
        print("\n")


class Read:
    def __init__(self, path):
        self.__path = path

    def set_path(self, path):
        self.__path = path

    def get_path(self):
        return self.__path

    def read_json(self):
        try:
            with open(self.get_path(), 'r') as file_json:
                data = json.load(file_json)
            return data
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")
            return None
