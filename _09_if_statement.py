'''
If statement examples
'''
def main():
    '''Main function'''
    is_raining = False
    is_cold = False

    if is_raining:
        print ("It is raining")
    else:
        print ("Not raining today")

    if is_cold:
        print ("It is cold")
    else:
        print ("Not cold today")

    if is_raining and is_cold:
        print ("Stay at home!")
    elif is_raining and not is_cold:
        print ("Take an umbrella")
    elif not is_raining and is_cold:
        print ("Take a good coat")
    else:
        print ("Great weather!!")

    def max_num (num1, num2, num3):
        if num1 >= num2 and num1 >= num3:
            return num1
        if num2 >= num1 and num2 >= num3:
            return num2
        return num3

    max_number = max_num (12, 2, 23)
    print (f"The max number is {max_number}")


main()
