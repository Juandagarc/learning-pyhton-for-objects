# colorama is for the color of the text
# Example of using colorama: https://pypi.org/project/colorama/
from colorama import init, Fore, Style

# Datetime module is used to calculate the age of the employee
from datetime import datetime

# Json module is used to load data from file
import json

# Initialize colorama
init(autoreset=True)

employee_file = 'employees.json'


def load_data():
    try:
        with open(employee_file, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


class Employee:
    def __init__(self, name, gender, birth_date, hire_date, hourly_rate, hours_worked):
        self.id = len(load_data().get("Employees", []))
        self.name = name
        self.gender = gender.lower()
        self.birth_date = birth_date
        self.hire_date = hire_date
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_monthly_salary(self):
        return self.hours_worked * self.hourly_rate

    def calculate_seniority(self):
        hire_date = datetime.strptime(self.hire_date, "%Y-%m-%d")
        difference = datetime.now() - hire_date
        return difference.days // 365

    def calculate_years_until_retirement(self):
        current_age = self.calculate_age()
        retirement_age = 60 if self.gender == 'female' else 65
        return max(0, retirement_age - current_age)

    def calculate_monthly_contributions(self):
        salary = self.calculate_monthly_salary()
        health_contribution = salary * 0.04
        pension_contribution = salary * 0.04
        return health_contribution, pension_contribution

    def calculate_annual_pension_contribution(self):
        _, monthly_pension = self.calculate_monthly_contributions()
        return monthly_pension * 12

    def calculate_age(self):
        birth_date = datetime.strptime(self.birth_date, "%Y-%m-%d")
        difference = datetime.now() - birth_date
        return difference.days // 365

    def save_data(self):
        data = load_data()
        if "Employees" not in data:
            data["Employees"] = []

        data["Employees"].append({
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "birth_date": self.birth_date,
            "hire_date": self.hire_date,
            "hourly_rate": self.hourly_rate,
            "hours_worked": self.hours_worked,
            "monthly_salary": self.calculate_monthly_salary(),
            "seniority": self.calculate_seniority(),
            "years_until_retirement": self.calculate_years_until_retirement(),
            "monthly_health_contributions": self.calculate_monthly_contributions()[0],
            "monthly_pension_contributions": self.calculate_monthly_contributions()[1],
            "annual_pension_contributions": self.calculate_annual_pension_contribution()
        })

        with open(employee_file, 'w') as file:
            json.dump(data, file, indent=4)

    def display_info(self):
        print(Fore.CYAN + f"Employee: {self.name}")
        print(Fore.GREEN + f"Monthly Salary: ${self.calculate_monthly_salary():.2f}")
        print(Fore.YELLOW + f"Years of Service: {self.calculate_seniority()} years")
        print(Fore.MAGENTA + f"Years Until Retirement: {self.calculate_years_until_retirement()} years")
        health, pension = self.calculate_monthly_contributions()
        print(Fore.BLUE + f"Monthly Contributions - Health: ${health:.2f}, Pension: ${pension:.2f}")
        print(Fore.RED + f"Annual Pension Contributions: ${self.calculate_annual_pension_contribution():.2f}")


def main():
    employee = Employee(
        name="Ana Lopez",
        gender="female",
        birth_date="1980-05-15",
        hire_date="2010-06-01",
        hourly_rate=20,
        hours_worked=160
    )
    employee.save_data()
    employee.display_info()


main()
