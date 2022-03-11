"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.
"""
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
    
"""
combination
조합이란 서로 다른 n개 중에서 r개(n≥r) 취하여 조를 만들 때, 이 하나하나의 조를 n개 중에서 r개 취한 조합이라고 한다. 출처 : [네이버 지식백과] 조합 (두산백과)

조합은 순서를 고려하지 않기 때문에 [A, B, C]의 리스트에서 2개의 원소를 골라 나열하면
[(A, B), (A, C), (B, C)] 가 나오게 된다. 조합은 (A, B)와 (B, A)는 같은 것으로 취급한다.

import itertools

arr = ['A', 'B', 'C']
nCr = itertools.combinations(arr, 2)
print(list(nCr))

결과 : [('A', 'B'), ('A', 'C'), ('B', 'C')]
"""
