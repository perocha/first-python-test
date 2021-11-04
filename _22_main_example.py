'''
Example of main guard
'''
import math

print("before function_a")
def example_function_a():
    '''Function A'''
    print("Function A")

print("before function_b")
def example_function_b():
    '''Function B'''
    print(f"Function B {math.sqrt(100)}")

print(f"before __name__ guard {__name__}")
if __name__ == '__main__':
    example_function_a()
    example_function_b()
print("after __name__ guard")
