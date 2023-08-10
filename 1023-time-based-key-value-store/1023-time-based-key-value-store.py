class TimeMap:

    def __init__(self):
        self.data = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        if key in self.data and self.data[key]:
            values = self.data[key]

            if values[-1][1] < timestamp:
                return values[-1][0]
            if values[0][1] > timestamp:
                return ""

            l, r = 0, len(values) - 1
            while l <= r:
                m = (l + r) // 2    

                if values[m][1] == timestamp:
                    return values[m][0]

                if values[m][1] < timestamp:
                    l = m + 1
                else:
                    r = m - 1

            print(l, r)
            if r >= 0:
                return values[r][0]
            # else:
            #     return values[l][0]
        return ""



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)