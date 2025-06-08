def perform_operation(num1, num2, operation):
    if operation == 'divide':
         if num2 == 0 :
             return "Error: Division by zero not allowed" 
         else:
             result = num1 / num2

    elif operation == 'add':
        result = num1 + num2

    elif operation == 'subtract':
        result = num1 - num2

    elif operation == 'multiply':
        result = num1 * num2
    

    else:
        return "Invalid operation"
            
    
    
    return result



  