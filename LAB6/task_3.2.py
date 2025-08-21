
# Alternative using match-case (Python 3.10+)
def Age_Classification_Match(age):
    match age:
        case age if age < 0:
            return "Invalid Age"
        case age if age <= 12:
            return "Child"
        case age if age <= 19:
            return "Teen"
        case age if age <= 59:
            return "Adult"
        case age if age >= 60:
            return "Senior"
        

age = int(input("Enter the age : "))
print(Age_Classification_Match(age))