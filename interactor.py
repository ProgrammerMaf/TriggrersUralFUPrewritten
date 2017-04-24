import time
import random
import itertools
import re

class IdlenessLimitExceeded(Exception):
    def __init__(self):
        pass

def writeVerdict(res):
    f = open("result.txt", "wt")
    f.writelines("{0}".format(res))
    f.close()
    
def try_read():
    try:
        x = input()
        return x
    except EOFError:
        return None

'''        
Use it instead of input()
Do not write code like 'input = read'
'''
def read(IdlenessTimeLimit = 4):
    start_time = time.time()
    while True:
        ans = try_read()
        if ans is not None:
            return ans
        cur_time = time.time()
        if cur_time - start_time > IdlenessTimeLimit:
            raise IdlenessLimitExceeded("Idleness limit!")

# -----------------------------------------------
# Write your code here
            
def main():
    pass
    
main()