# 19941 햄버거 분배
import sys

input = sys.stdin.readline

# input
N, K = map(int, input().split())
bench = input().strip()

# define
full = set()

# logic
for i in range(N):
    # 햄버거 기준 판별
    if bench[i] == "H":
        # K 범위 내에 P인데 아직 안 먹은 사람 저장
        for p in range(i - K, i + K + 1):
            if 0 <= p < N and bench[p] == "P" and p not in full:
                full.add(p)
                # 찾으면 멈춤
                break
# 햄버거 먹어서 배부른 사람 수
print(len(full))
