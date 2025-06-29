class Calculator:
    # Class attribute shared by all instances and methods
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a,b):
        """Static method to add two numbers."""
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """Class method to multiply two numbers.
        Prints the class attribute 'calculation_type' before returning the result.
        """
        print(cls.calculation_type)
        return a * b