# Function to convert numeric score into letter grade:

def convert_to_grade(score):
    if score > 100 or score < 0:
        return "Invalid score. Must be between 0 and 100."
    elif score >= 90:
        return "A"
    elif score >= 85:
        return "A-"
    elif score >= 80:
        return "B+"
    elif score >= 75:
        return "B"
    elif score >= 70:
        return "B-"
    elif score >= 65:
        return "C+"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

# Function to print grade summary using named parameters
def print_grade_summary(name, score):
    grade = convert_to_grade(score)
    if grade.startswith("Invalid"):
        print(grade)
    else:
        print(f"Student {name} scored {score} → Grade: {grade}")

# Example: Demonstrate result
print_grade_summary(name="Zara", score=87.5)
