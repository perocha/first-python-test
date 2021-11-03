'''
Useful tools example (to be imported by another program)
'''
import random

THIS_IS_A_TEST = "Test"
THIS_IS_A_CONSTANT = 23

def get_file_extension (filename):
    '''Get the file extention'''
    return filename[filename.index(".") + 1:]

def roll_a_dice (num):
    '''Just roll a dice from 0 to num'''
    return random.randint (1,num)
