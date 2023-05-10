from typing import List

'''
1337. The K Weakest Rows in a Matrix

You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

- The number of soldiers in row i is less than the number of soldiers in row j.
- Both rows have the same number of soldiers and i < j.

Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.
'''

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        soldiers = {index: sum(values) for index, values in enumerate(mat)}
# Using Dict Comprehension. https://www.programiz.com/python-programming/dictionary-comprehension
# Creating a dictionary with the index of the row as the key and the sum of the row as the value
# We are able to use sum because the values are 1's and 0's.
# If the values were different we could use this approach:
# - soldiers = {index: [x for x in values if x == 1] for index, values in enumerate(mat)}
# * Here we are using list comprehension. https://www.programiz.com/python-programming/list-comprehension
# By sorting firstly by index we are able to sastify the requierement:
#   "Both rows have the same number of soldiers and i < j."
# With this approach, when we later sort, the sorting algorithm will give priority to the order of elements in the list

        sorted_soldiers = sorted(soldiers, key=soldiers.values)
# Sorting the dictionary by the values
# And with that we sastify the requierement:
# * "Return the indices of the k weakest rows in the matrix ordered from weakest to strongest."

        return sorted_soldiers[:k]
# Now we just need to filter the first k elements, to achieve this we use slicing
# https://www.programiz.com/python-programming/methods/built-in/slice
