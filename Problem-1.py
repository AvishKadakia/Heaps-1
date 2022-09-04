
# 215. Kth Largest Element in an Array

'''
Leetcode all test cases passed: Yes
Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      n is length of nums
      Time Complexity: O(n log k) 
      Space Complexity: O(k)
'''
import heapq as hp
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for num in nums:
            hp.heappush(heap,num)
            if len(heap) > k:
                hp.heappop(heap)
        return heap[0]
