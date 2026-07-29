class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0 
        for num in numset:
            currLength = 1
            currNum = num
            if num - 1 not in numset:
                while currNum+1 in numset:
                    currLength += 1
                    currNum += 1
            if currLength > longest:
                longest = currLength
        return longest