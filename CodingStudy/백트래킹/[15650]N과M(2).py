from collections import deque
def solution(start):
    if len(q)==m:
        print(" ".join(map(str, q)))
        return
    for i in range(start, n+1):
        if i not in q:
            q.append(i)
            solution(i+1)
            q.pop()

if __name__ =="__main__":
    n,m = map(int, input().split())
    q = deque()
    solution(1)
