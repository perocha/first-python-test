number = input ("Enter your number: ")
root = input ("Enter the root: ")

def root_calculation (number, root):
    my_number = float (number)
    my_root = float (root)
    root_calculation = pow (my_number, 1/(my_root))
    return root_calculation

#print ("The root " + root + " of " + number + " is " + str(pow(float(number),1/float(root))))
my_result = root_calculation(number, root)
print ("The root " + root + " of " + number + " is " + str(my_result))