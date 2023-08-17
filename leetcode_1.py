#https://leetcode.com/problems/sliding-window-maximum/description/
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        #brute force approach
        # if not nums:
        #     return []
        # if k == 1:
        #     return nums
        # ans = []
        # i = 0
        # left = 0
        # right = k
        # while (right)< len(nums)+1:
        #     temp = nums[left:right]
        #     print(temp)
        #     temp_max = max(temp)
        #     print(temp_max)
        #     ans.append(temp_max)
        #     left+=1
        #     right+=1
        # return ans
        # Deque approach where you pop every entry of the list and compare it with the new element being added
        dq = deque()
        ans = []

        for i in range(k):
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        ans.append(nums[dq[0]])

        for i in range(k, len(nums)):
            if dq and dq[0] == i - k:
                dq.popleft()
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            ans.append(nums[dq[0]])
        return ans
