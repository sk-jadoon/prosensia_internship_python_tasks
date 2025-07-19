import os

# Employee Class
class Employee:
    def __init__(self, name, department, salary, joining_year):
        self.name = name
        self.department = department
        self.salary = float(salary)
        self.joining_year = joining_year

    def display(self):
        print(f"Name: {self.name}, Department: {self.department}, "
              f"Salary: {self.salary}, Joining Year: {self.joining_year}")

    def to_csv(self):
        return f"{self.name},{self.department},{self.salary},{self.joining_year}\n"

# Employee Manager Class
class EmployeeManager:
    def __init__(self, filename):
        self.filename = filename
        self.employees = []
        self.load_from_file()

    def load_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    name, dept, salary, year = line.strip().split(',')
                    self.employees.append(Employee(name, dept, salary, year))
        except FileNotFoundError:
            open(self.filename, 'w').close()

    def save_to_file(self):
        with open(self.filename, 'w') as file:
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
            print("Employee Added!\n")
        except:
            print("Invalid Input!")

    def list_employees(self):
        for emp in self.employees:
            emp.display()

    def search_employee(self):
        term = input("Enter Name or Department to Search: ")
        found = False
        for emp in filter(lambda e: term.lower() in e.name.lower() or term.lower() in e.department.lower(), self.employees):
            emp.display()
            found = True
        if not found:
            print("No Employee Found.")

    def sort_by_salary(self):
        desc = input("Sort Descending? (yes/no): ").lower() == 'yes'
        sorted_emps = sorted(self.employees, key=lambda e: e.salary, reverse=desc)
        for emp in sorted_emps:
            emp.display()

    def generate_report(self):
        total = len(self.employees)
        total_salary = sum(emp.salary for emp in self.employees)
        avg_salary = total_salary / total if total > 0 else 0

        with open('employee_report.txt', 'w') as report:
            report.write("Employee Report\n")
            report.write("==================\n")
            report.write(f"Total Employees: {total}\n")
            report.write(f"Total Salary: {total_salary}\n")
            report.write(f"Average Salary: {avg_salary:.2f}\n")

        print("Report Generated in employee_report.txt\n")

# Main Menu
def main():
    manager = EmployeeManager('employee_data.txt')

    while True:
        print("\n1. Add Employee")
        print("2. List Employees")
        print("3. Search Employee")
        print("4. Sort by Salary")
        print("5. Generate Report")
        print("6. Exit\n")

        choice = input("Enter Choice: ")

        if choice == '1':
            manager.add_employee()
        elif choice == '2':
            manager.list_employees()
        elif choice == '3':
            manager.search_employee()
        elif choice == '4':
            manager.sort_by_salary()
        elif choice == '5':
            manager.generate_report()
        elif choice == '6':
            manager.save_to_file()
            print("Data Saved. Exiting.")
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()
