class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        start = 0
        end = len(height) - 1
        max_vol = 0
        
        while start < end:
            if height[start] < height[end]:
                min_index = start
            else:
                min_index = end
            
            cur_vol = (end - start) * height[min_index]
            
            if min_index == start:
                start+=1
            else:
                end-=1

            if cur_vol > max_vol:
                max_vol = cur_vol
            
        return max_vol

        
        