class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        keymap = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        finallist = []
        for i in range(len(nums)):
            if nums[i] in keymap.keys():
                keymap[nums[i]] += 1
            else:
                keymap[nums[i]] = 1
        for key, value in keymap.items():
            buckets[value].append(key)
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                finallist.append(num)
                if len(finallist) == k:
                    return finallist
        return finallist        