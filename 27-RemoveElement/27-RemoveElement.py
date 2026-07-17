# Last updated: 7/16/2026, 6:59:38 PM
1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        emt = []
4        l = len(nums)
5        c = 0
6        for i in range(len(nums)-1,-1,-1):
7            print("i = ",i)
8            if nums[i] == val:
9                nums.pop(i)
10                print("1st change = ",nums)
11                
12                c+=1
13        # ans = len(emt)
14        ans = l-c
15        return ans