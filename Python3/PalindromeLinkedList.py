from typing import List

'''
234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        number = str()
        while head:
            number += str(head.val)
            head = head.next
        if number == number[::-1]:
            return True
        return False