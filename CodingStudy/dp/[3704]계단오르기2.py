"""
- Project : 3704 : 계단 오르기 2
- dp
- https://codeup.kr/problem.php?id=3704
- Author : Hae-Yeon-Won
- Date of last update : 2022.04.07.
"""

import sys
sys.setrecursionlimit(100000)
def solution(n):
    global memo
    if n in memo:
        return memo[n]
    memo[n]=((solution(n-3)+solution(n-2)+solution(n-1)))%1000
    return memo[n]

if __name__ =="__main__":
    n = int(input())
    memo={1:1, 2:2, 3:4}
    print(solution(n))
