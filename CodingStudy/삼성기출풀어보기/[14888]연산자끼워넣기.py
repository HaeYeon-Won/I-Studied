"""
- Project : [14888]연산자 끼워넣기
- 코딩테스트 연습, 시뮬레이션
-https://www.acmicpc.net/problem/14888
- Author : Hae-Yeon-Won
- Date of last update : 2022.03.30.
"""
from collections import deque
def solution(n, q, operator, check, data):
    global P, minVal, maxVal
    if (len(q) == n-1):
        result = data[0]
        for i in range(n-1):
            if q[i]==0: result = result + data[i+1]
            elif q[i]==1: result = result - data[i+1]
            elif q[i]==2: result = result * data[i+1]
            elif q[i] == 3: result = int(result/data[i+1])
        if result>maxVal: maxVal = result
        if result<minVal: minVal = result
        #P.add(tuple(q))
        return

    for i in range(len(operator)):
        if check[i]==True:
            continue
        q.append(operator[i])
        check[i]=True
        permutation(n,q,operator,check, data)
        q.pop()
        check[i]=False

if __name__ == "__main__":
    n= int(input())
    data = list(map(int, input().split()))
    temp = list(map(int, input().split()))
    operator = deque()
    for i in range(4):
        for _ in range(temp[i]):
            operator.append(i)
    P=set()
    maxVal, minVal = -1e9, 1e9
    q = deque()
    check=[False for _ in range(len(operator))]
    solution(n, q, operator, check, data)
    print(maxVal)
    print(minVal)
