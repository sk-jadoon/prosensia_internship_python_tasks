def read_student_data(file_path):
    student_marks = {}
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue

                try:
                    name, mark = line.split(',')
                    name = name.strip()
                    mark = mark.strip()

                    if not name or not mark:
                        raise ValueError(f"Missing value on line {line_number}: '{line}'")

                    mark = int(mark)

                    student_marks[name] = mark

                except ValueError as e:
                    print(f"[Line {line_number}] Skipping invalid entry: {e}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return student_marks


def print_student_summary(student_marks):
    try:
        if not student_marks:
            raise ZeroDivisionError("No student data available.")

        print("\nStudent Marks:")
        total = 0
        for name, mark in student_marks.items():
            print(f"{name}: {mark}")
            total += mark

        average = total / len(student_marks)
        print(f"\nAverage Mark: {average:.2f}")

    except ZeroDivisionError as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    file_path = "students.txt"
    student_data = read_student_data(file_path)
    print_student_summary(student_data)
