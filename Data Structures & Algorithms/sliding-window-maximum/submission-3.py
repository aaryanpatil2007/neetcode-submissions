class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k
        maxlist = []
        while right <= len(nums):
            sublist = nums[left:right]
            maxnum = sublist[0]
            for num in sublist:
                maxnum = max(maxnum, num)
            maxlist.append(maxnum)
            left += 1
            right += 1
        return maxlist
