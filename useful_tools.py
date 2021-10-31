import random

THIS_IS_A_TEST = "Test"
THIS_IS_A_CONSTANT = 23

def get_file_extension (filename):
    return filename[filename.index(".") + 1:]

def roll_a_dice (num):
    return random.randint (1,num)