import getpass
import hashlib


def hash_password(password):
    """Hash the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def anonymize_email(email):
    """Anonymize email by masking part of it."""
    parts = email.split('@')
    if len(parts) == 2:
        masked = parts[0][:2] + "***@" + parts[1]
        return masked
    return "***@***"

def anonymize_phone(phone):
    """Anonymize phone by masking all but last 2 digits."""
    if len(phone) > 2:
        return "*" * (len(phone)-2) + phone[-2:]
    return "**"

def collect_user_data():
    """Collect user data from input."""
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")
    return {
        "name": name,
        "age": age,
        "email": anonymize_email(email),
        "phone": anonymize_phone(phone),
        "address": address
    }

def save_data(filename, data, password_hash):
    """Save anonymized data and password hash to a file."""
    with open(filename, 'w') as f:
        f.write("# User Data (Anonymized)\n")
        for key, value in data.items():
            f.write(f"{key}: {value}\n")
        f.write("# Password hash for protection\n")
        f.write(f"password_hash: {password_hash}\n")

def main():
    print("Welcome to User Data Collector")
    # Prompt user to create a password for file protection
    password = getpass.getpass("Create a password to protect your data file: ")
    password_hash = hash_password(password)
    # Collect user data
    user_data = collect_user_data()
    # Save data to file
    filename = "user_data.txt"
    save_data(filename, user_data, password_hash)
    print(f"Your anonymized data has been saved to '{filename}' and protected with your password.")

if __name__ == "__main__":
    main()