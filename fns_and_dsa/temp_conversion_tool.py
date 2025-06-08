# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR  = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# converting fahrenheit to celsius
def  convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 
    return celsius

# converting  celsius to fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# user input and calculatiuon
temp = float (input(("Enter the temperature to convert: ")))
choice =  input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if choice == "C":
    temp_convert_f = convert_to_fahrenheit(temp)
    print(f"{temp}°C is {temp_convert_f}°F")
elif choice == "F":
    temp_convert_c = convert_to_celsius(temp)
    print(f"{temp}°F is {temp_convert_c}°C")
else:
    print("Invalid choice! Please enter 'C' or 'F'.")
