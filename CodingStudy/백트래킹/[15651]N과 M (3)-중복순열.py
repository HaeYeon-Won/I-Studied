"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
"""
from collections import deque
def printQue(q):
    for i in q:
        print(i, end = " ")
    print()
    return
def solution():
    if len(q)==m:
        printQue(q)
        return
    for i in range(1, n+1):
        q.append(i)
        solution()
        q.pop()

if __name__ =="__main__":
    n,m = map(int, input().split())
    q = deque()
    solution()

    
"""
    - 중복 순열이란?
중복 가능한 n개 중에 r개를 나열하는 경우의 수(순서 O)를 말한다.
itertools의 product 함수를 이용하여 두 개 이상의 리스트에서 모든 조합을 계산할 수도 있다.
- case1

from itertools import product

data1 = [1, 2, 3, 4]

for x in product(data1, repeat=2):
    print(x)
    
    
# 결과
(1, 1) (1, 2) (1, 3) (1, 4) (2, 1) (2, 2) (2, 3) (2, 4)
(3, 1) (3, 2) (3, 3) (3, 4) (4, 1) (4, 2) (4, 3) (4, 4)
"""
