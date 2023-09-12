# 12919_A와B2_A and B 2
import sys
from collections import deque
input = sys.stdin.readline

S = input().strip()
T = input().strip()

idx = len(S)
q = deque()
q.append(T)
ans = 0
while q:
    temp = q.popleft()
    if temp == S:
        ans = 1
        break

    if temp[-1] == 'A':
        if temp[:-1] != '':
            q.append(temp[:-1])
    if temp[0] == 'B':
        temp = temp[::-1]
        if temp[:-1] != '':
            q.append(temp[:-1])

print(ans)
