class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []

        def dfs(path, start):
            if start == len(s):
                res.append(path[:])
                return 

            for i in range(start, len(s)):
                part = s[start:i + 1]
                if part == part[::-1]:
                    path.append(part)
                    dfs(path, i + 1)
                    path.pop()

        dfs([], 0)
        return res

        