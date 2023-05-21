from typing import Optional

'''
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        1 -> 2 -> 3 -> 4 -> 5 -> None

        Here we want to reverse the list, so we need to change the direction of the pointers.
        None <- 1 <- 2 <- 3 <- 4 <- 5

        To do this, we need to keep track of the previous node and the next node.
        We can do this by creating two new variables, new_prev and new_next.
        We can then iterate through the list, and change the direction of the pointers.

        Important: in linked list, when we refer to the head.next, we are referring to the next node, not the value of the next node.
        What i mean by this is:
        head = 1 -> 2 -> 3 -> 4 -> 5 -> None
        head.next = 2 -> 3 -> 4 -> 5 -> None
        head.next.next = 3 -> 4 -> 5 -> None
        and so on...
        '''
        new_prev = None
        while head:
            new_next = head.next
            head.next = new_prev
            new_prev = head
            head = new_next
        return new_prev
    
    

def main():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    sol = Solution()
    head = sol.reverseList(head)
    while head:

        print(head.val)
        head = head.next
    
if __name__ == '__main__':
    main()

            