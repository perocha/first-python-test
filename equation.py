import re

class Equation:
    number1 = 0
    number2 = 0
    result = 0
    operation = ""

    def __init__(self, number1, number2, operation) -> None:
        self.number1 = number1
        self.number2 = number2
        self.operation = operation
        return None

    def calculate_result (self):
        try:
            if self.operation == "+":
                self.result = self.number1 + self.number2
                return self.result
            elif self.operation == "-":
                self.result = self.number1 - self.number2
                return self.result
            else:
                return False
        except:
            return False

    def print_result (self):
        # First lets make sure we calculate the result of the operation
        self.calculate_result()

        # Obtain the lenghts of each part of the equation for printing
        len_number1 = len(str(self.number1))
        len_number2 = len(str(self.number2))
        len_result = len(str(self.result))
        len_operation = len(self.operation)
        # Identify the maximum length from all parts
        max_lenght = max(len_number1, len_number2 + len_operation + 1, len_result)

        # Print the result
        trailing_spaces = max_lenght - len_number1
        print (" " * trailing_spaces, end = "")
        print (f"{self.number1}")

        trailing_spaces = max_lenght - len_number2 - len_operation - 1
        print (" " * trailing_spaces, end = "")
        print (f"{self.operation} {self.number2}")
        print ("-" * max_lenght)

        trailing_spaces = max_lenght - len_result
        print (" " * trailing_spaces, end = "")
        print (f"{self.result}")

        return None