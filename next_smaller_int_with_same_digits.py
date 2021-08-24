# Write a function that takes a positive integer and returns the next smaller
# positive integer containing the same digits.
# For example:
#
# next_smaller(21) == 12
# next_smaller(531) == 513
# next_smaller(2071) == 2017
import itertools
from itertools import combinations


def next_smaller(n):
    elements = list(str(n))
    length = len(str(n))
    numbers = sum([list(map(list, combinations(elements, length))) for i in range(length + 1)], [])
    return numbers


print(next_smaller(21))
print(next_smaller(123456798))
print(next_smaller(135))
