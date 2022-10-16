from os import *
from sys import *
from collections import *
from math import *

def nextPermutation(permutation, n):
    for i in reversed(range(n)):
        if i == 0:
            return permutation.reverse()
        else:
            if permutation[i] > permutation[i-1]:
                permutation[i], permutation[i-1] = permutation[i-1], permutation[i]
                permutation[i:] = sorted(permutation[i:])
                return permutation


print(nextPermutation([1,3,2], 3))
                    


