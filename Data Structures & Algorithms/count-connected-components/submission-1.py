class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        par = [i for i in range(n)]
        rank = [1] * n


        def find(n):
            res = n

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]

            return res
        
        def union(n1, n2):
            r1, r2 = find(n1), find(n2)

            if r1 == r2:
                return 0

            if rank[r2] > rank[r1]:
                par[r1] = r2
                rank[r2] += rank[r1]
            else:
                par[r2] = r1
                rank[r1] += rank[r2]

            return 1

        res = n
        for e1, e2 in edges:
            res -= union(e1, e2)
        
        return res





