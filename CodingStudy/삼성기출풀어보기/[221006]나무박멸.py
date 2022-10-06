from collections import deque
def init(n, mtrx):
    for r in range(n):
        for c in range(n):
            if mtrx[r][c]==-1:
                mtrx[r][c]=inf
    return mtrx

def checkAdj(size, r,c, mtrx): #4방향을 확인하는 함수
    global d_c
    ans = 0
    for dx, dy in d_c:
        x,y = r+dx, c+dy
        if 0<=x<size and 0<=y<size and 0<mtrx[x][y]<1e9:
            ans+=1
    return ans

def grow(n, mtrx):
    for r in range(n):
        for c in range(n):
            if 0<mtrx[r][c]<1e9: # 나무 존재
                mtrx[r][c]+=checkAdj(n,r,c,mtrx) #나무 존재칸수 확인 후 성장
    return mtrx

def spread(n, mtrx):
    global d_c
    temp = [[0 for _ in range(n)] for _ in range(n)] #한 사이클에 성장하는 나무를 담는 배열(동시 처리 위함)
    for r in range(n):
        for c in range(n):
            if 0<mtrx[r][c]<1e9:
                val=mtrx[r][c]
                count = 0
                pos = deque()
                for dx, dy in d_c:
                    x,y = r+dx, c+dy
                    if 0 <= x < n and 0 <= y < n and mtrx[x][y] == 0: #빈 땅인 경우
                        pos.append((x,y))
                        count+=1
                if count!=0:
                    val=val//count
                    while pos:
                        sx, sy = pos.popleft()
                        temp[sx][sy]+=val
    #번식 완료 후 원래 배열과 합쳐주기
    for r in range(n):
        for c in range(n):
            mtrx[r][c]+=temp[r][c]

    return mtrx

def checkX(n,r,c, mtrx,k):#X자 형태로 뿌려보기
    global d_x
    result = mtrx[r][c] #초기값은 처음 고른 땅의 나무 수
    for dx, dy in d_x:
        for i in range(1, k + 1):
            x,y = r+(dx*i), c+(dy*i)
            if 0 <= x < n and 0 <= y < n: #정상 범위
                if mtrx[x][y]==1e9: #돌인경우
                    break #해당 방향은 더이상 볼 필요 없음
                elif mtrx[x][y]<=0: #빈땅 or 제초제 뿌려진 땅인 경우
                    break #마찬가지로 더 볼 필요 없음
                elif 0<mtrx[x][y]<1e9: # 나무가 있는 경우
                    result+=mtrx[x][y]
            else:
                break #정상 범위가 아니라면 루프 좀료
    return result

def getPos(n, mtrx, k):
    result = [0,0,0] #x, y, val
    for r in range(n):
        for c in range(n):
            if 0<mtrx[r][c]<1e9: #나무가 있는 위치
                val = checkX(n,r,c, mtrx,k)
                if val>result[2]:
                    result[0], result[1], result[2] = r, c, val
    return result

def process(n, r, c, mtrx, k, year):#target 지점 제초제 처리
    global d_x
    mtrx[r][c]=-year #시작칸 죽이기
    for dx, dy in d_x:
        for i in range(1, k + 1):
            x, y = r + (dx * i), c + (dy * i)
            if 0 <= x < n and 0 <= y < n:  # 정상 범위
                if mtrx[x][y] == 1e9:  # 돌인경우
                    break  # 해당 방향은 더이상 볼 필요 없음
                elif mtrx[x][y] <= 0:  # 빈땅 or 제초제 뿌려진 땅인 경우
                    mtrx[x][y]=-year #제초제만 뿌리고 break
                    break
                elif mtrx[x][y] > 0:  # 나무가 있는 경우
                    mtrx[x][y]=-year #제초제 뿌리고 계속 진행
            else:
                break  # 정상 범위가 아니라면 루프 좀료
    return mtrx

def heal(n, mtrx):
    for r in range(n):
        for c in range(n):
            if mtrx[r][c]<0:
                mtrx[r][c]+=1
    return mtrx

def solution(n,m,k,c,mtrx):
    result = 0
    #만약 c==2 고 0일때 뿌리면 2까지 남음 -> 3에 종료
    for _ in range(m):#m년 동안 반복
        #1. 나무가 성장한다
        mtrx = grow(n, mtrx)
        #2. 나무가 번식한다
        mtrx = spread(n, mtrx)
        #3. 제초제 살포 위치 선정
        targetR, targetC, val = getPos(n,mtrx,k)
        #4. 제초제를 살포한다
        mtrx = process(n,targetR, targetC, mtrx, k, c+1)
        #5. 죽은 나무의 수 합산
        result += val
        #6. 제초제 감소(여기서 할꺼라서 c+1 만큼 제초제 뿌려야함
        mtrx = heal(n, mtrx)
    return result

if __name__=="__main__":
    inf = 1e9
    d_c=((1,0), (0,1), (-1,0), (0,-1))# + 모양 direction
    d_x=((1,1), (1,-1), (-1,1), (-1,-1))# x 모양 direction
    N, M, K, C = map(int, input().split())
    mtrx = []
    for _ in range(N):
        mtrx.append(list(map(int,input().split())))
    mtrx = init(N, mtrx)
    print(solution(N,M,K,C,mtrx))
