# Last updated: 9/6/2026, 3:28:52 PM
1from typing import List
2
3
4class Solution:
5    def search(self, nums: List[int], target: int) -> int:
6        l = 0
7        r = len(nums) -1 
8        mid = (l + r)//2
9
10        while l <= r:
11            
12            mid = (l + r)//2
13
14            if nums[mid] == target:
15                return True
16
17            if nums[l] == nums[mid] and nums[mid] == nums[r]:
18                    l+=1
19                    r-=1
20                    continue
21
22            
23            elif nums[l] <= nums[mid]:
24                if nums[l] <= target <= nums[mid]:
25                    r = mid - 1
26                else:
27                    l = mid + 1
28
29            
30
31            else:
32                if nums[mid] <= target <= nums[r]:
33                    l = mid + 1
34                else:
35                    r  = mid - 1    
36            mid = (l + r)//2
37            
38        return False