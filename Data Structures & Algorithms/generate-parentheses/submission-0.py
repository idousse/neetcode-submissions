class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        def dfs(openp, closep, path):
            if openp == closep == n:
                res.append(path[:])
                return

            if openp < n:
                dfs(openp + 1, closep, path + "(")

            if closep < openp:
                dfs(openp, closep + 1, path + ")")
        
        dfs(0,0,"")
        return res