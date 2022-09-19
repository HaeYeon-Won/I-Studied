#https://www.codetree.ai/frequent-problems/rounding-eight-angle/description
#각 지역은 12시 방향부터 시계 방향 순서대로 공백없이 주어지며, 0은 북쪽 지방, 1은 남쪽 지방을 의미합니다.
from collections import deque
def init(pos):
    result = []
    for p in pos:
        result.append(int(p))
    return result

def getRotate_direction(target, direction):
    rotate_direction = [0,0,0,0]
    rotate_direction[target]=direction
    for left in range(target, 0, -1):
        if data[left][6]!=data[left-1][2]:
            rotate_direction[left-1]=-rotate_direction[left]
        else:
            break
    for right in range(target, 3):
        if data[right][2]!=data[right+1][6]:
            rotate_direction[right+1]=-rotate_direction[right]
        else:
            break
    return rotate_direction
    

def solution(plan, data):
    result = 0
    for p in plan:
        rotate_directin = getRotate_direction(p[0]-1, p[1])
        for i in range(len(rotate_directin)):
            if rotate_directin[i]==0: continue
            data[i].rotate(rotate_directin[i])
    for table in range(4):
        result+=((2**table)*data[table][0])
    return result
        

if __name__=="__main__":
    data = []
    for _ in range(4):
        pos = input()
        pos = init(pos)
        data.append(deque(pos))
    k = int(input())
    plan = []
    for _ in range(k):
        plan.append(list(map(int, input().split()))) #의자번호, 방향
    print(solution(plan, data))
