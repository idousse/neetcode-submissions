class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = {}
        for i in range(len(numbers)):
            if target - numbers[i] in s:
                index1 = s[target - numbers[i]] +1
                index2 = i+1
                return [index1, index2]
            s[numbers[i]] = i
        