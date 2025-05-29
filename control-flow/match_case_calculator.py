# Prompt for User Input:
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
user = (input("Choose the operation (+, -, *, /):"))

# Perform the Calculation using Match case 
# output the result

match user:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")

    case "-":
        result = num1 - num2
        print(f"The result is {result}.")

    case "*":
        result = num1 * num2
        print(f"The result is {result}.")

    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    
    






