# Last updated: 7/1/2026, 1:45:46 PM
1# class Solution:
2#     def maxArea(self, height: List[int]) -> int:
3#         i, j = 0, len(height)-1
4#         max_h = 0
5
6#         while i<j:
7#             max_h = max(max_h, (j-i)* min(height[i],height[j]))
8#             if height[i]<=height[j]:
9#                 i+=1
10#             else:
11#                 j-=1
12
13#         return max_h
14
15
16
17class Solution:
18    def maxArea(self, height: List[int]) -> int:
19        left = 0
20        right = len(height) -1
21        max_area = 0
22
23        while left < right:
24            width = right - left
25            h = min(height[left], height[right])
26
27            current_area = width * h
28
29            if current_area > max_area:
30                max_area = current_area
31            
32            if height[left] < height[right]:
33                left += 1
34            else:
35                right -= 1
36        return max_area
37
38
39
40
41
42
43
44
45