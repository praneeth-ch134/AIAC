def format_full_name():
    full_name = input("Enter the Full Name : ").strip()
    parts = full_name.split()
    if len(parts) >= 2:
        first_name = parts[0]
        last_name = parts[-1]
        print(f"First Name : {first_name}")
        print(f"Last Name : {last_name}")
    else:
        print("Please enter both first and last names.")

# Example usage:
if __name__ == "__main__":
    format_full_name()