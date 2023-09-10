
import sys

input = sys.stdin.readline

S = input().strip()
T = input().strip()

result = 0
# 문자열 T 리스트 입력
def dfs(t):
    global result
     
    if t==S:
        result = 1
        return
    
    if len(t)==0:
        return 0
    
    if t[-1]=='A': 
        dfs(t[:-1])
    if t[0]=='B': 
        dfs(t[1:][::-1]) 

dfs(T)
print(result)