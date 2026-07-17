# Last updated: 7/16/2026, 11:21:27 PM
1# class Solution:
2#     def validPalindrome(self, s: str) -> bool:
3
4#         def check_palindrome(s, i, j, x):
5#             while i<j:
6#                 if s[i] != s[j]:
7#                     if x==1:
8#                         return False
9#                     return check_palindrome(s, i+1,j,1) or check_palindrome(s,i,j-1,1)
10                
11#                 i+=1
12#                 j-=1
13#             return True
14
15#         return check_palindrome(s,0,len(s)-1,0)
16
17class Solution:
18    def check(self,s,l,r,count):
19        print(l,r,count)
20       
21        while l < r:
22            # print(l,r,count)
23            if s[l] != s[r]:
24                ans1 = ans2 = False 
25                count += 1
26                if count > 1:
27                    return False
28                
29                # if s[l] == s[r-1]:
30                #     r =r -1
31                #     ans1 = self.check(s,l,r,count)
32                # if s[l+1] == s[r]:
33                #     l = l+1
34                #     ans2 = self.check(s,l,r,count)
35                
36
37                    
38                # return ans1 or ans2
39                
40                return self.check(s,l+1,r,count) or self.check(s,l,r-1,count)
41
42            elif s[l] == s[r]:
43                l += 1
44                r -= 1
45                        
46        return True
47    
48
49    def validPalindrome(self, s: str) -> bool:
50        l = 0
51        r = len(s) - 1
52        if len(s) == 1:
53                print("yes, a palindrome...")
54        count = 0
55        return self.check(s,l,r,count)
56        
57        