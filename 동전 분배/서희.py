'''for _ in range(3):
    N = int(input())
    total_cnt = 0 
    coin = 0
    lst_money = []

    for _ in range(N):
        money, cnt = map(int, input().split())
        coin += money * cnt
        total_cnt += cnt
        lst_money.extend([money] * cnt)  # lst_money에 money를 cnt만큼 추가하는 메서드임!

    half_coin = coin // 2

    for l in range(total_cnt):
        if lst_money[l] <= half_coin:
            half_coin = half_coin - lst_money[l]
            if half_coin == 0:
                print(1)
                break
    else:
        print(0)
'''


# 여전히 실패,,, 시간초과


import sys

for _ in range(3):
    N = int(sys.stdin.readline())
    coins = {}
    total_coin = 0

    for _ in range(N):
        coin, cnt = map(int, sys.stdin.readline().split())
        coins[coin] = cnt
        total_coin += coin * cnt

    if total_coin % 2:
        print(0)
    else:
        half = total_coin // 2
        dp = [0] * (half + 1)
        dp[0] = 1

        for coin, cnt in coins.items():
            for idx in range(half + 1):
                if dp[idx]:
                    for index in range(
                        idx + coin, min(idx + coin * cnt + 1, half + 1), coin
                    ):
                        dp[index] = 1
        # 목표금액이 만들 수 있는지 확인
        if dp[half]:
            print(1)
        else:
            print(0)
