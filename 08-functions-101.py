def say_hi ():
    print ("Hello world")

def say_hi_with_name (name):
    print (f"Hello world to {name}")

def square_number (input_number):
    return input_number * input_number


say_hi ()
say_hi_with_name ("Pedro")

number = square_number (5)
print (number)