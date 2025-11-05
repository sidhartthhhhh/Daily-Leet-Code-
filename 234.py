# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        head_of_second_half = prev

        first_half_ptr = head
        second_half_ptr = head_of_second_half
        is_palindrome = True
        while second_half_ptr:
            if first_half_ptr.val != second_half_ptr.val:
                is_palindrome = False
                break
            first_half_ptr = first_half_ptr.next
            second_half_ptr = second_half_ptr.next

        return is_palindrome