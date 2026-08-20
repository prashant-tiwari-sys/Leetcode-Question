# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def removeNthFromEnd(self, head, n):
        def remove(node):
            idx = remove(node.next) + 1 if node else 0
            if idx == n + 1:
                node.next = node.next.next
            return idx

        dummy = ListNode(0, head)
        remove(dummy)
        return dummy.next