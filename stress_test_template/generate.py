import random
import sys

def generate(args):
    # write your generator here
    pass
    
def main():
    args = sys.argv[1:]
    with open("input.txt", "wt") as sys.stdout:
        generate(args)
      
main()