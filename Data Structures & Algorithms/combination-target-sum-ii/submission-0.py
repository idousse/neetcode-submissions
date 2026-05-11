class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        

        res = []

        def dfs(path, rem, start):

            if rem < 0:
                return

            if rem == 0:
                res.append(path[:])

            candidates.sort()
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                path.append(candidates[i])
                dfs(path, rem - candidates[i], i+1)
                path.pop()
            
        dfs([], target, 0)
        return res