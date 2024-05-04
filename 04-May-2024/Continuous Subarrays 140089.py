# Problem: Continuous Subarrays - https://leetcode.com/problems/continuous-subarrays/

from collections import deque

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        max_deque, min_deque = deque(), deque()
        result, left = 0, 0

        for right in range(len(nums)):
            while max_deque and nums[max_deque[-1]] < nums[right]:
                max_deque.pop()
            while min_deque and nums[min_deque[-1]] > nums[right]:
                min_deque.pop()

            max_deque.append(right)
            min_deque.append(right)

            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                left += 1
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()

            result += right - left + 1

        return result