def tornado(d, data, pos):
    global result
    direction = ((0, -1), (1, 0), (0, 1), (-1, 0))  # 서 남 동 북
    case = \
        (
            ((1,0,0.01),(-1,0,0.01),(0,-3,0.05),(-1,-1,0.07),(1,-1,0.07),(-2,-1,0.02),(2,-1,0.02),(1,-2,0.1),(-1,-2,0.1)), #서
            ((0,1,0.01),(0,-1,0.01),(3,0,0.05),(1,-1,0.07),(1,1,0.07),(1,-2,0.02),(1,2,0.02),(2,-1,0.1),(2,1,0.1)), #남
            ((1,0,0.01),(-1,0,0.01),(0,3,0.05),(1,1,0.07),(-1,1,0.07),(2,1,0.02),(-2,1,0.02),(1,2,0.1),(-1,2,0.1)), #동
            ((0,1,0.01),(0,-1,0.01),(-3,0,0.05),(-1,-1,0.07),(-1,1,0.07),(-1,2,0.02),(-1,-2,0.02),(-2,1,0.1),(-2,-1,0.1))  #북
        )
    a = ((0,-2),(2,0),(0,2),(-2,0)) # 서 남 동 북
    new_pos = [pos[0]+direction[d][0], pos[1]+direction[d][1]]
    send = data[new_pos[0]][new_pos[1]]
    data[new_pos[0]][new_pos[1]]=0
    total = 0
    for c in case[d]:
        row, col = pos[0]+c[0], pos[1]+c[1]
        s = int(send*c[2])
        if 0<=row<n and 0<=col<n:
            data[row][col] += s
        else:
            result+=s
        total+=s
    row, col = pos[0]+a[d][0], pos[1]+a[d][1]
    if 0 <= row < n and 0 <= col < n:
        data[pos[0]+a[d][0]][pos[1]+a[d][1]] += (send-total)
    else:
        result += (send-total)
    return new_pos
def solution(n, data):
    """
    시행 횟수는 2번씩 이동거리는 1씩 증가 (1,1 2,2 3,3 4,4 5,5...)
    size = n 일때 n-1번쨰는 같은 이동 거리를 3번 반복을 한다
    size = n 일때 최대로 이동하는 거리는 n-1
    """
    loop=2
    round=0
    d=0 # 초기 이동방향은 서쪽
    pos = [n//2, n//2]
    for i in range(1, n): #size = n 일때 최대로 이동하는 거리는 n-1
        if i ==n-1:
            loop=3
        for _ in range(loop):
            d = round % 4
            for _ in range(i):
                pos = tornado(d, data, pos)
            round+=1

if __name__=="__main__":
    n=int(input()) #n은 홀수
    data=[list(map(int, input().split())) for _ in range(n)]
    result = 0
    solution(n, data)
    print(result)
