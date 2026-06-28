class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF  # simulate 32-bit integer overflow
        while b & mask != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)