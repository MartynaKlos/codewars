# Given an array of integers.
#
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.
#
# If the input array is empty or null, return an empty array.
# Example
#
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
#


def count_positives_sum_negatives(arr):
    if not arr:
        return []

    count_of_positives = 0
    sum_of_negatives = 0
    for number in arr:
        if number > 0:
            count_of_positives += 1
        elif number < 0:
            sum_of_negatives += number

    result = [count_of_positives, sum_of_negatives]
    return result