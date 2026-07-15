# Last updated: 7/14/2026, 10:59:17 PM
1class Solution:
2    def mySqrt(self, x: int) -> int:
3        if x<2:
4            return x
5        
6        left, right = 2, x//2
7        mid = 0
8        while left<=right:
9            mid = left + (right-left)//2
10            mul = mid*mid
11            if mul == x:
12                return mid
13            elif mul<x:
14                left = mid+1
15            else:
16                right = mid-1
17        
18        return right