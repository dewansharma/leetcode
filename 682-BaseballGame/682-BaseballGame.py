# Last updated: 8/6/2026, 7:46:27 PM
1from typing import List
2
3
4class Solution:
5    def calPoints(self, operations: List[str]) -> int:
6        stack = []
7        for i in range(len(operations)):
8            if operations[i] == '+':
9                add = stack[-1] + stack[-2]
10                stack.append(add)
11                print('stack = ',stack)
12
13            elif operations[i] == 'D':
14                double = stack[-1] * 2
15                stack.append(double)
16                print('stack = ',stack)
17
18            elif operations[i] == 'C':
19                # element = stack[i]
20                stack.pop()
21                print('stack = ',stack)
22
23            # elif operations[i].isdigit() is True:
24            else:
25                item = int(operations[i])
26                stack.append(item)
27                print('stack = ',stack)
28
29    
30        print(sum(stack))
31        return sum(stack)
32            