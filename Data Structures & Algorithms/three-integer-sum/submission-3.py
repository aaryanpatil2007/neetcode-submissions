class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # fix on one number, then implement two sum on right side only
        totallist = []
        sortednums = sorted(nums)
        for i in range(len(sortednums) - 2):
            if i > 0 and sortednums[i] == sortednums[i-1]:
                continue
            else:
                currnumber = sortednums[i]
                target = -(currnumber)
                left = i+1
                right = len(sortednums) - 1
                while left < right:
                    if sortednums[left] + sortednums[right] == target:
                        totallist.append([currnumber, sortednums[left], sortednums[right]])
                        left += 1
                        right -= 1
                        while left < len(sortednums) and sortednums[left] == sortednums[left - 1]:
                            left += 1
                        while right > i and sortednums[right] == sortednums[right + 1]:
                            right -=1
                    elif sortednums[left] + sortednums[right] > target:
                        right -= 1
                    elif sortednums[left] + sortednums[right] < target:
                        left += 1
        return totallist
            

