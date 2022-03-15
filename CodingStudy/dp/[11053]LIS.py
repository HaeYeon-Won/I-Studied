"""
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.
"""
def binary_search(n, arr, target):
    start, end = 0, n-1
    while start<end:
        mid = (start+end)//2
        if arr[mid]<target:
            start=mid+1
        else:
            end=mid #mid 포함 왼쪽 (target과 같은게 없을 때 큰수중 가장 작은값을 위해)
    return end

def solution(n, data):
    result=[]
    LIS = [[] for _ in range(n)]
    result.append(data[0])
    for i in range(1,n):
        if result[-1]<data[i]:
            result.append(data[i])
        else:#같을때에는 어차피 서치하면 result안에서 해당 위치로 치환되기 때문에 문제없음
            idx = binary_search(len(result), result, data[i])  # 이분탐색하여 해당 숫자가 어디에 들어갈지 결정
            result[idx] = data[i]
    return len(result)



if __name__=="__main__":
    n=int(input())
    data = list(map(int,input().split()))
    print(solution(n, data))
