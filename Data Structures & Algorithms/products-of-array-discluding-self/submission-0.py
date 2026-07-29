class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      pre = [1]
      post = [1]
      final = []
      for i in range(1, len(nums)):
        pre.append(nums[i-1]*pre[i-1])
      for i in range (len(nums)-2, -1, -1):
        post.append(nums[i+1] * post[-1])
      post.reverse()
      for i in range(0, len(nums)):
        final.append(pre[i] * post[i])
      return final
            