# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        current = dummy

        carry = 0

        while l1 or l2 or carry:

            # Get values from both lists
            if l1:
                val1 = l1.val
            else:
                val1 = 0

            if l2:
                val2 = l2.val
            else:
                val2 = 0

            # Add the two digits and carry
            total = val1 + val2 + carry

            # Digit to store
            digit = total % 10

            # New carry
            carry = total // 10

            # Create new node
            current.next = ListNode(digit)
            current = current.next

            # Move both pointers
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next
        