# Function to manually sort a list:

def manual_sort(numbers):
    for i in range(len(numbers)):
        for j in range(0, len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


# Function to calculate sum, average, min, and max
def analyze_list(numbers):
    total = 0
    minimum = numbers[0]
    maximum = numbers[0]

    for num in numbers:
        total += num
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    average = total / len(numbers)

    return {
        'Sorted List': manual_sort(numbers[:]),
        'Sum': total,
        'Average': average,
        'Minimum': minimum,
        'Maximum': maximum
    }


# Function to print results using enumerate:
def print_results(results):
    print("\n📈 List Analysis Summary:")
    for index, (key, value) in enumerate(results.items(), start=1):
        print(f"{index}. {key}: {value}")


# --- Main Program ---
try:
    # Accept user input
    user_input = input("Enter a list of numbers separated by spaces: ")
    number_list = [float(x) for x in user_input.strip().split()]

    # Analyze and print results
    stats = analyze_list(number_list)
    print_results(stats)

except ValueError:
    print("Invalid number! ")
