"""
n, 배열을 입력으로 받음
3 ≤ n ≤ 29
1 ≤ 주어지는 숫자 ≤ 10

입력 예시
5
1 2 2 1 2
2 2 2 2 2
2 2 1 3 1
1 2 1 1 2
2 2 1 2 2



1. 초기 예술 점수
2. 반시계 회전
3. 1회전 후 예술 점수
4. 반시계 회전
5. 2회전 후 예술 점수
6. 반시계 회전
7. 3회전 후 예술 점수

=> 결과

회전은 init 할때 좌표 미리 나누어 놓으면 편할 듯
ex. center좌표 => n//2, n//2 를 기준으로 center 구하고 이거 기준으로 나머지 4가지 사격형 구분

예술 점수 계산 전 그룹을 나누는 함수도 만들어야 함
여기서 각 그룹의 정보를 담고있으면 너무 메모리를 많이 먹을거같은데
각 그룹은 순열 형태로 묶여야 함 (1,2), (2,1) 은 같은것이므로
"""
from collections import deque
from copy import deepcopy
def getCrossPos(size, mtrx):
    result = set()
    for r in range(0, size):
        result.add((r, size//2))
    for c in range(0, size):
        result.add((size//2, c))
    return result

def rotate(n, mtrx, crossPos):
    #원본 배열 복사본 생성 (회전 시 원본배열 값 변경 방지)
    tmp_mtrx = deepcopy(mtrx)
    #1. 십자가 모양의 회전
    #02->20  [r][c] -> [n-1-c][r]
    for p in crossPos:
        mtrx[n-1-p[1]][p[0]] = tmp_mtrx[p[0]][p[1]]

    center = (n//2, n//2)

    #2. 사각형 모양의 회전
    # (1) Left Up
    """
    ##반시계
    회전 후의 열번호 -> 회전 전의 행번호
    회전 후의 행번호 -> n-1-회전 전의 열번호
    
    ##시계
    회전 후 행번호 -> 회전 전의 열번호
    회전 후 열번호 -> n-1-회전 전의 행번호
    [r][c] -> [c][n-1-r]
    """
    for r in range(center[0]):
        for c in range(center[1]):
            mtrx[c][center[0]-1-r] = tmp_mtrx[r][c]
    # (2) Right Up
    for r in range(center[0]): #03 -> 04
        for c in range(center[1]+1, n):
            mtrx[c-center[1]-1][n-1-r] = tmp_mtrx[r][c]
    # (3) Left Down
    for r in range(center[0]+1, n): #30->40
        for c in range(center[1]):
            mtrx[c+center[1]+1][n-r-1] = tmp_mtrx[r][c]
    # (4) Right Down
    for r in range(center[0]+1, n): #33->43  43->44
        for c in range(center[1]+1, n):
            mtrx[c][n-r+center[0]] = tmp_mtrx[r][c]
    return mtrx

def getGroup(n, mtrx, groups, chk_tbl, r, c, target):
    direction = ((0,1), (1,0), (0,-1), (-1,0))
    q = deque([(r,c)])
    temp = [(r,c)]
    chk_tbl[r][c]=False
    while q:
        row, col = q.popleft()
        for dx, dy in direction:
            x,y = row+dx, col+dy
            if 0<=x<n and 0<=y<n and mtrx[x][y]==target and chk_tbl[x][y]:
                q.append((x,y))
                chk_tbl[x][y] = False
                temp.append((x, y))
    groups.append(temp)
    return groups, chk_tbl

def getCombinations(n, temp, chk, start, combinations):
    if len(temp)==2:
        combinations.append((temp[0], temp[1]))
        return
    for i in range(start,n):
        if chk[i]==0:
            temp.append(i)
            chk[i]=1
            getCombinations(n,temp, chk, i+1, combinations)
            temp.pop()
            chk[i]=0


def getPoint(n, mtrx):
    direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
    chk_tbl = [[True for _ in range(n)] for _ in range(n)]
    groups = []
    numGroups = 0
    #그룹 구하기
    for r in range(n):
        for c in range(n):
            if chk_tbl[r][c]:
                groups, chk_tbl = getGroup(n, mtrx, groups, chk_tbl, r, c, mtrx[r][c])
                numGroups+=1

    #조합 구하기
    temp = deque()
    check = [0 for _ in range(numGroups)]
    combinations = deque()
    getCombinations(numGroups, temp, check, 0, combinations)
    """
    (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수 ) x 그룹 a를 이루고 있는 숫자 값 x 그룹 b를 이루고 있는 숫자 값 x 그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수
    """
    point = 0
    while combinations:
        g1, g2 = combinations.popleft()
        g1_length = len(groups[g1])
        g2_length = len(groups[g2])
        g1_val = mtrx[groups[g1][0][0]][groups[g1][0][1]]
        g2_val = mtrx[groups[g2][0][0]][groups[g2][0][1]]
        area = 0
        for x1, y1 in groups[g1]:
            for x2, y2 in groups[g2]:
                for dx, dy in direction:
                    nx, ny = x2+dx, y2+dy
                    if 0<=nx<n and 0<=ny<n and (x1, y1)==(nx, ny):
                        area+=1
        point += ((g1_length+g2_length)*g1_val*g2_val*area)

    return point

def solution(n, mtrx, crosPos):
    result = 0
    for i in range(4):
        #1. 점수 계산
        result +=getPoint(n, mtrx)
        #2. 회전
        mtrx = rotate(n, mtrx, crosPos)
    print(result)
    return

if __name__ =="__main__":
    N = int(input())
    mtrx = []
    for _ in range(N):
        mtrx.append(list(map(int, input().split())))
    crosPos = getCrossPos(N, mtrx)
    solution(N, mtrx, crosPos)
