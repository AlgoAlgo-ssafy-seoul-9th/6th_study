'''
31256KB	92ms
'''


N, K = input().split()
String = list(input())


N = int(N)
K = int(K)

cnt = 0
for i in range(N):
    if String[i] == 'P':
        for j in range(i-K, i+K+1):
            if j >= 0 and j < N:
                if String[j] == 'H':
                    String[j] = 0
                    cnt += 1
                    break

print(cnt)