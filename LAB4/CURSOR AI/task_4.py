def count_vowels_in_string():
    input_str = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = sum(1 for char in input_str if char in vowels)
    print(f"Total number of vowels: {count}")
    return count
count_vowels_in_string()