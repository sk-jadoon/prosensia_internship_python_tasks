# Take full name as input:
full_name = input("Enter the full name:  ")

# Find the space between first and last name:
space_index = full_name.find(" ")

# Slice the first name and last name using string slicing:
first_name = full_name[:space_index]
last_name = full_name[space_index + 1:]

# Display first and last names:
print("The first name is ",first_name)
print("The last name is ",last_name)

# Take two numeric inputs:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations:
add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2

try:
    divide = num1 / num2
except ZeroDivisionError:
    divide = "undefined (division by zero)"

# Display results:
print("Results")
print(f"{num1} + {num2} = {add}")
print(f"{num1} - {num2} = {subtract}")
print(f"{num1} * {num2} = {multiply}")
print(f"{num1} / {num2} = {divide}")
