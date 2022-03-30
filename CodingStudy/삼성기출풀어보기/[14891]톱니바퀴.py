"""
- Project : [14891]톱니바퀴
- 코딩테스트 연습, 시뮬레이션
-https://www.acmicpc.net/problem/14891
- Author : Hae-Yeon-Won
- Date of last update : 2022.03.30.
"""
from collections import deque
def init(temp):
    data = []
    for t in temp:
        q = deque()
        for d in t:
            q.append(int(d))
        data.append(q)
    return data

def state(data):
    return sum([data[0][0]*1, data[1][0]*2, data[2][0]*4, data[3][0]*8])
def rotate(data, target, d):
    left, right = 6, 2
    temp_d = d #d값 저장
    nowL, nowR = data[target][left], data[target][right]
    data[target].rotate(d)#돌리기
    for i in range(target+1, 4): # 오른쪽
        d *=-1
        if nowR != data[i][left]:
            nowR = data[i][right]
            data[i].rotate(d)
        else:
            break
    d = temp_d
    for i in range(target-1, -1, -1):
        d *= -1
        if nowL != data[i][right]:
            nowL = data[i][left]
            data[i].rotate(d)
        else:
            break
    return data

def solution(data, plan):
    for p in plan:
        target, d = p[0]-1, p[1]
        data = rotate(data, target, d)
    return state(data)

if __name__ =="__main__":
    #N극은 0, S극은 1, 12시 부터 시계방향으로 주어짐
    data = [input() for _ in range(4)]
    data = init(data)
    k=int(input())
    plan = [list(map(int, input().split())) for _ in range(k)] #1은 시계, -1은 반시계 회전
    print(solution(data, plan))

