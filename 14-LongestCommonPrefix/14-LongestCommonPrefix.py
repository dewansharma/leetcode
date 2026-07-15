# Last updated: 7/15/2026, 12:37:30 AM
1# class Solution:
2#     def longestCommonPrefix(self, strs: List[str]) -> str:
3#         idx = None
4#         n = len(strs)
5
6#         for i, c in enumerate(strs[0]):
7#             for j in range (1, n):
8#                 if i == len(strs[j]) or c!=strs[j][i]:
9#                     return strs[0][:i]
10#         return strs[0]
11        
12
13class Solution:
14    def longestCommonPrefix(self, strs: List[str]) -> str:
15        ans = ""
16        for i in range(len(strs[0])):
17            # s1 = strs[i]
18            # if len(strs[i]) == 1:
19            #         return strs[0]
20            for j in range(1,len(strs)):
21                # if len(strs[0][i]) > len(strs[j][i]):
22                #     return ans
23                if i>=len(strs[j]) :
24                    return ans
25
26                if strs[0][i] !=  strs[j][i]:
27                    # ans += strs[j][i]
28                    # print(strs[j][i])
29                    # print("nothing")
30                    return ans
31                
32            ans += strs[0][i]
33            
34            # print(strs[j][i])
35        return ans
36