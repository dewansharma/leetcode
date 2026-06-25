# Last updated: 6/25/2026, 2:05:29 AM
1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        
4        stack = []
5        answer = 0
6        for token in tokens:
7            if token in ['-','/','+','*']:      
8                right = int(stack.pop())
9                left = int(stack.pop())
10                if token == '-':
11                    answer = left - right 
12                if token == '+':
13                    answer = right + left
14                if token == '/':
15                    answer = int(left / right)
16                if token == '*':
17                    answer = right * left
18                # print("answer is ", answer)
19                stack.append(answer)
20                # print('stack = ',stack)
21
22            else:
23                stack.append(token)
24
25        return int(stack[0])