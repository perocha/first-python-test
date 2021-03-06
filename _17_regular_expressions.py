'''
Example of regular expressions
'''
import re

def use_regex():
    '''Function with examples of regex usage'''
    text = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
    lst = re.findall('\\S+@\\S+', text)
    print(f"1: {lst}")
    lst = re.findall("[me]", text)
    print(f"2: {lst}")
    lst = re.findall("[Aa]", text)
    print(f"3: {lst}")
    lst = re.findall("[a-z]", text)
    print(f"4: {lst}")
    lst = re.findall("[\\s]", text)
    print(f"5: {lst}")
    lst = re.findall("[\\S]", text)
    print(f"6: {lst}")
    lst = re.findall("[0-9]", text)
    print(f"7: {lst}")
    lst = re.split("\\s", text)
    print(f"8: {lst}")
    lst = re.findall("[^a-z]", text)
    print(f"9: {lst}")

use_regex()
