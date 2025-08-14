# Program to remove duplicates from a list of integers, sort them, and display the result

# Take input from user
user_input = input("Enter a list of integers separated by spaces: ")

# Convert input string to list of integers
numbers = list(map(int, user_input.split()))

# Remove duplicates using set, then sort
unique_sorted_numbers = sorted(set(numbers))

# Display the result
print("Sorted list without duplicates:", unique_sorted_numbers)