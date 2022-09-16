"""
n개의 정수가 순서대로 주어질 때, n-1개의 연산자를 정수 사이에 하나씩 배치하고자 합니다. 
이 때 주어진 정수의 순서를 바꿀 수 없으며, 연산자는 덧셈, 뺄셈, 곰셈 이렇게 세 가지 종류가 있습니다.
연산자 간의 우선 순위를 무시하고 앞에서부터 차례대로 연산한다고 하였을 때, 
가능한 식의 최솟값과 최댓값을 출력하는 코드를 작성해보세요.
"""
from collections import deque
def init(op):
    ops = [1, -1, 0]
    result  = []
    for i in range(3):
        for j in range(op[i]):
            result.append(ops[i])
    return result

def getValue(data, op):
    result = data[0]
    for i in range(1, len(data)):
        if op[i-1]==1: result+=data[i]
        elif op[i-1]==-1: result-=data[i]
        elif op[i-1]==0: result*=data[i]
    return result

def solution(n, data, ops, op, check, count):
    global minVal, maxVal
    if count==n-1:
        val = getValue(data, op)
        minVal = min(minVal, val)
        maxVal = max(maxVal, val)
        return
    for i in range(n-1):
        if not check[i]:
            op.append(ops[i])
            check[i]=True
            solution(n,data,ops, op, check, count+1)
            op.pop()
            check[i]=False
    return


if __name__=="__main__":
    minVal, maxVal = 1e9, -1e9
    n = int(input())
    data = list(map(int, input().split()))
    operator = list(map(int, input().split()))
    operators = init(operator)
    check = [False] * (len(operators))
    op = deque()
    solution(n, data, operators, op, check, 0)
    print(minVal, maxVal)