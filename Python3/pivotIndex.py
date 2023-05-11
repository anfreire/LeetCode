from typing import List

'''
724. Find Pivot Index

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
'''

class Solution:
    # Here there is nothing complex, just a simple for loop.
    # We are using slicing to get the sum of the elements to the left and to the right of the pivot.
    # https://www.programiz.com/python-programming/methods/built-in/slice
    # Its important to understant how the slicing works, because it can be a little bit confusing.
    # https://www.w3schools.com/python/trypython.asp?filename=demo_string_negativeindex
    # Play around and try to understand how it works on the link above.
    def pivotIndex(self, nums: List[int]) -> int:
        for x in range(len(nums)):
            if sum(nums[:x]) == sum(nums[x + 1:]):
                return x
        return -1
        