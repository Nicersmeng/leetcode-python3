class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        target = ListNode(0)
        p=target
        add = 0
        while l1 and l2:
            tmp_sum = (l1.val + l2.val + add )%10
            add = (l1.val + l2.val + add )//10
            p.next = ListNode(tmp_sum)
            p = p.next
            l1 = l1.next
            l2 = l2.next
        l1 = l1 if l1 else l2
        while add:
            if l1:
                p.next = ListNode((l1.val+add)%10)
                add = (l1.val+add)//10
                p,l1 = p.next,l1.next
            else:
                p.next = ListNode(add)
                p = p.next
                break
        p.next = l1

        return target.next
