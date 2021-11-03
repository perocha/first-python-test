'''
Some more advanced usage of functions
'''
import statistics as st
import time

def describe(sample):
    '''Function that returns 3 separate values'''
    return st.mean(sample), st.median(sample), st.mode(sample)

# Call with 3 separate variables
my_sample = [10, 2, 4, 7, 9, 3, 9, 8, 6, 7]
mean, median, mode = describe (my_sample)
print (mean)
print (median)
print (mode)

# Store the 3 results in one variable
desc = describe (my_sample)
print (desc)

#
# Decorator function to get execution time of another function
#
def my_timer(func):
    '''My time decorator function'''
    def _timer(*args, **kwargs):
        print(f"my_timer::start {args}")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start}")
        return result
    return _timer

# Add the decorator function before the function
@my_timer
def this_is_a_test(argument):
    '''Dummy function to test a decorator function'''
    print (f"this_is_a_test::start {argument}")
    time.sleep(1)
    print ("this_is_a_test::after 1 sec")
    time.sleep(2)
    print ("this_is_a_test::after 2 sec")

# Test the decorator function
this_is_a_test ("prueba")


#
# Additional examples of functions
#
def my_function (arg1, arg2, *args, **kwargs):
    '''Function to test multiple arguments'''
    print (f"a: {arg1}")
    print (f"b jk,: {arg2}")
    print (f"args: {args}")
    print (f"kwargs: {kwargs}")
    i = 0
    for arguments in args:
        print (f"args[{i}]: {arguments}")
        i += 1
    i = 0
    for arguments in kwargs.values():
        print (f"kwargs[{i}]: {arguments}")
        i += 1
    return arg1, arg2

print ("call my_function 1 ***************")
my_result = my_function ("a", "b")

print ("call my_function 2 ***************")
my_result = my_function ("a", "b", "c", "d", 123)

print ("call my_function 3 ***************")
my_result = my_function ("string1", "string2", "string3", key1 = "key1 value", key2 = "key2 value")
