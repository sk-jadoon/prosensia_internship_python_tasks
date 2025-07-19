from employee import Employee
from utils import clear_screen

class EmployeeManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.employees = []
        self.load_employees()

    def load_employees(self):
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    name, dept, salary, year = line.strip().split(",")
                    self.employees.append(Employee(name, dept, salary, year))
        except FileNotFoundError:
            open(self.file_path, "w").close()

    def save_employees(self):
        with open(self.file_path, "w") as file:
            for emp in self.employees:
                file.write(emp.to_csv())

    def add_employee(self):
        try:
            name = input("Enter Name: ")
            dept = input("Enter Department: ")
            salary = float(input("Enter Salary: "))
            year = input("Enter Joining Year: ")
            emp = Employee(name, dept, salary, year)
            self.employees.append(emp)
            print("Employee Added Successfully!")
        except:
            print("Invalid input! Please try again.")

    def list_employees(self):
        clear_screen()
        print("\nAll Employees:\n")
        for emp in self.employees:
            emp.display()

    def search_employee(self, term):
        clear_screen()
        print(f"\nSearch Results for '{term}':\n")
        results = filter(lambda e: term.lower() in e.name.lower() or term.lower() in e.department.lower(), self.employees)
        found = False
        for emp in results:
            emp.display()
            found = True
        if not found:
            print("No matching employee found.")

    def sort_by_salary(self, desc=False):
        clear_screen()
        print("\nEmployees Sorted by Salary:\n")
        sorted_list = sorted(self.employees, key=lambda e: e.salary, reverse=desc)
        for emp in sorted_list:
            emp.display()

    def generate_report(self):
        total = len(self.employees)
        total_salary = sum(emp.salary for emp in self.employees)
        avg_salary = total_salary / total if total > 0 else 0

        with open("employee_report.txt", "w") as file:
            file.write("Employee Summary Report\n")
            file.write("=======================\n")
            file.write(f"Total Employees: {total}\n")
            file.write(f"Total Salary: {total_salary}\n")
            file.write(f"Average Salary: {avg_salary:.2f}\n")

        print("Report Generated: employee_report.txt")
