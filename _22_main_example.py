'''
Example of main guard
'''
print("before import math")
import math

print("before functionA")
def functionA():
    print("Function A")

print("before functionB")
def functionB():
    print("Function B {}".format(math.sqrt(100)))

print(f"before __name__ guard {__name__}")
if __name__ == '__main__':
    functionA()
    functionB()
print("after __name__ guard")