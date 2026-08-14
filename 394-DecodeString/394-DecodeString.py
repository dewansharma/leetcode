# Last updated: 8/14/2026, 3:46:11 PM
1class Solution:
2    def decodeString(self, s: str) -> str:
3        stack =[]
4        cur_str = ''
5        cur_n = 0
6        final_str = ''
7        for i in range(len(s)):
8            
9            print()
10            print("Loop number is ", i)
11            print()
12            
13            if s[i].isalpha():
14                cur_str += s[i]
15                print('cur_s = ',cur_str)
16            
17            if s[i].isdigit():
18                cur_n = (cur_n * 10) + int(s[i])
19                print('cur_n = ',cur_n)
20            
21            if s[i] == '[':
22                stack.append(cur_str)
23                stack.append(cur_n)
24                print(stack)
25
26                cur_str = ''
27                cur_n = 0
28
29            if s[i] == ']':
30                
31                count = stack.pop()
32                prev_s = stack.pop()
33                print('previous string = ',prev_s)
34                print('current string = ',cur_str)
35                print('count = ',count)
36                updated_str = prev_s + count*cur_str
37                cur_str = updated_str
38                print('updated string = ',updated_str)
39                print('stack updated = ',stack)
40        return cur_str
41        