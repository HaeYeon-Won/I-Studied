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
    before = way[0]
    i=1
    runway = [0]*(len(way))
    while i!=len(way):
        now = way[i]
        if now==before and runway[i-1]!=1:
            accumulate+=1
        else:
            diff = now-before
            if abs(diff)>=2: return False
            if diff==1: #지금까지 쌓아온걸 보면됨
                if accumulate<l:
                    return False
                count=1
                if runway[i-1]==1:
                    return False
                for j in range(i-1, i-2-l, -1):
                    if count==l:
                        break
                    if way[j]!=now and runway[j]==1:
                        return False
                    count+=1
            elif diff==-1: #다음껄 봐야함
                if len(way)-i<l:
                    return False
                else:
                    count = 1
                    runway[i]=1 #경사로
                    for j in range(i+1, len(way)):
                        if count==l:
                            i=j-1
                            break
                        if way[j]==now:
                            count+=1
                        else:
                            return False
                        runway[j]=1 # 경사로

            accumulate=1
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

    
    """
    이건좀 아닌데
    """
