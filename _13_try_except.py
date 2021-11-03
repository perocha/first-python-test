'''
Example of try-except to calculate the N root of a number
'''
def root_calculation (number, root):
    '''Function to calculate the N root of a number'''
    return pow (number, 1/(root))

def main():
    '''Main procedure'''
    try:
        number = float(input ("Enter your number: "))
        root = float(input ("Enter the root: "))

        my_result = root_calculation(number, root)
        print (f"The root {root} of {number} is {my_result}")
    except ValueError:
        print ("You need to enter numbers!!")
    except ZeroDivisionError as err:
        print (f"ZeroDivisionError exception: {err}")

main()
