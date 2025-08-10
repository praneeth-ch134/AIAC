def register_user(credentials):
    username = input("Enter a username to register: ").strip()
    if username in credentials:
        print("Username already exists. Please try a different username.")
        return
    password = input("Enter a password: ").strip()
    credentials[username] = password
    print("Registration successful!")

def login_user(credentials):
    username = input("Enter your username: ").strip()
    if username not in credentials:
        print("Username does not exist. Please register first.")
        return
    password = input("Enter your password: ").strip()
    if credentials[username] == password:
        print("Login successful! Welcome,", username)
    else:
        print("Incorrect password. Please try again.")

def main():
    credentials = {}
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == '1':
            register_user(credentials)
        elif choice == '2':
            login_user(credentials)
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

