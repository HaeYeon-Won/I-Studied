"""
- Project : [14890]경사로
- 코딩테스트 연습, 시뮬레이션
- https://www.acmicpc.net/problem/14890
- Author : Hae-Yeon-Won
- Date of last update : 2022.03.29.
"""
def runway(l, way):
    # 길을 지나갈 수 있으려면 길에 속한 모든 칸의 높이가 모두 같아야 한다.
    # 또는, 경사로를 놓아서 지나갈 수 있는 길을 만들 수 있다. 경사로는 높이가 항상 1이며, 길이는 L이다.
    accumulate = 1 #중복적으로 나오는 횟수
    before = way[0] # 직전 높이
    i=1
    runway = [0]*(len(way)) #경사로 설치 위치
    while i!=len(way):
        now = way[i]#현재 높이
        if now==before and runway[i-1]!=1:#직전에 경사로 설치 x , 직전이랑 현재 높이가 같으면
            accumulate+=1#누적 +1
        else:
            diff = now-before #높이차이
            if abs(diff)>=2: return False #높이차이 2이상 => 경사로 못놓음
            if diff==1: #지금까지 쌓아온걸 보면됨(올라가는형태)
                if accumulate<l: #지금까지 쌓은양이 경사로 길이보다 짧으면 경사로 못놈
                    return False
                count=1 #경사로 놓을 수 있는 땅 숫자
                if runway[i-1]==1: #now 직전에 경사로 이미 있으면 경사로 못놓음
                    return False
                for j in range(i-1, i-2-l, -1): #지금 위치 직전에서 경사로 길이까지 반복
                    if count==l: # 경사로 충분히 쌓을 수 있으면 break
                        break
                    if runway[j]==1: # 만약 경사로 길이 안됐는데 경사로 있으면 거긴 못놓으니까 return False
                        return False
                    count+=1
                    
            elif diff==-1: #다음껄 봐야함(내려가는형태)
                if len(way)-i<l: #남아있는칸이 경사로 길이보다 짧으면 못놓음
                    return False
                else:
                    count = 1
                    #이경우는 before -> now로 내려가는 형태
                    runway[i]=1 #일단 지금위치에 경사로 설치
                    for j in range(i+1, len(way)): #설치한 뒤부터 봄
                        if count==l: # 경사로 조건 충족
                            i=j-1 #이렇게 안하면 while loop 마지막 i+1때문에 하나 건너고 진행해버림
                            break
                        if way[j]==now: #높이가 계속 같은 경우 count+1
                            count+=1
                        else: # 아직 설치할 충분한 길이가 안됐는데 높이가 달라지면 설치 못함
                            return False
                        runway[j]=1 # 경사로

            accumulate=1 # 경사로 다 깔았으니까 경사로 설치 다음 부터 다시 시작
        before = now
        i+=1

    return True

def reverse(data):#행과 열을 변경하는 함수
    return list(map(list, zip(*data)))

def solution(n,l,data):
    answer = 0
    for d in data:
        if runway(l, d):
            answer+=1
    data = reverse(data)
    for d in data:
        if runway(l, d):
            answer+=1
    return answer


if __name__ =="__main__":
    n, l = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(n)]
    print(solution(n,l,data))
