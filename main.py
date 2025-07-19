from manager import EmployeeManager

def main():
    manager = EmployeeManager("employee_data.txt")

    while True:
        print("\n==== Employee Management System ====")
        print("1. Add Employee")
        print("2. List Employees")
        print("3. Search Employee")
        print("4. Sort Employees by Salary")
        print("5. Generate Report")
        print("6. Exit")

        choice = input("\nEnter choice (1-6): ")

        if choice == '1':
            manager.add_employee()
        elif choice == '2':
            manager.list_employees()
        elif choice == '3':
            term = input("Enter name or department to search: ")
            manager.search_employee(term)
        elif choice == '4':
            desc = input("Sort Descending? (yes/no): ").lower() == 'yes'
            manager.sort_by_salary(desc)
        elif choice == '5':
            manager.generate_report()
        elif choice == '6':
            manager.save_employees()
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
