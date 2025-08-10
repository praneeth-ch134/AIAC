# def factorial(n):
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers.")
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result

# def main():
#     try:
#         num = int(input("Enter a number to compute its factorial: "))
#         print(f"Factorial of {num} is {factorial(num)}")
#     except ValueError as e:
#         print(f"Invalid input: {e}")

# if __name__ == "__main__":
#     main()

# def factorial(n):
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers.")
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result

# def main():
#     try:
#         num = int(input("Enter a number to compute its factorial: "))
#         print(f"Factorial of {num} is {factorial(num)}")
#     except ValueError as e:
#         print(f"Invalid input: {e}")

# if __name__ == "__main__":
#     main()

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    try:
        num = int(input("Enter a number to compute its factorial: "))
        print(f"Factorial of {num} is {factorial(num)}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
