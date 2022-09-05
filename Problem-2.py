
# 23. Merge k Sorted Lists

'''
Leetcode all test cases passed: Yes
Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]])
      k is length of lists
      n is total number of elements in lists
      Time Complexity: O(n log k) 
      Space Complexity: O(k)
'''
import heapq as hp
class Node(object):
    def __init__(self, pointer: int):
        self.val = pointer.val
        self.pointer = pointer

    def __lt__(self, other):
        return self.val < other.val
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        head = ListNode()
        n = head
        for l in lists:
            if l:
                hp.heappush(heap,Node(l))
        while heap:
            curr = hp.heappop(heap)
            
            k = ListNode(curr.val)
            n.next = k
            n = n.next  
            curr = curr.pointer.next
            if curr:
                hp.heappush(heap,Node(curr))
        
        return head.next
