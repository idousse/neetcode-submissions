class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        h = []

        for x,y in points:
            distance = x**2 + y**2

            heapq.heappush(h, (-distance, [x,y]))

            if len(h) > k:
                heapq.heappop(h)

        h = [x[1] for x in h]
        return h