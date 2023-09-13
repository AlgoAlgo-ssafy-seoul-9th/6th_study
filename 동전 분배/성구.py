# 1943_동전분배_coin-distribution
import sys
input = sys.stdin.readline

for tc in range(3):
    N = int(input())

    coins = []
    total = 0
    for _ in range(N):
        c, cnt = map(int, input().split())
        total += c*cnt
        coins.append([c, cnt])
    if total%2 == 1:
        print(0)
        continue
    coins.sort(key=lambda x:-x[0])
    # print(coins)

    # a, b = 0, 0
    mid = total//2

    check = [0]*(mid+1)
    check[0] = 1
    for c in coins:
        value, cnt = c[0], c[1]

        for j in range(mid, value-1, -1):
            if check[j-value]:
                for i in range(cnt):
                    if j+value*i <= mid:
                        check[j+value*i] = 1
                    else:
                        break
            if check[mid]:
                break
        if check[mid]:
            break

    print(check[-1])