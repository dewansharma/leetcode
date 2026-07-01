# Last updated: 7/1/2026, 2:03:40 PM
1# class Solution:
2#     def isAnagram(self, s: str, t: str) -> bool:
3#         sar = [0]*26
4#         tar = [0]*26
5#         if len(s)!=len(t):
6#             return False
7#         for i in range(len(s)):
8#             sar[ord(s[i])-ord('a')]+=1
9#             tar[ord(t[i])-ord('a')]+=1
10
11#         return sar==tar
12
13        
14class Solution:
15    def isAnagram(self, s: str, t: str) -> bool:
16        array1 = []
17        array2 = []
18
19        for char in s:
20            array1.append(char)
21        for char in t:
22            array2.append(char) 
23
24        array1.sort()
25        # print(array1)
26        array2.sort()
27        # print(array2)
28
29        if array1 == array2:
30            return True
31        else:
32            return False
33
34
35