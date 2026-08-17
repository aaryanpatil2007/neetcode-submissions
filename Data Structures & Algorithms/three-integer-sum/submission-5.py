class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final = []
        seen = set()
        for i in range(len(nums) - 2):
            value = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr = nums[left] + nums[right]
                if curr > value:
                    right -= 1
                elif curr < value:
                    left += 1
                elif curr == value:
                    if (nums[i], nums[left], nums[right]) not in seen:
                        seen.add((nums[i], nums[left], nums[right]))
                        final.append([nums[i], nums[left], nums[right]])
                    left += 1
        return final


        