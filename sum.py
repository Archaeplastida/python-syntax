def sum_nums(nums):
    """Given list of numbers, return sum of those numbers.

    For example:
      sum_nums([1, 2, 3, 4])

    Should return (not print):
      10
    """
    result = 0
    for x in nums:
        result += x
    return result

print("sum_nums returned", sum_nums([1, 2, 3, 4]))