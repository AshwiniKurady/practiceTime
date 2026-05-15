#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    output = [0 for x in range(n)]
    state = 0
    for i in range(n,0):
        print("Inside")
        state = i
        print("first state", state)
        # while len(n) - state!= 0:
        #     output[state].append(" ")
        #     state = state+1
        # state = i
        # while i>0:
        #     output[state].append("#")
        #     i = i-1
if __name__ == '__main__':
    n = 6
    staircase(n)