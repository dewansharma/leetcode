# Last updated: 7/21/2026, 1:21:12 AM
1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        n = len(nums)
7        # print(nums)
8        # i=0
9        start=0
10        count = 0
11        while count < n:
12            i=start
13            current = nums[start]
14            while True:
15                # print()
16                new_i = (i+k)%n
17                # print("new_i = ",new_i)
18                next = nums[new_i]
19                # print('next = ',next)
20                nums[new_i] = current
21                # print("nums = ",nums)
22
23                current = next
24                # print("current = ",current)
25
26                i = new_i
27                # print("nums = ",nums)
28                count+=1  
29                if i == start:
30                    break
31            # print(nums)
32            start+=1
33              