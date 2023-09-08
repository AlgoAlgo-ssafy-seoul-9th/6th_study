import sys

input = sys.stdin.readline

# input
S = input().strip()
T = input().strip()


# DFS
def dfs(t):
    stack = [t]
    # T -> S 갈수 있는가?
    while stack:
        s = stack.pop()
        # 길이가 같으면 확인
        if len(s) == len(S):
            # T -> S 가능 하면 1
            if s == S:
                return 1
            # 다르면 다음 거 확인
            continue
        # 마지막이 A면 빼줌
        if s[-1] == "A":
            stack.append(s[:-1])
        # 처음이 B이면 뒤집어서 B뺌
        if s[0] == "B":
            stack.append(s[::-1][:-1])
    # 모두 확인했는데 안되면 0
    return 0


print(dfs(T))


"""
# # 12919 A와 B 2
# import sys
# from collections import deque

# input = sys.stdin.readline

# S = input().strip()
# T = input().strip()


# def addA(s):
#     return s + "A"


# def addB(s):
#     return (s + "B")[::-1]


# def bfs(s):
#     que = deque([s])
#     # visited = set([s, a, b])
#     while que:
#         tmp = que.popleft()
#         if len(tmp) == len(T):
#             if tmp == T:
#                 return 1
#             continue

#         que.append(addA(tmp))
#         que.append(addB(tmp))
#         # a = addA(tmp)
#         # b = addB(tmp)
#         # if a not in visited:
#         #     visited.add(a)
#         # que.append(a)
#         # if b not in visited:
#         #     visited.add(b)
#         # que.append(b)
#     return 0


# # def dfs(s):
# #     stack = [s]
# #     visited = set()
# #     while stack:
# #         tmp = stack.pop()
# #         if len(tmp) == len(T):
# #             if tmp == T:
# #                 return 1
# #             continue
# #         if tmp in visited:
# #             continue
# #         else:
# #             visited.add(tmp)
# #             stack.append(addA(tmp))
# #             stack.append(addB(tmp))

# #         # a = addA(tmp)
# #         # b = addB(tmp)
# #         # if a not in visited:
# #         #     stack.append(a)
# #         #     visited.add(a)
# #         # if b not in visited:
# #         #     stack.append(b)
# #         #     visited.add(b)
# #     return 0


# print(dfs(S))
# # print(bfs(S))
# # print(answer)
# 12919 A와 B 2
import sys

input = sys.stdin.readline

S = input().strip()
T = input().strip()
visited = set()


def addA(s):
    return s + "A"


def addB(s):
    return (s + "B")[::-1]


def dfs(s):
    if len(s) == len(T):
        if s == T:
            print(1)
            exit(0)
        return
    if s in visited:
        return
    else:
        visited.add(s)
        dfs(addA(s))
        dfs(addB(s))
    return


dfs(S)

"""
