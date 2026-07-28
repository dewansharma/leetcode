# Last updated: 7/28/2026, 12:04:19 PM
1from typing import List
2
3
4class Solution:
5    def isValidSudoku(self, board: List[List[str]]) -> bool:
6    
7        for row in board:
8            seen = set()
9            for val in row:
10                if val == '.':
11                    continue
12                if val in seen:
13                    return False
14                seen.add(val)
15
16
17        for col in range(9):
18                seen  = set()
19                for r in range(9):
20                    val = board[r][col]
21                    if val == '.':
22                        continue
23                    if val in seen:
24                        return False
25                    seen.add(val)
26
27        for i in range(0,9,3):
28            for j in range(0,9,3):
29                seen = set()
30                for x in range(i, i+3):
31                    for y in range(j, j+3):
32                        val = board[x][y]
33                        if val == '.':
34                            continue
35                        if val in seen:
36                            return False
37                        seen.add(val)
38        return True