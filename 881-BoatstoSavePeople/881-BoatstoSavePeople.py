# Last updated: 7/20/2026, 12:28:01 AM
1# class Solution:
2#     def numRescueBoats(self, people: List[int], limit: int) -> int:
3#         people.sort()
4
5#         i, j = 0, len(people)-1
6#         res = 0
7#         while i<=j:
8#             res +=1
9#             if people[i]+people[j]<=limit:
10#                 i+=1
11#             j-=1
12#         return res
13
14
15class Solution:
16    def numRescueBoats(self, people: List[int], limit: int) -> int:
17        l = 0
18        r = len(people) - 1
19        boat = 0
20        people.sort()
21        while l<=r:
22            if (people[l] + people[r])<=limit :
23                boat+=1
24                print("boat = ",boat)
25                l+=1
26                r-=1
27            elif (people[l] + people[r])>limit :
28                boat+=1
29                r-=1
30
31        print("length of boat = ",boat)
32        return boat