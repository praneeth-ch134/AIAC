def cm_to_inches():
    try:
        cm = float(input("Enter the length (cm) : "))
        inches = cm / 2.54
        print(f"Length in meters : {inches:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
cm_to_inches()