class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(path, used):

            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for num in nums:
                
                if num in used:
                    continue

                path.append(num)
                used.add(num)

                dfs(path, used)

                path.pop()
                used.remove(num)


        dfs([], set())
        return res