class Employee:
    def __init__(self, name, department, salary, joining_year):
        self.name = name
        self.department = department
        self.salary = float(salary)
        self.joining_year = joining_year

    def display(self):
        print(f"Name: {self.name} | Department: {self.department} | "
              f"Salary: {self.salary} | Joining Year: {self.joining_year}")

    def to_csv(self):
        return f"{self.name},{self.department},{self.salary},{self.joining_year}\n"
