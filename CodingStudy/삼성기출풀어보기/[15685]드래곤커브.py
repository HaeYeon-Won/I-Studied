"""
- Project : [15685]드래곤 커브
- 코딩테스트 연습, 시뮬레이션
- https://www.acmicpc.net/problem/15685
- Author : Hae-Yeon-Won
- Date of last update : 2022.03.28.
"""
from collections import deque
def check(mtrx):
    result = 0
    for i in range(199):
        for j in range(199):
            if mtrx[i][j]==1:
                if mtrx[i+1][j] and mtrx[i][j+1] and mtrx[i+1][j+1]: #파이썬에서 0이아닌수는 다 True
                    result+=1
    return result

def rotate90(q):
    point = q[-1] #회전 시키는 기준점
    for i in range(len(q)-2,-1,-1): #중심점을 기준으로 가까운 점부터 회전
        #(a,b)를 기준으로 x,y를 회전 시키는 공식
        #sin90 = 1, cos90 = 0

        #반시계 방향 회전 변환
        #x' = (x-a) * cosR - (y-b)sinR
        #y' = (x-a) * sinR + (y-b)cosR

        #시계 방향 회전 변환
        # x' = a + ( (x-a) * cosR + (y-b) * sinR )
        # y' = b + ( -(x-a) * sinR + (y-b) * cosR )
        #ex . (3,3), (3,4)에서 (3,4) 중심 회전 => 위 식에 따라 시계방향으로 90도 회전 시키면 (2,4)가 된다.
        rotate_row, rotate_col = point[0]+(q[i][1]-point[1]), point[1]-(q[i][0]-point[0])
        q.append((rotate_row, rotate_col))
    return q

def DragonCurve(q, mtrx, generation):
    for i in range(generation):
        q = rotate90(q)
    while q: #
        row,col = q.popleft()
        mtrx[row][col]=1
    return mtrx

def solution(n, data):
    #x축 = col, y축 = row
    #0: x좌표가증가하는방향(→)
    #1: y좌표가감소하는방향(↑)
    #2: x좌표가감소하는방향(←)
    #3: y좌표가증가하는방향(↓)
    direction = ((0,1),(-1,0),(0,-1),(1,0))
    mtrx = [[0 for _ in range(200)] for _ in range(200)] #점을 확장 시키면 하나의 grid로 볼 수 있음
    for i in data:
        q=deque()
        start_row, start_col, d, g = i[1], i[0], i[2], i[3] #x축 = col, y축 = row
        next_row, next_col = start_row+direction[d][0], start_col+direction[d][1] #여기까지 0세대
        q.append((start_row, start_col))
        q.append((next_row, next_col))
        mtrx = DragonCurve(q, mtrx, g)

    return check(mtrx)


if __name__ == "__main__":
    n= int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    print(solution(n,data))
