'''
차량 번호가 작은 자동차부터 요금 출력
누적으로 계산
fees
[ 기본시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원) ]
records
시간 기준 오름차순
'''
from collections import defaultdict # default 값 지정해주는 것(여기서는 기본시간?)

def solution(fees, records):
    answer = []
    return answer