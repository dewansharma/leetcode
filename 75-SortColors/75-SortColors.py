# Last updated: 7/23/2026, 10:39:14 AM
1# class Solution:
2#     def sortColors(self, nums: List[int]) -> None:
3#         """
4#         Do not return anything, modify nums in-place instead.
5#         """
6#         c0 = curr = 0
7#         c2 = len(nums)-1
8
9#         while curr<=c2:
10#             if nums[curr] == 0:
11#                 nums[c0], nums[curr] = nums[curr], nums[c0]
12#                 c0+=1
13#                 curr+=1
14#             elif nums[curr] == 2:
15#                 nums[c2], nums[curr] = nums[curr], nums[c2]
16#                 c2-=1
17#             else:
18#                 curr+=1
19        
20
21class Solution:
22    def sortColors(self, nums: List[int]) -> None:
23        n =len(nums)
24        l = 0
25        r = n - 1
26        current = 0
27        while current<=r:
28            if nums[current] == 0:
29                nums[current],nums[l] = nums[l],nums[current]
30                l+=1
31                current+=1
32            elif nums[current] == 1:
33                current +=1
34            elif nums[current] == 2:
35                nums[current],nums[r] = nums[r],nums[current]
36                r-=1
37            
38        print(nums)