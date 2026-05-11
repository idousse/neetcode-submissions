class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        res = []

        def dfs(path, rem, start):

            if rem < 0:
                return
            
            if rem == 0:
                res.append(path[:])

            for i in range(start, len(nums)):
                remainder = rem - nums[i]
                path.append(nums[i])
                dfs(path, remainder, i)
                path.pop()
        
        dfs([], target,0)
        return res