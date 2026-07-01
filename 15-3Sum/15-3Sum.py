# Last updated: 7/1/2026, 1:25:22 AM
1# class Solution:
2#     def threeSum(self, nums: List[int]) -> List[List[int]]:
3#         nums.sort()
4#         size = len(nums)
5
6#         res =[]
7#         def twosum(c,sum):
8#             j = size-1
9#             i=c
10#             while i<j:
11#                 if nums[i]+nums[j] == sum:
12#                     res.append([nums[c-1],nums[i],nums[j]])
13#                     i+=1
14#                     j-=1
15#                     while i<j and nums[i]==nums[i-1]:
16#                         i+=1
17#                     while i<j and nums[j]==nums[j+1]:
18#                         j-=1
19#                 elif nums[i]+nums[j]< sum:
20#                     i+=1
21#                 else:
22#                     j-=1
23            
24
25
26#         for i, num in enumerate(nums):
27#             sum = -num
28#             if i>=1 and nums[i-1]== nums[i]:
29#                 continue
30#             twosum(i+1, sum)
31
32#         return res
33            
34class Solution:
35    def threeSum(self, nums: List[int]) -> List[List[int]]:
36        nums.sort()
37        array = []
38    
39        for i in range(len(nums)):
40            if i > 0 and nums[i] == nums[i - 1]:
41                continue
42            l = i+1
43            r = len(nums) - 1
44
45            while l< r:
46                sum = nums[i] + nums[l] + nums[r]
47                if sum < 0:
48                    l+=1
49                elif sum > 0:
50                    r-=1
51                else:
52                    array.append([nums[i],nums[l],nums[r]])
53
54                    l+=1
55                    r-=1
56                    
57                    while l<r and nums[l] == nums[l-1]:
58                        l+=1
59                    while l<r and nums[r] == nums[r+1]:
60                        r-=1
61
62        return array
63
64
65
66
67