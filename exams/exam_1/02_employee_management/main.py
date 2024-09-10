from colorama import init, Fore, Style
import json

init(autoreset=True)

path = 'data.json'


def load_data():
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_data(data):
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)


class Employee:
    def __init__(self, name: str, base_salary: float, years_of_service: int, emp_id: int = None):
        self.name = name
        self.base_salary = base_salary
        self.years_of_service = years_of_service
        self.id = emp_id if emp_id is not None else self._get_next_id()

    def _get_next_id(self):
        employees = load_data().get("employees", [])
        if not employees:
            return 1
        else:
            max_id = max(emp["id"] for emp in employees)
            return max_id + 1

    def calculate_salary(self):
        bonus = 0
        if 0 <= self.years_of_service < 3:
            bonus = 0.05
        elif 3 <= self.years_of_service < 6:
            bonus = 0.1
        else:
            bonus = 0.15

        return self.base_salary + self.base_salary * bonus

    def show_employee(self):
        return (f"Employee {self.id}: {self.name} has a base salary of "
                f"{self.base_salary} and has worked for {self.years_of_service} years.")

    def save_data(self):
        data = load_data()

        if "employees" not in data:
            data["employees"] = []

        # Update existing employee or add a new one
        existing_data = {item["id"]: item for item in data["employees"]}
        existing_data[self.id] = {"id": self.id, "name": self.name,
                                  "base_salary": self.base_salary, "years_of_service": self.years_of_service}

        data["employees"] = list(existing_data.values())

        save_data(data)


class EmployeeManager:
    def __init__(self):
        self.employees = []
        self.load_employees()

    def load_employees(self):
        data = load_data()
        if "employees" in data:
            for emp in data["employees"]:
                self.employees.append(Employee(emp["name"], emp["base_salary"], emp["years_of_service"], emp["id"]))

    def add_employee(self, employee: Employee):
        self.employees.append(employee)
        employee.save_data()

    def show_employees(self, id: int):
        for emp in self.employees:
            if emp.id == id:
                return emp.show_employee()
        return "Employee not found"

    def delete_employee(self, id: int):
        data = load_data()
        if "employees" in data:
            data["employees"] = [emp for emp in data["employees"] if emp["id"] != id]
            save_data(data)
            self.employees = [emp for emp in self.employees if emp.id != id]  # Remove from local list
            return f"Employee with ID {id} removed."
        return "Employee not found"

    def update_employee(self, id: int):
        for emp in self.employees:
            if emp.id == id:
                emp.name = input("Enter new name: ")
                emp.base_salary = float(input("Enter new base salary: "))
                emp.years_of_service = int(input("Enter new years of service: "))
                emp.save_data()
                return f"Employee {emp.name} updated."
        return "Employee not found"


def main():
    manager = EmployeeManager()

    while True:
        print(Fore.CYAN + "Menu:" + Style.RESET_ALL)
        print(Fore.YELLOW + "1. Add employee" + Style.RESET_ALL)
        print(Fore.YELLOW + "2. Show employee" + Style.RESET_ALL)
        print(Fore.YELLOW + "3. Delete employee" + Style.RESET_ALL)
        print(Fore.YELLOW + "4. Update employee" + Style.RESET_ALL)
        print(Fore.YELLOW + "5. Show salary of an employee" + Style.RESET_ALL)
        print(Fore.RED + "0. Exit" + Style.RESET_ALL)

        choice = input("Choose an option: ")

        if choice == '0':
            print(Fore.BLUE + "Bye!" + Style.RESET_ALL)
            break

        if choice == '1':
            name = input("Enter employee name: ")
            base_salary = float(input("Enter base salary: "))
            years_of_service = int(input("Enter years of service: "))
            manager.add_employee(Employee(name, base_salary, years_of_service))

        elif choice == '2':
            id = int(input("Enter employee id: "))
            print(manager.show_employees(id))

        elif choice == '3':
            id = int(input("Enter employee id: "))
            print(manager.delete_employee(id))

        elif choice == '4':
            id = int(input("Enter employee id: "))
            print(manager.update_employee(id))

        elif choice == '5':
            print(Fore.CYAN + "View salary of an employee" + Style.RESET_ALL)
            id = int(input("Enter employee id: "))
            for emp in manager.employees:
                if emp.id == id:
                    print(f"Employee {emp.id}: {emp.name} has a salary of {emp.calculate_salary()}")
                    break
            else:
                print(Fore.RED + "Employee not found." + Style.RESET_ALL)

        else:
            print(Fore.RED + "Invalid option." + Style.RESET_ALL)


main()
