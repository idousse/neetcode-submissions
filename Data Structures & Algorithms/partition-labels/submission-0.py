class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_letter = {}
        res = []

        for i in range(len(s)):
            last_letter[s[i]] = i
        
        
        max_index = 0
        start = 0

        for i in range(0,len(s)):
            max_index = max(max_index, last_letter[s[i]])

            if max_index == i:
                res.append(i - start + 1)
                start = i + 1

        return res