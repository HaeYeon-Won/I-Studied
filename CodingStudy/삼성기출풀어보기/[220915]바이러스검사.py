"""
바이러스의 확산을 막기 위해 총 n개의 식당에 있는 고객들의 체온을 측정하고자 합니다. 
체온을 측정하는 검사자는 검사팀장과 검사팀원으로 나뉘어집니다. 
팀장과 팀원이 검사할 수 있는 고객의 수가 다르며, 한 가게당 팀장은 오직 한 명, 팀원은 여러명 있을 수 있습니다. 
하지만 가게당 팀장 한 명은 무조건 필요합니다. 가게에 검사팀원만 존재하는 경우는 있을 수 없습니다.
 팀장이든 팀원이든 담당한 가게에 대해서만 검사합니다.
n개의 식당 고객들의 체온을 측정하기 위해 필요한 검사자 수의 최솟값을 구하는 프로그램을 작성해주세요.

입력:
5
999999 999999 999999 999999 999999
111111 5

출력:
888895
"""

def solution(n,s,p):
    result = 0
    for i in range(n):
        remain = s[i]-p[0]
        result+=1
        if remain<0:
            continue
        quotient, remainder = divmod(remain, p[1])
        if remainder==0:
            result+=quotient
        else:
            result+=(quotient+1)
    return result

if __name__=="__main__":
    num_store = int(input())
    store = list(map(int, input().split()))
    possible = list(map(int, input().split()))
    print(solution(num_store, store, possible))