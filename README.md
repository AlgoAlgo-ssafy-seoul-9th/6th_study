# 6th_study

[백준 문제집](https://www.acmicpc.net/workbook/view/16780)

[프로그래머스 문제](https://school.programmers.co.kr/learn/courses/30/lessons/92341)

<br><br><br>

## [주차 요금 계산](./주차%20요금%20계산/)

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

### [민웅](./주차%20요금%20계산/민웅.py)

```py

```

### [병국](./주차%20요금%20계산/병국.py)

```py

```

### [상미](./주차%20요금%20계산/상미.py)

```py

```

### [서희](./주차%20요금%20계산/서희.py)

```py
from collections import defaultdict # default 값 지정해주는 것(여기서는 기본시간?)

def solution(fees, records):
    answer = []
    return answer
```

### [성구](./주차%20요금%20계산/성구.py)

```py
'''
차량 번호가 작은 자동차부터 요금 출력
누적으로 계산
fees
[ 기본시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원) ]
records
시간 기준 오름차순
'''
from collections import defaultdict

def solution(fees, records):
    answer = []
    check = dict()
    check_time = defaultdict(int)
    for record in records:
        hour, minute, number, code = int(record[:2]), int(record[3:5]), record[6:10], record[-2:]
        if code == "IN":
            check[number] = [hour, minute]
        else:
            check_time[number] += (hour*60 + minute)-(check[number][0]*60 + check[number][1])
            check.pop(number)
    for key, val in check.items():
        check_time[key] += (23*60+59) - (val[0]*60+val[1])
    number = list(check_time.keys())
    number.sort()
    for num in number:
        answer.append(check_time[num])
    for i in range(len(answer)):
        if answer[i] <= fees[0]:
            answer[i] = fees[1]
        else:
            if (answer[i] - fees[0]) / fees[2] > (answer[i] - fees[0]) // fees[2]:
                answer[i] = fees[1] + ((answer[i] - fees[0])//fees[2] + 1) * fees[3]
            else:
                answer[i] = fees[1] + ((answer[i] - fees[0])//fees[2]) * fees[3]
    return answer
```

</div>
</details>
<br><br><br>

## [햄버거 분배](./햄버거%20분배/)

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

### [민웅](./햄버거%20분배/민웅.py)

```py
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
```

### [병국](./햄버거%20분배/병국.py)

```py
n, k = map(int,input().split())
burger = list(input())
answer_list = []
# PPPPHHHH
# HHHHPPPP 이거 두개를 생각해봐,,
# 스택써서 pop하는게아니군,,
cnt = 0
for i in range(len(burger)):
    if burger[i] == "P": # 사람이 나오면 양옆 살피자,,
        for j in range(i-k,i+k+1): # 항상 왼쪽꺼 먹어치우면됨
            if 0<=j<n and burger[j] == "H" : # j<n 조건넣어야 인덱스에러안뜸 0<= 안넣어서틀림,,
                cnt += 1
                burger[j] = 'A' # 먹었으면 대체
                # print(burger)
                break
print(cnt)



```

### [상미](./햄버거%20분배/상미.py)

```py

```

### [서희](./햄버거%20분배/서희.py)

```py
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
```

### [성구](./햄버거%20분배/성구.py)

```py
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

```

</div>
</details>
<br><br><br>

## [A와 B 2](./A와%20B%202/)

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

### [민웅](./A와%20B%202/민웅.py)

```py

```

### [병국](./A와%20B%202/병국.py)

```py

```

### [상미](./A와%20B%202/상미.py)

```py

```

### [서희](./A와%20B%202/서희.py)

```py

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
```

### [성구](./A와%20B%202/성구.py)

```py
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
```

</div>
</details>
<br><br><br>

## [동전 분배](./동전%20분배/)

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

### [민웅](./동전%20분배/민웅.py)

```py
# 틀린곳 모르겠음
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
        break
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

# 시간초과
# # 1943_동전분배_coin-distribution
# import sys
# input = sys.stdin.readline

# for tc in range(3):
#     N = int(input())

#     coins = []
#     total = 0
#     for _ in range(N):
#         c, cnt = map(int, input().split())
#         total += c*cnt
#         coins.append([c, cnt])
#     if total%2 == 1:
#         print(0)
#         break
#     coins.sort(key=lambda x:-x[0])
#     # print(coins)

#     # a, b = 0, 0
#     mid = total//2

#     check = [0]*(mid+1)
#     check[0] = 1
#     for c in coins:
#         value, cnt = c[0], c[1]
#         for i in range(cnt):
#             for j in range(mid, -1, -1):
#                 if check[j]:
#                     if j+value <= mid:
#                         check[j+value] = 1

#     print(check[-1])
```

### [병국](./동전%20분배/병국.py)

```py

```

### [상미](./동전%20분배/상미.py)

```py

```

### [서희](./동전%20분배/서희.py)

```py
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

```

### [성구](./동전%20분배/성구.py)

```py
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
            dp = [*tmp]
        # 목표금액이 만들 수 있는지 value로 들어가 있음
        print(dp[total])

```

</div>
</details>
<br><br><br>
