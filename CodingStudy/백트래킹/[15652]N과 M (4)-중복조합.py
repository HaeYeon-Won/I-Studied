"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
"""
from collections import deque
def printQue(q):
    for i in q:
        print(i, end = " ")
    return
def solution(start):
    if len(q)==m:
        printQue(q)
        return
    for i in range(start, n+1):
        q.append(i)
        solution(i)
        q.pop()

if __name__ =="__main__":
    n,m = map(int, input().split())
    q = deque()
    solution(1)

    

"""
     중복 조합이란?
중복 가능한 n개 중에 r개를 선택하는 경우의 수(순서 X)를 말한다.
- combinations_with_replacement 함수를 이용한 코드 구현

from itertools import combinations_with_replacement

data = [1, 2, 3, 4]

for x in combinations_with_replacement(data, 2):
    print(x, end=" ")


# 결과
(1, 1) (1, 2) (1, 3) (1, 4) (2, 2) (2, 3) (2, 4) (3, 3) (3, 4) (4, 4)
"""
