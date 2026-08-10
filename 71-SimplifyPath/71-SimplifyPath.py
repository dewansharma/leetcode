# Last updated: 8/10/2026, 9:09:13 PM
1class Solution:
2    def simplifyPath(self, path: str) -> str:
3        
4        parts = path.split('/')
5        stack = []
6        # print(path)
7
8        for part in parts:
9            if part == '..':
10                if stack:
11                    stack.pop()
12            elif part == '.' or part == '':
13                continue
14            else:
15                stack.append(part)
16        print(stack)
17        result = "/" + "/".join(stack)
18        print(result)
19        return result