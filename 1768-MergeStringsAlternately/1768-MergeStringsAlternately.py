# Last updated: 7/18/2026, 1:37:30 PM
1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3        p1 = 0
4        p2 = 0
5        l1 = len(word1)
6        l2 = len(word2)
7        word = ''
8        longest = max(l1,l2)
9        print(longest)
10
11        i = 0
12        while p1 < len(word1) or p2 < len(word2):
13        # while p1 < longest or p2 < longest:
14
15            if p1<len(word1):
16                word = word + word1[p1]
17                p1+=1
18
19            if p2<len(word2):
20                word = word + word2[p2]
21                p2+=1
22        print(word)
23        return word
24