# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if head.next is None or left == right:
            return head
        dummy = ListNode(0, head)
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next
        p, q = pre, pre.next
        cur = q
        # +1, so when for loop done, 'cur' is at right's next node
        for _ in range(right - left + 1):
            t = cur.next
            cur.next = pre
            pre, cur = cur, t
        p.next = pre
        # p,q did not change by the for loop, but now pre at right(or called m) node, cur at right+1 node
        q.next = cur
        return dummy.next

############

class Solution_optimize:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        prev = dummy
        prev.next = head
        p = head

        for i in range(1, m):
            prev = p
            p = p.next

        original_first = p # this is anchor node always pointing to the next-to-be-swapped
        for i in range(m, n):
            current_head = prev.next
            future_head = original_first.next
            
            prev.next = future_head
            original_first.next = future_head.next
            future_head.next = current_head

        return dummy.next

############

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def reverseBetween(self, head, m, n):
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """

    def reverse(root, prep, k):
      cur = root
      pre = None
      next = None
      while cur and k > 0:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
        k -= 1
      root.next = next
      prep.next = pre
      return pre

    dummy = ListNode(-1)
    dummy.next = head
    k = 1
    p = dummy
    start = None
    while p:
      if k == m:
        start = p
      if k == n + 1:
        reverse(start.next, start, n - m + 1)
        return dummy.next
      k += 1
      p = p.next
