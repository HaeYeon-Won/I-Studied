from collections import deque
def solution():
    if len(q)==m:
        print(" ".join(map(str, q)))
        return
    for i in range(1, n+1):
        if i not in q:
            q.append(i)
            solution()
            q.pop()

if __name__ =="__main__":
    n,m = map(int, input().split())
    q = deque()
    solution()
