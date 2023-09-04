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