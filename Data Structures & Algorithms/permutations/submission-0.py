class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(path, remaining):
            if not remaining:
                res.append(path[:])
                return
            
            for num in list(remaining):
                path.append(num)
                remaining.remove(num)
                dfs(path, remaining)

                remaining.add(num)
                path.pop()
        
        dfs([], set(nums))
        return res