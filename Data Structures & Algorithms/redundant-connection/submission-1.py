class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        par = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(n):
            res = n

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            
            return res

        def union(n1,n2):
            r1, r2 = find(n1), find(n2)

            if r1 == r2:
                return True
            
            if rank[r2] > rank[r1]:
                par[r1] = r2
                rank[r2] += rank[r1]
            else:
                par[r2] = r1
                rank[r1] += rank[r2]

            return False
        
        for e1,e2 in edges:
            if union(e1,e2):
                return [e1,e2]

        