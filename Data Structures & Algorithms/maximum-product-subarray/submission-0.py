class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curMin = curMax = res = nums[0]

        for n in nums[1:]:
            curMin, curMax = min(n * curMin, n * curMax, n), max(n * curMin, n * curMax, n)
            res = max(res, curMax)

        return res