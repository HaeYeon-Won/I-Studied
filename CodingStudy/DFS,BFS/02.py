from collections import deque
def BFS(graph, start, visited):
    #큐 구현을 위해 deque 라이브러리 이용
    q=deque([start])
    #현재노드를 방문처리하기 위해사용
    visited[start]=True
    #큐가 빌때까지 반복
    while q:
        #큐에서 하나의 원소를 뽑아 출력
        now = q.popleft()
        print(now, end = " ")
        #해당 원소와 연결된 아직 방문하지않은 원소들을 큐에 삽입
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i]=True
#예제 입력
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * 9
BFS(graph, 1, visited)

#실행 결과
# 1 2 3 8 7 4 5 6
