class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        def backtrack(start, path):

            res.append(path[:])  # on ajoute une copie
            for i in range(start, len(nums)):

                path.append(nums[i])       # choix

                backtrack(i + 1, path)    # exploration

                path.pop()                # annulation

        

        backtrack(0, [])

        return res
            
        