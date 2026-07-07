# Last updated: 7/7/2026, 2:41:42 AM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        top = 0
4        bottom = len(matrix) - 1
5        mid = (top + bottom)//2
6        row_index = -1
7        while top <= bottom:
8            if target < matrix[mid][0]:
9                bottom = mid -1
10            elif target > matrix[mid][-1]:
11                top = mid + 1
12            else:
13                row_index = mid
14                break
15            mid = (top + bottom)//2
16        row = matrix[row_index]
17        left = 0
18        right = len(row) - 1
19        middle = (left + right)//2
20        while left <= right:
21            if target < row[middle]:
22                right = middle - 1
23            elif target > row[middle]:
24                left = middle + 1
25            if target == row[middle]:
26                return True
27            middle = (left + right)//2
28            
29        if target not in row:
30            return False
31
32