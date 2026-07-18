# Last updated: 7/18/2026, 2:14:33 PM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        p1 = m
7        p2 = 0
8        while p2<len(nums2):
9            # print("m = ",p1)
10            nums1.pop(p1)
11            # print("array after popping = ",nums1)
12            
13            nums1.insert(m,nums2[p2])
14            # print(nums1)
15
16            p1+=1
17            p2+=1
18        nums1.sort()
19        # print(nums1