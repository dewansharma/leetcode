# Last updated: 7/20/2026, 10:45:57 PM
1class MyHashSet:
2
3    def __init__(self):
4        self.sett = set()
5
6    def add(self, key: int) -> None:
7        return self.sett.add(key)
8
9    def remove(self, key: int) -> None:
10        if key in self.sett:    
11            self.sett.remove(key)
12        else:
13            return 0
14
15    def contains(self, key: int) -> bool:
16        if key in self.sett:
17            return True
18        else:
19            return False
20
21
22# Your MyHashSet object will be instantiated and called as such:
23# obj = MyHashSet()
24# obj.add(key)
25# obj.remove(key)
26# param_3 = obj.contains(key)