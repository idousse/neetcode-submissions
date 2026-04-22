class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        count = {}

        left = max_count = result = 0

        for right in range(len(s)):
            r = s[right]
            count[r] = count.get(r, 0) + 1

            if count[r] > max_count:
                max_count = count[r]

            window_size = right - left + 1

            if window_size - max_count > k:
                l = s[left]
                count[l] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result 