'''
(Very) basic calculator example
'''
def calculator():
    ''' Main function to simulate a simple calculator'''
    number = float(input ("Enter your number: "))
    root = float(input ("Enter the root: "))

    def root_calculation (number, root):
        return pow (number, 1/(root))

    my_result = root_calculation(number, root)
    print (f"The root {root} of {number} is {my_result}")

calculator()
