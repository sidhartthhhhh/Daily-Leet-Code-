# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        num = 0
        current = head
        while current:
            num = (num << 1) | current.val  # Left shift and add current node's value
            current = current.next
        return num