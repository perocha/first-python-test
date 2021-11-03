'''
My first hello world program
'''
def hello_world():
    ''' Function that will print some hello world messages'''
    print ("hello world!")

    my_name = "Pedro"
    my_age = "47"
    print (f"My name is {my_name} and my age is {my_age}")
    print ("My name is " + my_name + " and my age is " + my_age)


    print (my_name.capitalize())
    print (my_name.casefold())
    print (my_name.isalpha())
    print (my_name.isalnum())
    print (my_name.upper())
    print (my_name.lower())

    my_index = 0
    while my_index < len(my_name):
        print (my_name[my_index])
        my_index += 1

    print (my_name.index("e"))
    my_name = "Pedroooo"
    print (my_name.index("o"))

    print (my_name.replace ("o","a"))

hello_world ()
