# Last updated: 8/3/2026, 8:51:10 PM
1# class Solution:
2#     def longestConsecutive(self, nums: List[int]) -> int:
3#         nums_set = set(nums)
4
5#         longest_streak = 0
6
7#         for num in nums_set:
8#             if num-1 not in nums_set:
9#                 curr_streak =1
10#                 current_num = num
11
12#                 while current_num+1 in nums_set:
13#                     curr_streak+=1
14#                     current_num+=1
15                
16#                 longest_streak = max(curr_streak, longest_streak)
17
18#         return longest_streak
19
20
21from typing import List
22
23
24class Solution:
25    def longestConsecutive(self, nums: List[int]) -> int:
26        items = set()
27        current = 1
28        length = 1
29        longest = 0
30        if len(nums) == 0:
31                return 0
32        for i in range(len(nums)):
33            items.add(nums[i])
34        # print(items)
35
36        for num in items:
37            if num - 1 not in items:
38                current = num
39                length = 1
40                while current + 1 in items:
41                    current += 1
42                    length += 1
43                longest = max(longest, length)
44        # print(length)
45        return longest