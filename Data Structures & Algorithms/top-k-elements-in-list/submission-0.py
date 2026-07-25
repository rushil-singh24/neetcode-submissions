class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1
        sortedItems = sorted(map.items(), key=lambda pair: pair[1], reverse=True)
        ans = []
        for i in range (0,k):
            ans.append(sortedItems[i][0])
        return ans