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

```

### [성구](./A와%20B%202/성구.py)

```py

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

```

### [병국](./동전%20분배/병국.py)

```py

```

### [상미](./동전%20분배/상미.py)

```py

```

### [서희](./동전%20분배/서희.py)

```py

```

### [성구](./동전%20분배/성구.py)

```py

```

</div>
</details>
<br><br><br>
