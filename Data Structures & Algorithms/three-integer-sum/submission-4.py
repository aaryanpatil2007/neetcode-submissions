class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        finallist = set()
        for i in range(len(nums)):
            targetval = 0 - nums[i]
            checkerdict = {}
            for j in range(i+1, len(nums)):
                otherval = targetval - nums[j]
                if otherval in checkerdict.keys():
                    if not (nums[i], nums[j], otherval) in finallist:
                        finallist.add((nums[i], nums[j], otherval))
                else:
                    checkerdict[nums[j]] = j
        return [list(t) for t in finallist]
                
                
            