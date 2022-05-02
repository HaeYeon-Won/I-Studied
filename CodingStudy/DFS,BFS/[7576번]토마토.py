from collections import deque
def init(n,m,data):#초기 토마토 위치 파악
    result = deque()
    for i in range(n):
        for j in range(m):
            if data[i][j]==1:
                result.append((i,j))
    return result

def ans(n,m,data):
    result = 0
    for i in range(n):
        for j in range(m):
            if data[i][j]==0:
                print(-1)
                return
            result = max(result, data[i][j])
    print(result-1)
    return

def solution(n,m,data):
    direction = ((1,0),(0,1),(-1,0),(0,-1))
    q = init(n,m,data)
    while q:
        row, col = q.popleft()
        for dy, dx in direction:
            y, x = row+dy, col+dx
            if 0<=y<n and 0<=x<m:
                if data[y][x]==0: #아직 익지 않은 토마토인 경우
                    q.append((y,x))
                    data[y][x] = data[row][col]+1 #이전 깊이+1
    ans(n,m,data)

if __name__ =="__main__":
    m,n = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    solution(n,m,data)
