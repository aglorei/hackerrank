"""
https://www.hackerrank.com/challenges/extra-long-factorials/problem
Difficulty: Medium
"""

from functools import reduce

def extraLongFactorials(n):
    return reduce(lambda x, y: x * y, range(n + 1)[1:])
