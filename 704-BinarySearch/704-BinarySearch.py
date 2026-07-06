# Last updated: 7/6/2026, 4:41:59 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l = 0
4        r = len(nums) -1
5        m = (l+r)//2
6
7        while l <= r:
8            m = (l+r)//2
9
10            if target < nums[m]:
11                r = m-1
12            elif target > nums[m]:
13                l = m+1
14            elif target == nums[m]:
15                # print("m = ",m)
16                return m
17        if target not in nums:
18            return -1
19            