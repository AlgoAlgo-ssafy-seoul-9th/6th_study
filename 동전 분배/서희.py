for _ in range(3):
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
