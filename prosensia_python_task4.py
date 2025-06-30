# Student Record System with Tuples & Sets:

#  Store student IDs using a tuple (immutable):
student_ids = (101, 102, 103, 104)
print("Student IDs (Tuple):", student_ids)

# Create a set of unique courses names:
courses = {"Python", "AI", "ML"}
print("Initial Courses (Set):", courses)

# Function to add a new course:
def add_course(course_name):
    # Adds a course to the set:
    courses.add(course_name)
    print(f"Course '{course_name}' added.")
    print("Updated Courses:", courses)

# Function to remove an existing course:
def remove_course(course_name):
    # Removes course if it exists in the set
    if course_name in courses:
        courses.remove(course_name)
        print(f"Course '{course_name}' removed.")
    else:
        print(f"Course '{course_name}' not found.")
    print("Updated Courses:", courses)

# Function to display all courses:
def display_courses():
    print("Current Courses:", courses)

# Add new courses:
add_course("Data Science")
add_course("DataBase Management System")

# Remove a course:
remove_course("ML")
remove_course("AI")

# Display final course list:
display_courses()
