# 19941_햄버거분배_distribute hambergur
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

HP = list(input().rstrip())

# print(HP)
cnt = 0
for i in range(N):
    if HP[i] == 'P':
        # temp = K
        # while temp:
        #     a, b = i-temp, i+temp
        #     if 0 <= a <= N-1:
        #         if HP[a] == 'H':
        #             HP[a] = 'E'
        #             cnt += 1
        #             break
        #     if 0 <= b <= N-1:
        #         if HP[b] == 'H':
        #             HP[b] = 'E'
        #             cnt += 1
        #             break
        #     temp -= 1
        for j in range(i-K, i+K+1):
            if 0 <= j <= N-1:
                if HP[j] == 'H':
                    HP[j] = 'E'
                    cnt += 1
                    break

print(cnt)