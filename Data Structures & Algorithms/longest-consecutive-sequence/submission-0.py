class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        keymap = set()
        for num in nums:
            keymap.add(num)
        maxlongest = 0
        for num in nums:
            currlongest = 1
            if num - 1 not in keymap:
                while num + 1 in keymap:
                    currlongest += 1
                    num += 1
            maxlongest = max(currlongest, maxlongest)
        return maxlongest