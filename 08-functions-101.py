def say_hi ():
    print ("Hello world")

def say_hi_with_name (name):
    print (f"Hello world to {name}")

def square_number (input_number):
    return input_number * input_number

# Default parameters
def function_default_param (country = "Portugal"):
    print (country)

# Arbitrary Arguments *args
def function_args (*test_arg):
    print ("function_args ####")
    i = 0
    for arg in test_arg:
        print (f"{i} = {arg}")
        i += 1

# Arbitrary Keyword Arguments **kwargs
def function_kwargs (**test_arg):
    print ("function_kwargs ####")
    i = 0
    for arg in test_arg:
        print (f"{i} = {arg}")
        i += 1

# Receive a list as argument
def function_list (one_list):
    print ("function_list ####")
    print (one_list)
    for item in one_list:
        print (item)

# Function to return a list with the even numbers
def get_even_numbers (input_numbers):
    even_nums = [num for num in input_numbers if not num % 2]
    return even_nums


say_hi ()
say_hi_with_name ("Pedro")

number = square_number (5)
print (number)

my_list = {"this", "is", "my", "list"}
function_list (my_list)

function_args ("test", "2", "another arg", 123, -123, 1.34123)

function_kwargs (a = "test", b = "2", c = "another arg")

function_default_param ("Spain")
function_default_param ()


numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
even_num = get_even_numbers (numbers)
print (even_num)