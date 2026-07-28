# Last updated: 7/27/2026, 10:44:28 PM
1# from typing import List
2
3
4# class Solution:
5#     def productExceptSelf(self, nums: List[int]) -> List[int]:
6#         temp = 0
7#         ar = []
8#         ans = []
9#         for i in range(len(nums)):
10#             # print("array nums = ",nums)
11#             temp = nums[i]
12#             # print('temp = ',temp)
13#             nums.pop(i)
14#             # print('nums = ',nums)
15#             p = 1
16#             for j in range(len(nums)):
17#                 p *= nums[j]
18#             ans.append(p)
19#             # print("ans = ",ans)
20#             nums.insert(i,temp)
21#         print("answer is ", ans)
22#         return ans
23
24class Solution:
25    def productExceptSelf(self, nums: List[int]) -> List[int]:
26        n = len(nums)        
27        left = [0]*n
28        right = [0]*n
29        ans = [0]*n
30        for i in range(len(nums)):
31            if i == 0:
32                left[i] = 1
33            elif i == n-1:
34                left[i] = left[i-1]*nums[i-1]
35            else:
36                left[i] = left[i-1]*nums[i-1]
37        for i in range(n-1,-1,-1):
38            if i == n-1:
39                right[n-1] = 1
40            else:
41                right[i] = right[i + 1] * nums[i + 1]
42        for i in range(n):
43            ans[i] = left[i] * right[i]
44        # print(left)
45        # print(right)
46        return ans