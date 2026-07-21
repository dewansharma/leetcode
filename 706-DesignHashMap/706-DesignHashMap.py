# Last updated: 7/20/2026, 10:55:08 PM
1class MyHashMap:
2
3    def __init__(self):
4        self.dictt = {}
5
6    def put(self, key: int, value: int) -> None:
7        if key in self.dictt:
8            self.dictt[key] = value
9        else:
10            self.dictt[key] = value
11
12    def get(self, key: int) -> int:
13        if key not in self.dictt:
14            return -1
15        else:
16            return self.dictt[key]
17
18    def remove(self, key: int) -> None:
19        if key in self.dictt:
20            self.dictt.pop(key)
21
22
23# Your MyHashMap object will be instantiated and called as such:
24# obj = MyHashMap()
25# obj.put(key,value)
26# param_2 = obj.get(key)
27# obj.remove(key)