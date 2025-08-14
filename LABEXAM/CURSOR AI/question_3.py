def convert_temperature(): 
    temp = float(input("Enter the temperature : "))
    input_unit = input("Enter the units you are entering (C, F, K) : ").strip().upper()# Read output unit
    output_unit = input("Enter the units you are willing to convert (C, F, K) : ").strip().upper()# Convert input to Celsius first
    if input_unit == 'C':
        temp_c = temp
    elif input_unit == 'F':
        temp_c = (temp - 32) * 5/9
    elif input_unit == 'K':
        temp_c = temp - 273.15
    else:
        print("Invalid input unit.")
        return
    if output_unit == 'C':
        result = temp_c
        unit_name = "Celsius"
    elif output_unit == 'F':
        result = temp_c * 9/5 + 32
        unit_name = "Fahrenheit"
    elif output_unit == 'K':
        result = temp_c + 273.15
        unit_name = "Kelvin"
    else:
        print("Invalid output unit.")
        return
    print(f"Temperature in {unit_name} : {result}")
convert_temperature()