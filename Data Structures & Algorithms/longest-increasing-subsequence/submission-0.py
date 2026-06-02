class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        

        prev = [1] * len(nums)

        for i in range(1, len(nums)):
            prev[i] = 1 + max((prev[j] for j in range(i) if nums[j] < nums[i]), default=0)

        return max(prev, default=0)