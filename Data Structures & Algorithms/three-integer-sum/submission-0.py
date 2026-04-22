class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        rslt = []

        for i in range(len(nums) -2):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s == 0:
                    rslt.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif s > 0:
                    right -= 1
                else:
                    left += 1

        return rslt