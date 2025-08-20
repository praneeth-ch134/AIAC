
# Python script to collect user data and store it in a '.txt' file

# Prompt the user for their details
name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")
address = input("Enter your address: ")

# Prepare the data to be written to the file
user_data = (
    f"Name: {name}\n"
    f"Age: {age}\n"
    f"Email: {email}\n"
    f"Phone Number: {phone}\n"
    f"Address: {address}\n"
)

# Open a text file in write mode and save the user data
with open("user_data.txt", "w") as file:
    file.write(user_data)

# Inform the user that their data has been saved
print("Your data has been saved to 'user_data.txt'.")