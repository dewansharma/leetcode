# Last updated: 7/1/2026, 12:46:18 AM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        l = 0
4        r = len(numbers) - 1
5        sum = numbers[l] + numbers[r]
6        array = []
7
8        for i in range(len(numbers)):
9            # sum = numbers[l] + numbers[r]
10            
11            if sum == target:
12                array.append(l+1)
13                array.append(r+1)
14                # print('sum = ',sum)
15                return array
16            elif sum < target:
17                l+=1
18                sum = numbers[l] + numbers[r]
19                
20                # print('sum = ',sum)
21
22            elif sum > target:
23                r-=1
24                sum = numbers[l] + numbers[r]
25                # print('sum = ',sum)
26        return array
27
28                
29
30