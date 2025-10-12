FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR)+32
try:
    enter_temperature = int(input("Enter the temperature to convert: "))
    celsius_or_fahrenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    match celsius_or_fahrenheit:
        case 'C':
            print(f"{enter_temperature}C is {convert_to_fahrenheit(enter_temperature)}")

        case 'F':
            print(f"{enter_temperature}F is {convert_to_celsius(enter_temperature)}")

except ValueError:
    print("Invalid temperature. Please enter a numeric value.") 
        