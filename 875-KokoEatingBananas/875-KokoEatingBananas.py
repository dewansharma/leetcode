# Last updated: 9/6/2026, 12:25:11 AM
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3
4        left = 1
5        right = max(piles)
6
7        while left<right:
8            speed = (left+right)//2
9            hours_spent = 0
10
11            for pile in piles:
12                hours_spent+= math.ceil(pile/speed)
13
14            if hours_spent<=h:
15                right = speed
16            else:
17                left = speed+1
18
19        return right
20
21
22
23
24
25