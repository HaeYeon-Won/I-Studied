"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
"""
from collections import deque
def printQue(q):
    for i in q:
        print(i, end = " ")
        
def solution():
    if len(q)==m: #정해진 길이가 되면 해당 수 출력
        printQue(q)
        return
    for i in range(1, n+1):
        if i not in q: #중복허용 방지 조건
            q.append(i)
            solution()
            q.pop()

if __name__ =="__main__":
    n,m = map(int, input().split())
    q = deque()
    solution()

    """
    permutation
순열이란 몇 개를 골라 순서를 고려해 나열한 경우의 수를 말한다. 즉, 서로 다른 n 개 중 r 개를 골라 순서를 정해 나열하는 가짓수이며 순열이라는 의미의 영어 ‘Permutation’의 첫 글자 P를 따서 nPr로 표시한다. 출처 : [네이버 지식백과] 순열 [Permutation, 順列] (두산백과)

순열은 순서를 고려하기 때문에 [A, B, C]의 리스트에서 2개의 원소를 골라 순서를 정해 나열하면
[(A, B), (A, C), (B, A), (B, C), (C, A), (C, B)] 가 나오게 된다. 즉 순열에서는 (A, B)와 (B, A)는 다른 것이다.

import itertools

arr = ['A', 'B', 'C']
nPr = itertools.permutations(arr, 2)
print(list(nPr))

결과 : [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
    """
