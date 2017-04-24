import random
import os
import sys
import time

NEED_REDIRECTION = False
SOLUTION_FILE_NAME = "your_program_name.ext"

def fail(message):
    print("Result:\n{0}".format(message))
    exit(0)
    
def fail_wa(correct, program):
    fail("Program output:\n{0}\nCorrect output:\n{1}".format(program, correct))

def run_solution():
    command = SOLUTION_FILE_NAME
    if NEED_REDIRECTION:
        command += " <input.txt >output.txt"
    return os.system(command)

def generate_test(test_number):
    os.system("generate.py {0}".format(test_number))
   
def run_test(test_number, TL=2.0):
    generate_test(test_number)
    start_time = time.time()
    exit_code = run_solution()
    end_time = time.time()
    if exit_code != 0:
        fail("Non-zero exit code.")
    run_checker()
    if end_time - start_time > TL:
        fail("Time limit exceeded. Used time: {0}".format(end_time - start_time))
    
def main():
    test_number = 1
    prev_time = time.time()
    while True:
        run_test(test_number)
        test_number += 1
        cur_time = time.time()
        if cur_time - prev_time >= 3.0:
            print("{0} tests passed.\n".format(test_number))
            prev_time = cur_time
# -----------------------------------------------------------------------------
# ------ Write checker here ---------------------------------------------------
           
def run_checker():
    # TODO: write running of correct solution
    with open("input.txt", "rt") as sys.stdin:
        # read input data here
        pass
    # you can use your input data here
    with open("output.txt", "rt") as sys.stdin:
        # read output data here
        pass
    # here you can use all read data
    
main()