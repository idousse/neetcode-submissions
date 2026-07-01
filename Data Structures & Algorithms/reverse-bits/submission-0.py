class Solution:
    def reverseBits(self, n: int) -> int:
        
        result = 0

        for _ in range(32): 
            result = result << 1
            bitzero = n & 1
            result = result | bitzero
            n = n >> 1
        
        return result



