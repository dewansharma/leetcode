# Last updated: 7/24/2026, 1:38:55 AM
1# class Solution:
2#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3#         hashmap = defaultdict(int)
4#         for num in nums:
5#             hashmap[num] += 1
6#         sorted_map = sorted(hashmap, key=lambda x:hashmap[x], reverse =True)
7#         #Also works
8#         #sorted_map = heapq.nlargest(k, hashmap.keys(), key=lambda x:hashmap[x])
9#         return sorted_map[:k]
10
11
12from typing import List
13
14
15class Solution:
16    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
17        freq = {}
18        # count = 0
19        for num in nums:
20            if num in freq:
21                freq[num]+=1
22
23            else:
24                freq[num] = 1
25        # for item, frequ in freq.items():
26        sorted_list = sorted(freq.items(), key=lambda pair: pair[1], reverse=True)
27        print(sorted_list)
28        i = 0
29        arr = []
30        while i < k:
31            print(sorted_list[0][0])
32            arr.append(sorted_list[i][0])
33            i+=1
34        print(arr)
35        return arr
36
37