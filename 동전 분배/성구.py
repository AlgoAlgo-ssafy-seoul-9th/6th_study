# 1943 동전 분배
import sys

input = sys.stdin.readline


for _ in range(3):
    # define
    coins = {}
    total = 0
    # input
    N = int(input())
    for i in range(N):
        coin, cnt = map(int, input().split())
        coins[coin] = cnt
        # 총 금액 산정
        total += coin * cnt
    # 총 금액이 홀수이면 무조건 불가능
    if total % 2:
        print(0)
    else:
        # 목표 금액으로 바꾸기
        total //= 2
        # index를 목표금액으로 갖는 배열 만듦
        dp = [0] * (total + 1)
        # 목표가 0 이면 무조건 만들 수 있으므로 1
        dp[0] = 1
        # 변화 저장용 (직접 변환하면 바꾼 index도 if문에서 걸려 모두 1이 됨)
        tmp = [*dp]
        for key, val in coins.items():
            for idx in range(total + 1):
                if dp[idx]:
                    for index in range(
                        idx + key, min(idx + key * val + 1, total + 1), key
                    ):
                        tmp[index] = 1
                if dp[total]:
                    break     
            dp = [*tmp]
            if dp[total]:
                break
        # 목표금액이 만들 수 있는지 value로 들어가 있음
        print(dp[total])


"""
# 동전으로 총 금액의 반액 만들기
def make_money_with_coin(coinList: list, coins: dict):
    money = 0

    return 0


# test case
for _ in range(3):
    # define
    coins = {}
    total = 0

    # input
    N = int(input())
    flag = 0
    for i in range(N):
        coin, cnt = map(int, input().split())
        coins[coin] = cnt
        total += coin * cnt
        if cnt % 2:
            flag += 0
        else:
            flag += 1
    if flag == N:
        print(1)
    elif total % 2:
        print(0)
    else:
        total /= 2

        coin_list = list(coins.keys())
        coin_list.sort(reverse=1)
        print(make_money_with_coin(coin_list, coins))

예외 케이스
4
3 7
5 2
7 3
8 1
30
21
9

3 4 12
8 1 8
5 2 10

"""
