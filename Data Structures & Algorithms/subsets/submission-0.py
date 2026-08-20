class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.finallist = []
        self.subset = []

        def recurse(i):
            if i >= len(nums):
                self.finallist.append(self.subset.copy())
                return
            else:
                self.subset.append(nums[i])
                recurse(i+1)
                self.subset.pop()
                recurse(i+1)
        
        recurse(0)
        return self.finallist