from typing import List

'''
1480. Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
'''

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Here we are using list comprehension. https://www.programiz.com/python-programming/list-comprehension
        # We didn't have other approach, like using the second paramater of the sum function, because that would decrease the sum of the array by one element each time.
        # We want to keep adding elements, as we iterate through the array and not the inverse.
        # To achieve this we HAD to use slicing. https://www.programiz.com/python-programming/methods/built-in/slice
        # I used the range with 2 arguments, because through some tests, I found that this approach is faster than running like this:
        # - return [sum(nums[:i + 1]) for i in range(len(nums))]
        # It would still work, but it would be a little bit slower.
        return [sum(nums[:i]) for i in range(1, len(nums) + 1)]