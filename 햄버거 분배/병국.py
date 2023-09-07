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


