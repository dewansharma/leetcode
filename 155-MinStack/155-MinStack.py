# Last updated: 6/25/2026, 2:07:13 AM
1class MinStack:
2
3    def __init__(self):
4        self.stack = []
5        self.minstack = []
6
7    def push(self, value: int) -> None:
8        if not self.minstack:
9            self.minstack.append(value)
10            return self.stack.append(value)
11        if value < self.minstack[-1]:
12            self.stack.append(value)
13            return self.minstack.append(value)
14        else:
15            self.minstack.append(self.minstack[-1])
16            return self.stack.append(value)
17
18        # return self.stack.append(value)
19
20    def pop(self) -> None:
21        if not self.minstack:
22            self.stack.pop()
23        else:
24            self.minstack.pop()
25            self.stack.pop()
26
27    def top(self) -> int:
28        return self.stack[-1]
29
30    def getMin(self) -> int:
31        if not self.minstack:
32            return min(self.stack)
33        else:
34            return self.minstack[-1]
35        
36
37
38# Your MinStack object will be instantiated and called as such:
39# obj = MinStack()
40# obj.push(value)
41# obj.pop()
42# param_3 = obj.top()
43# param_4 = obj.getMin()