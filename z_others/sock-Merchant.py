#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar

def sockMerchant(n, ar):
    # Write your code here
    sock_pair_dict = {}
    total_pairs = 0
    for i in ar:
        if i in sock_pair_dict.keys():
            sock_pair_dict[i] +=1
        else:
            sock_pair_dict[i]=1
    
    for key, val in sock_pair_dict.items():
        if val == 2:
            total_pairs +=1
        if val>2:
            total_pairs += math.floor(val/2)
    return total_pairs
if __name__ == '__main__':

    n = 7

    ar = [10,20,20,10,10,30,50,10,20]

    print(sockMerchant(n, ar))
