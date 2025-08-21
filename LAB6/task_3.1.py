
def Age_Classification(age):
    if age >= 0 and age <= 12:
        return "Child"
    elif age >= 13 and age <= 19:
        return "Teen"
    elif age >= 20 and age <= 59:
        return "Adult"
    elif age >= 60:
        return "Senior"
    else :
        return "Invalid Age"
    
age = int(input("Enter the age : "))
print(Age_Classification(age))