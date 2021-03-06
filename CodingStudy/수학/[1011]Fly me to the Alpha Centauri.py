"""
우현이는 어린 시절, 지구 외의 다른 행성에서도 인류들이 살아갈 수 있는 미래가 오리라 믿었다.
그리고 그가 지구라는 세상에 발을 내려 놓은 지 23년이 지난 지금, 세계 최연소 ASNA 우주 비행사가 되어 새로운 세계에 발을 내려 놓는 영광의 순간을 기다리고 있다.

그가 탑승하게 될 우주선은 Alpha Centauri라는 새로운 인류의 보금자리를 개척하기 위한 대규모 생활 유지 시스템을 탑재하고 있기 때문에,
그 크기와 질량이 엄청난 이유로 최신기술력을 총 동원하여 개발한 공간이동 장치를 탑재하였다.
하지만 이 공간이동 장치는 이동 거리를 급격하게 늘릴 경우 기계에 심각한 결함이 발생하는 단점이 있어서,
이전 작동시기에 k광년을 이동하였을 때는 k-1 , k 혹은 k+1 광년만을 다시 이동할 수 있다.
예를 들어, 이 장치를 처음 작동시킬 경우 -1 , 0 , 1 광년을 이론상 이동할 수 있으나 사실상 음수 혹은 0 거리만큼의 이동은 의미가 없으므로 1 광년을 이동할 수 있으며,
그 다음에는 0 , 1 , 2 광년을 이동할 수 있는 것이다. ( 여기서 다시 2광년을 이동한다면 다음 시기엔 1, 2, 3 광년을 이동할 수 있다. )

김우현은 공간이동 장치 작동시의 에너지 소모가 크다는 점을 잘 알고 있기 때문에 x지점에서 y지점을 향해 최소한의 작동 횟수로 이동하려 한다.
하지만 y지점에 도착해서도 공간 이동장치의 안전성을 위하여 y지점에 도착하기 바로 직전의 이동거리는 반드시 1광년으로 하려 한다.

김우현을 위해 x지점부터 정확히 y지점으로 이동하는데 필요한 공간 이동 장치 작동 횟수의 최솟값을 구하는 프로그램을 작성하라.
"""

"""
from collections import deque
direction = [-1,0,1]
def solution(data):
    result = []
    start, end = data[0], data[1]-1
    q= deque()
    q.append((start+1, 1, 1)) # 현재위치, 시도횟수, 이동하는거리
    while q:
        pos, cnt, warp = q.popleft()
        if pos==end and (warp==0 or warp==1 or warp==2):
            result.append(cnt)
        for d in direction:
            w = warp+d
            p = pos+w
            if start>p or p>end or w<=0:
                continue
            else:
                q.append((p,cnt+1, w))
    return min(result)+1
"""
def solution(data):
    distance = data[1]-data[0]
    if distance==1: return 1
    elif distance==2: return 2
    start, end = 3, 4
    result=3
    step=2
    loop=1
    while True:
        if start<=distance<=end: return result #범위안에 있으면 result반환
        start=end+1 #그다음 범위의 시작값 설정
        end=end+step #시작 ~ 시작+반복주기의 값으로 설정
        result+=1
        loop+=1
        if loop==2: #매번 루프가 두번 반복되는것을 확인. 반복이후 반복주기가 1씩 증가하는것을 확인하였다
            loop=0
            step+=1 #루프가 종료된 후 반복주기 하나 증가


if __name__ =="__main__":
    case = int(input())
    for _ in range(case):
        data = list(map(int, input().split()))
        print(solution(data))

"""
예제 입력
3
0 3
1 5
45 50

예제 출력
3
3
4

알고리즘이라고 할것은 딱히 없고 반복되는 패턴을 찾기가 까다로운 문제
처음 시도에는 BFS방식으로 타당성을 검증하며 q에 값을 추가해주는 방식을 사용 => 메모리 초과로 실패
이후 패턴을 찾기 위해 직접 손으로 적어본 결과는 다음과 같음

이동거리
식
이동횟수 순으로 표기

1
1
1

2
1+1
2

3
1+1+1
3

4
1+2+1
3

5
1+2+1+1
4

6
1+2+2+1
4

7
1+2+2+1+1
5

8
1+2+2+2+1
5

9
1+2+3+2+1
5

10
1+2+3+2+1+1
6

11
1+2+3+2+2+1
6

12
1+2+3+3+2+1
6

13
1+2+3+3+2+1+1
7

14
1+2+3+3+2+2+1
7

15
1+2+3+3+3+2+1
7

16
1+2+3+4+3+2+1
7

17
1+2+3+4+3+2+1+1
8

18
1+2+3+4+3+2+2+1
8

19
1+2+3+4+3+3+2+1
8

20
1+2+3+4+4+3+2+1
8

21
1+2+3+4+4+3+2+1+1
9

22
1+2+3+4+4+3+2+2+1
9

23
1+2+3+4+4+3+3+2+1
9

24
1+2+3+4+4+4+3+2+1
9

25
1+2+3+4+5+4+3+2+1
9

26
1+2+3+4+5+4+3+2+1+1
10

"""
