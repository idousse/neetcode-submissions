class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(speed: int) -> bool:
            hours = sum((pile +speed -1) // speed for pile in piles)

            if hours > h:
                return False
            else:
                return True

        left, right = 1, max(piles)
        while left < right: 
            mid = (left + right) // 2

            if feasible(mid):
                right = mid
            else:
                left = mid + 1

        return left