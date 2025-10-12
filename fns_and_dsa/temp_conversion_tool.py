FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR)+32

enter_temperature = int(input("Enter the temperature to convert: "))
celsius_or_fahrenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

match celsius_or_fahrenheit:
    case 'C':
        if type(enter_temperature) == str:
            print("Invalid input")
        else:
            print(f"{enter_temperature}C is {convert_to_fahrenheit(enter_temperature)}")
    case 'F':
        if type(enter_temperature) == str:
            print("Invalid input")
        else:
            print(f"{enter_temperature}F is {convert_to_celsius(enter_temperature)}")
        