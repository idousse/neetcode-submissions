class Solution:

    def encode(self, strs: List[str]) -> str:
        rslt = ""

        for s in strs:
            rslt += str(len(s)) + "#" + s
        return rslt 

    def decode(self, s: str) -> List[str]:
        
        rslt = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            i = j + 1
            rslt.append(s[i:i + length])

            i += length
        return rslt 