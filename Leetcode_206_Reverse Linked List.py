from typing import Optional

from Coding_Skills.LeetCode_21_mergesortedlist import ListNode

# recursive approach
'''
if not head or not head.next:
    return head
reversed_head = self.reverseList(head.next)
head.next.next = head
head.next = None
return reversed_head'''


# iterative approach
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    if head!=None and head.next==None:
        return head
    else:
        temp =  None
        next_node = None
        while head!=None:
            next_node = head.next
            head.next = temp
            temp = head
            head = next_node
    return temp
