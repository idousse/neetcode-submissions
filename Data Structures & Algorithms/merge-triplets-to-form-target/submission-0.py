class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        res = [False] * 3
        t0,t1,t2 = target

        for trip in triplets:
            if trip[0] <= t0 and trip[1] <= t1 and trip[2] <= t2:
                if trip[0] == t0:
                    res[0] = True
                if trip[1] == t1:
                    res[1] = True
                if trip[2] == t2:
                    res[2] = True

        return res[0] and res[1] and res[2]



