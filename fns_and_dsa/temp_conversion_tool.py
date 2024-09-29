FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

convert = int(input("Enter the temperature to convert: "))
cf = input("Is this temprature in Celsius or Fahrenheit? (C/F):")
if cf.upper() == 'F':
    result = convert_to_celsius(convert)
    print(f"{convert}°F is equal to {result:.2f}°C.")
elif cf.upper() == 'C':
    result = convert_to_fahrenheit(convert)
    print(f"{convert}°C is equal to {result:.2f}°F.")
else:
    print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
