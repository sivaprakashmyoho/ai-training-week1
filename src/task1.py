def bonus(salary, rate=0.1, *extras, **options):
    total_bonus = salary * rate + sum(extras)

    if "cap" in options:
        total_bonus = min(total_bonus, options["cap"])

    return total_bonus


print("Bonus:", bonus(50000, 0.1, 1000, 2000, cap=7000))

class InvalidSalaryError(Exception):
    pass


class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")

        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return (
            f"Manager: {self.name}, "
            f"Salary: {self.salary}, "
            f"Team Size: {self.team_size}"
        )

emp = Employee("Rahul", 60000)

print(emp.get_details())
print("Annual Salary:", emp.annual_salary())

manager = Manager("Arun", 90000, 5)

print(manager.get_details())

try:
    emp = Employee("Test", -500)

except InvalidSalaryError as e:
    print("Error:", e)

finally:
    print("Transaction finished")

employees = [
    {"id": 1, "name": "Arun", "department": "Sales", "salary": 30000, "city": "Chennai"},
    {"id": 2, "name": "Priya", "department": "HR", "salary": 45000, "city": "Chennai"},
    {"id": 3, "name": "Rahul", "department": "IT", "salary": 60000, "city": "Bangalore"},
    {"id": 4, "name": "Divya", "department": "IT", "salary": 75000, "city": "Chennai"},
    {"id": 5, "name": "Karthik", "department": "Finance", "salary": 90000, "city": "Mumbai"},
    {"id": 6, "name": "Meena", "department": "Sales", "salary": 52000, "city": "Bangalore"},
    {"id": 7, "name": "Suresh", "department": "IT", "salary": 68000, "city": "Chennai"},
    {"id": 8, "name": "Anitha", "department": "HR", "salary": 48000, "city": "Mumbai"}
]

above_50000 = [
    emp["name"]
    for emp in employees
    if emp["salary"] > 50000
]

print("Above 50000:", above_50000)

raised_salaries = list(
    map(lambda emp: emp["salary"] * 1.10, employees)
)

print("Raised Salaries:", raised_salaries)

chennai_employees = list(
    filter(lambda emp: emp["city"] == "Chennai", employees)
)

chennai_names = [emp["name"] for emp in chennai_employees]

print("Chennai:", chennai_names)

salaries = [30000, 0, 45000, 60000, 90000, 75000]

for salary in salaries:

    if salary == 0:
        continue

    if salary > 85000:
        break

    print(salary)

    raised_salaries = list(
    map(lambda emp: round(emp["salary"] * 1.10, 2), employees)
)