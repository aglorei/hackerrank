"""
https://www.hackerrank.com/challenges/non-divisible-subset/problem
Difficulty: Medium
"""

def nonDivisibleSubset(k, arr):
    remainders = {r: 0 for r in range(k)}

    for n in arr:
        remainders[n % k] += 1

    count = min(remainders[0], 1)

    for r in range(1, k//2 + 1):
        if r == k - r:
            count += min(remainders[r], 1)
        else:
            count += max(remainders[r], remainders[k - r])
    return count
