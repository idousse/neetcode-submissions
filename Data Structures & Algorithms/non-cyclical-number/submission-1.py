class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            n = self.sumOfSquares(n)
        
        return True

    def sumOfSquares(self, n:int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10

        return output
