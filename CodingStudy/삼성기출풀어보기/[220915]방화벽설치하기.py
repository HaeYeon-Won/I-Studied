"""
n * m 크기의 이차원 영역에 방화벽을 설치하여 불로 인한 피해를 최소화 하고자 합니다. 
불은 상하좌우의 인접한 공간으로 모두 번지는 특성을 지니고 있으며, 방화벽을 뚫을 수는 없습니다. 
예를 들어 [그림 1]과 같이 불과 방화벽이 배치되어 있을 경우, 불이 모두 번지고 난 후에는 [그림 2]와 같은 상태로 변하게 됩니다. 
기존에 이미 설치되어 있는 방화벽을 제외하고 추가로 3개의 방화벽을 설치할 수 있을 때 
정확히 3개의 방화벽을 추가로 설치하여 불이 퍼지지 않는 영역이 최대일 때의 크기를 출력하는 코드를 작성해보세요.

 단, 방화벽을 불이 있는 위치에 설치할 수는 없습니다.
"""
from collections import deque
from copy import deepcopy
def init(n,m,data):
    fire = []
    for i in range(n):
        for j in range(m):
            if data[i][j]==2:
                fire.append((i,j))
    return fire

def BFS(data, fire):
    ans = 0
    direction = ((1,0),(0,1),(-1,0),(0,-1))
    q = deque()
    for i in range(len(fire)):
        q.append(fire[i])
    while q:
        row, col = q.popleft()
        for dx, dy in direction:
            x,y = row+dx, col+dy
            if 0<=x<n and 0<=y<m and data[x][y]==0:
                data[x][y]=1
                q.append((x,y))
    for i in data:
        ans+=i.count(0)
    return ans

def solution(n ,m, data, fire, wall):
    global result
    if wall == 3:
        result = max(result, BFS(deepcopy(data), fire))
        return
    for r in range(n):
        for c in range(m):
            if data[r][c]==0:
                data[r][c]=1
                solution(n,m,data,fire,wall+1)
                data[r][c]=0

if __name__=="__main__":
    result = 0
    n,m = map(int, input().split())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))
    fire = init(n,m,data)
    solution(n,m,data, fire, 0)
    print(result)