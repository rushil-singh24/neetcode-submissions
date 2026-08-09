class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for k, num in enumerate(nums):
            if k != 0 and nums[k] == nums[k-1]:
                continue
            target = -num
            i = k+1
            j = len(nums) - 1
            while i < j:
                if nums[i] + nums[j] < target:
                    i += 1
                elif nums[i] + nums[j] > target:
                    j -= 1
                else:
                    add = [num, nums[i], nums[j]]
                    result.append(add)
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return result