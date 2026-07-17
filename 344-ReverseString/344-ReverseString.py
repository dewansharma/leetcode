# Last updated: 7/16/2026, 8:00:03 PM
1# class Solution:
2#     def reverseString(self, s: List[str]) -> None:
3        # """
4        # Do not return anything, modify s in-place instead.
5        # """
6        # l, h = 0, len(s)-1
7        # while l<=h:
8        #     s[l], s[h] = s[h], s[l]
9        #     l+=1
10        #     h-=1
11        
12class Solution:
13    def reverseString(self, s: List[str]) -> None:
14        l = 0
15        r = len(s)-1
16        while l<r:
17            s[l],s[r] = s[r],s[l]
18            # print("s = ",s)
19            l+=1
20            r-=1
21        print(s)
22        return s