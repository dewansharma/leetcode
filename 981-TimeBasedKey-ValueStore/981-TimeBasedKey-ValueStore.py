# Last updated: 9/6/2026, 4:08:58 PM
1class TimeMap:
2
3    def __init__(self):
4        self.store = {}
5
6    def set(self, key: str, value: str, timestamp: int) -> None:
7        if key not in self.store:
8            self.store[key] = []
9
10        self.store[key].append((timestamp, value))
11
12    def get(self, key: str, timestamp: int) -> str:
13        if key not in self.store:
14            return ""
15
16        values = self.store[key]
17
18        l = 0
19        r = len(values) - 1
20        result = ""
21
22        while l <= r:
23            mid = (l + r) // 2
24
25            if values[mid][0] <= timestamp:
26                result = values[mid][1]
27                l = mid + 1
28            else:
29                r = mid - 1
30
31        return result
32
33
34# Your TimeMap object will be instantiated and called as such:
35# obj = TimeMap()
36# obj.set(key,value,timestamp)
37# param_2 = obj.get(key,timestamp)