class TimeMap:

    def __init__(self):
        self.a = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.a:
            self.a[key] = []
        self.a[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.a:
            return ""
        
        res = ""
        values_array = self.a[key]
        left, right = 0, len(values_array) -1

        while left <= right:
            mid = (left + right) // 2

            if values_array[mid][1] <= timestamp:
                res = values_array[mid][0]
                left = mid + 1
            else:
                right = mid - 1
            
        return res



