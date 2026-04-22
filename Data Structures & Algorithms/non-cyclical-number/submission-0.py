class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        while n != 1:
            w = 0
            if n in seen:
                return False
            seen.add(n)

            for num in str(n):
                w += int(num) ** 2
            
            n = w

        return True