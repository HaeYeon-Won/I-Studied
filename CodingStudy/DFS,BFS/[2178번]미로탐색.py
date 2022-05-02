from collections import deque
def init(n,m,data):#문자열을 정수로 변환한 리스트 만들기
    result = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp. append(int(data[i][j]))
        result.append(temp)
    return result

def solution(n,m,data):
    direction = ((1,0),(0,1),(-1,0),(0,-1))
    q = deque([(0,0)])
    data = init(n,m,data)
    while q:
        row, col = q.popleft()
        for dy, dx in direction:
            y, x = row+dy, col+dx
            if 0<=y<n and 0<=x<m:
                if data[y][x]==1: #가보지 않은 방향만 이동
                    q.append((y,x))
                    data[y][x] = data[row][col]+1 #이전 깊이+1
    print(data[n-1][m-1])


if __name__ =="__main__":
    n,m = map(int, input().split())
    data = [list(input()) for _ in range(n)]
    solution(n,m,data)
