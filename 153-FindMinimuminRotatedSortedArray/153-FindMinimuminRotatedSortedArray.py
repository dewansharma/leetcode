# Last updated: 7/7/2026, 8:06:47 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        left = 0
4        right = len(nums) - 1
5        mid = (left + right)//2
6
7        while left < right:
8            if nums[mid] < nums[right]:
9                right = mid
10                mid = (left + right)//2
11                answer =  nums[mid]
12            elif nums[mid] > nums[right]:
13                left = mid + 1
14                mid = (left + right)//2
15                answer =  nums[mid]
16        if left == right:
17            answer = nums[mid]
18
19        return answer
20
21