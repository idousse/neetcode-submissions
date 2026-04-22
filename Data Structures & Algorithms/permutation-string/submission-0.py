class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        freq = {}
        
        for c in s1:
            freq[c] = freq.get(c, 0) + 1

        left = 0
        window = {}

        for right in range(len(s2)):
            c = s2[right]
            window[c] = window.get(c, 0) + 1

            if right - left + 1 > len(s1):
                left_char = s2[left]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
                left += 1

            if window == freq:
                return True

        return False