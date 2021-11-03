def root_calculation (number, root):
    return pow (number, 1/(root))

try:
    number = float(input ("Enter your number: "))
    root = float(input ("Enter the root: "))

    my_result = root_calculation(number, root)
    print (f"The root {root} of {number} is {my_result}")
except ValueError:
    print ("You need to enter numbers!!")
except ZeroDivisionError as err:
    print (f"ZeroDivisionError exception: {err}")
except:
    print (f"Other exceptions")