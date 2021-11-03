'''
A program to calculate simple arithmetic problems and print the result in a formatted way

 32
+ 8
---
 40
'''
import equation

# arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

# arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

equation1 = equation.Equation (32, 8, "+")
equation1.print_result ()

equation2 = equation.Equation (1, 3801, "-")
equation2.print_result ()

equation3 = equation.Equation (9999, 9999, "+")
equation3.print_result ()

equation4 = equation.Equation (523, 49, "-")
equation4.print_result ()
