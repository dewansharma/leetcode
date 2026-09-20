# Last updated: 9/20/2026, 1:31:27 AM
1# class Solution:
2#     def lengthOfLongestSubstring(self, s: str) -> int:
3#         hashmap = {}
4
5#         ans,i= 0,0
6#         n=len(s)
7#         for j in range(n):
8#             if s[j] in hashmap:
9#                 i = max(i, hashmap[s[j]]+1 )
10#             ans = max(j-i+1, ans)
11#             hashmap[s[j]] = j
12#         return ans
13
14
15
16
17# class Solution:
18#     def lengthOfLongestSubstring(self, s: str) -> int:
19#         left = 0
20#         right = 0
21#         window = set()
22#         longest_length = 0
23#         for right in range(len(s)):
24#             while s[right] in window:
25#                 window.discard(s[left])
26#                 left+=1
27                
28#             window.add(s[right])
29#             longest_length = max(longest_length,len(window))
30
31#             right +=1 
32#         return longest_length
33 
34
35
36class Solution:
37    def lengthOfLongestSubstring(self, s: str) -> int:
38        hset = set()
39        l = 0
40        max_l = 0
41
42        
43        for r in range(len(s)):
44            # print()
45            
46            # print('r = ', r)
47            # hset.add(s[r])
48
49            # print('hset = ', hset)
50
51            
52
53            while s[r] in hset:
54                hset.remove(s[l])
55                # print('updated hset = ', hset)
56                l += 1
57            
58                
59            hset.add(s[r])
60
61            max_l = max(max_l,r-l+1)
62            print(max_l)
63        return max_l
64
65