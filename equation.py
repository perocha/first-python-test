'''
Equation class
'''

class Equation:
    '''Class Equation'''
    number1 = 0
    number2 = 0
    result = 0
    operation = ""

    def __init__(self, number1, number2, operation) -> None:
        '''Class constructor'''
        self.number1 = number1
        self.number2 = number2
        self.operation = operation

    def calculate_result (self):
        '''Calculate the result of the equation'''
        try:
            if self.operation == "+":
                self.result = self.number1 + self.number2
                return self.result
            if self.operation == "-":
                self.result = self.number1 - self.number2
                return self.result
            return False
        except TypeError:
            print ("Type error in parameters")
            return False

    def print_result (self):
        '''Calculate and print the result with the specific format'''
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
