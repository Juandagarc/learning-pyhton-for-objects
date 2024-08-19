# subjects = ['Math', 'Science', 'English', 'Filipino', 'PE']
# grades = [90, 85, 95, 88, 92]

# that's also great but it could be better to declare the grades of the subjects in a dictionary
# so that you can easily access the grades of the subjects by their name

subjects = {
    'Math': 90,
    'Science': 85,
    'English': 95,
    'Filipino': 88,
    'PE': 92
}


class Person:
    def __init__(self, name, age, subjects_grades):
        self.name = name
        self.age = age
        self.subjects_grades = subjects_grades

    def get_grades(self):
        return self.subjects_grades


# Now we create a class Student that inherits from the class Person

Person1 = Person('John', 15, subjects)

print(Person1.get_grades())

list_of_subjects = [1, 23, 4]
list_of_subjects.reverse()
print(1 in list_of_subjects)
