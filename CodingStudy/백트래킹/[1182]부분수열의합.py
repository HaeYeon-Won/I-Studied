"""
N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.
"""
def Valid(stack):
    if sum(stack)==s: return True
    return False
def solution(start, numTarget):
    global result
    if len(stack)==numTarget:
        if Valid(stack):
            result+=1
        return
    for i in range(start, n):
        stack.append(data[i])
        solution(i+1, numTarget)
        stack.pop()

if __name__ =="__main__":
    n,s = map(int, input().split())
    data = list(map(int,input().split()))
    result=0
    stack=[]
    for i in range(1, n+1):
        solution(0,i)
    print(result)

"""
백트래킹으로 조합을 만든후 값을 계산하여 내가 원하는 값과 같다면 result를 하나씩 증가시켰다.
속도를 증가시킬 수 있는 방법이 있을까?
"""
