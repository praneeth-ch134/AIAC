def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: (C × 9/5) + 32
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Formula: (F - 32) × 5/9
    """
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """
    Convert Celsius to Kelvin.
    Formula: C + 273.15
    """
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """
    Convert Kelvin to Celsius.
    Formula: K - 273.15
    """
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """
    Convert Fahrenheit to Kelvin.
    Formula: (F - 32) × 5/9 + 273.15
    """
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    """
    Convert Kelvin to Fahrenheit.
    Formula: (K - 273.15) × 9/5 + 32
    """
    return (kelvin - 273.15) * 9/5 + 32

def get_temperature_input():
    """
    Prompt the user to enter a temperature value and its unit.
    Returns:
        value (float): The temperature value.
        unit (str): The unit of the temperature ('C', 'F', or 'K').
    """
    while True:
        try:
            value = float(input("Enter the temperature value: "))
            unit = input("Enter the unit of temperature (C for Celsius, F for Fahrenheit, K for Kelvin): ").strip().upper()
            if unit in ['C', 'F', 'K']:
                return value, unit
            else:
                print("Invalid unit. Please enter C, F, or K.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for temperature.")

def get_target_unit():
    """
    Prompt the user to enter the target unit for conversion.
    Returns:
        unit (str): The target unit ('C', 'F', or 'K').
    """
    while True:
        unit = input("Enter the unit you want to convert to (C for Celsius, F for Fahrenheit, K for Kelvin): ").strip().upper()
        if unit in ['C', 'F', 'K']:
            return unit
        else:
            print("Invalid unit. Please enter C, F, or K.")

def convert_temperature(value, from_unit, to_unit):
    """
    Convert temperature from one unit to another.
    Args:
        value (float): The temperature value.
        from_unit (str): The original unit ('C', 'F', or 'K').
        to_unit (str): The target unit ('C', 'F', or 'K').
    Returns:
        float: The converted temperature value.
    """
    if from_unit == to_unit:
        return value
    if from_unit == 'C':
        if to_unit == 'F':
            return celsius_to_fahrenheit(value)
        elif to_unit == 'K':
            return celsius_to_kelvin(value)
    elif from_unit == 'F':
        if to_unit == 'C':
            return fahrenheit_to_celsius(value)
        elif to_unit == 'K':
            return fahrenheit_to_kelvin(value)
    elif from_unit == 'K':
        if to_unit == 'C':
            return kelvin_to_celsius(value)
        elif to_unit == 'F':
            return kelvin_to_fahrenheit(value)
    raise ValueError("Invalid unit conversion.")

def main():
    """
    Main function to collect temperature data and convert it as per user interest.
    """
    print("Temperature Converter")
    value, from_unit = get_temperature_input()
    to_unit = get_target_unit()
    try:
        converted = convert_temperature(value, from_unit, to_unit)
        print(f"{value}°{from_unit} is equal to {converted:.2f}°{to_unit}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
