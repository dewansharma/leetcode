# Last updated: 7/2/2026, 11:31:01 PM
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
17class Solution:
18    def lengthOfLongestSubstring(self, s: str) -> int:
19        left = 0
20        right = 0
21        window = set()
22        longest_length = 0
23        for right in range(len(s)):
24            while s[right] in window:
25                window.discard(s[left])
26                left+=1
27                
28            window.add(s[right])
29            longest_length = max(longest_length,len(window))
30
31            right +=1 
32        return longest_length
33 
34
35
36