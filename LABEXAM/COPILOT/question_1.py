# Program to calculate sum of even and odd numbers from user input

# Take input from user and convert to list of integers
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

even_sum = 0
odd_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)