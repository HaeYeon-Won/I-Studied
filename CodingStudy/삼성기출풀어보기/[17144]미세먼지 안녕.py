"""
- Project : [17144번]미세먼지 안녕!
- 코딩테스트 연습, 시뮬레이션
- Author : Hae-Yeon-Won
- Date of last update : 2022.03.27.
"""
from collections import deque
def init(R,C,arr):
    AirCleaner = []
    for r in range(R):
        for c in range(C):
            if arr[r][c]==-1:
                AirCleaner.append((r,c))
    return AirCleaner

def solution(R, C, T, arr):
    direction = ((0,1),(0,-1),(1,0),(-1,0))
    AirCleaner = init(R,C,arr)
    round = 0
    while round!=T:
        #1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
        temp = [[0 for _ in range(C)] for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if arr[r][c]>0:
                    spread = 0
                    #1_1 (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
                    for dx, dy in direction:
                        x,y = r+dx, c+dy
                        #1_2 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
                        if 0 <= x < R and 0 <= y < C and arr[x][y] != -1:
                            #1_3 확산되는 양은 Ar,c/5이고 소수점은 버린다.
                            temp[x][y] += (arr[r][c] // 5)
                            spread += (arr[r][c] // 5)
                            #1_4 (r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.
                    arr[r][c] -= spread
        #확산된거 처리
        for i in range(R):
            for j in range(C):
                arr[i][j]+=temp[i][j]
                
        #2. 공기청정기가 작동한다.
        #위쪽 공기청정기
        #오른쪽 회전, 위로 회전, 왼쪽 회전, 아래로 회전
        AirUp = ((0,1),(-1,0),(0,-1),(1,0))
        mv=0#움직이는 방향
        uq= deque([[AirCleaner[0][0], AirCleaner[0][1]+1, arr[AirCleaner[0][0]][AirCleaner[0][1]+1]]])
        arr[AirCleaner[0][0]][AirCleaner[0][1] + 1]=0
        while True:
            ur, uc, unow = uq.popleft()
            if ur==AirCleaner[0][0] and uc==AirCleaner[0][1]:
                break
            if ur==AirCleaner[0][0] and uc==(C-1): #위로 꺾어 올라가는 부분
                mv+=1
            elif ur==0 and uc==(C-1): #왼쪽으로 꺾는 부분
                mv+=1
            elif ur==0 and uc==0: #아래로 꺾는 부분
                mv+=1
            ux,uy = ur+AirUp[mv][0], uc+AirUp[mv][1]
            uq.append([ux,uy, arr[ux][uy]])
            arr[ux][uy]=unow
        arr[AirCleaner[0][0]][AirCleaner[0][1]]=-1
        
        #아래쪽 공기청정기
        #오른쪽 회전, 아래로 회전, 왼쪽회전, 위로 회전
        AirDown = ((0, 1), (1, 0), (0, -1), (-1, 0))
        mv = 0  # 움직이는 방향
        dq= deque([[AirCleaner[1][0], AirCleaner[1][1]+1, arr[AirCleaner[1][0]][AirCleaner[1][1]+1]]])
        arr[AirCleaner[1][0]][AirCleaner[1][1] + 1]=0
        while True:
            dr, dc, dnow = dq.popleft()
            if dr == AirCleaner[1][0] and dc == AirCleaner[1][1]:
                break
            if dr == AirCleaner[1][0] and dc == (C - 1):  # 아래로 꺾는 부분
                mv += 1
            elif dr == (R-1) and dc == (C - 1):  # 왼쪽으로 꺾는 부분
                mv += 1
            elif dr == (R-1) and dc == 0:  # 위로 꺾는 부분
                mv += 1
            dx, dy = dr + AirDown[mv][0], dc + AirDown[mv][1]
            dq.append([dx, dy, arr[dx][dy]])
            arr[dx][dy] = dnow
        arr[AirCleaner[1][0]][AirCleaner[1][1]] = -1
        round+=1

    result = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j]>0:
                result+=arr[i][j]

    return result

if __name__ =="__main__":
    R,C,T = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(R)]
    print(solution(R, C, T, arr))
