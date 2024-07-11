# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """This finds the indices of the two numbers that add up to target
    >>> two_sum([2, 7, 11, 15], 9)
    [0, 1]
    """
    # short the numbers
    nums.sort()
    # Base case
    if len(nums) < 2:
        return None
    # use two pointers
    left = 0
    right = len(nums) - 1

    # Iterating through the list
    while left < right:
        # If Last index and first index values are matching return it
        if nums[left] + nums[right] == target:
            return [left, right]
        # If sum is less than target then increase the left pointer
        # because the numbers are in increasing order so if sum is less
        # than target it will be in increasing order
        elif nums[left] + nums[right] < target:
            left += 1
        # If sum is greater than target then decrease the right pointer
        # because the numbers are in decreasing order
        else:
            right -= 1
