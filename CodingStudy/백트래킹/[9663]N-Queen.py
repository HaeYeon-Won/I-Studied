"""
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
"""
def isValid(locate):
    for i in range(locate[0]):
        if table[i]==locate[1] or abs(i-locate[0])==abs(table[i]-locate[1]):
            #같은 열상에 있거나
            return False
    return True

def solution(round,table):
    global answer
    if round==n:
        answer+=1
        return
    else:
        for col in range(n):
            if isValid((round, col)):
                table[round]=col
                solution(round+1, table)

if __name__ =="__main__":
    n= int(input())
    table = [-1 for _ in range(n)]
    answer = 0
    solution(0,table)
    print(answer)
