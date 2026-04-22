class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            prod = 1
            j = i
            for _ in range(len(nums)-1):
                j+=1
                prod *= nums[j % len(nums)]
            res.append(prod)
        return res