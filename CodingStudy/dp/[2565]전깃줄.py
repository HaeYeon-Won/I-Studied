"""
두 전봇대 A와 B 사이에 하나 둘씩 전깃줄을 추가하다 보니 전깃줄이 서로 교차하는 경우가 발생하였다.
합선의 위험이 있어 이들 중 몇 개의 전깃줄을 없애 전깃줄이 교차하지 않도록 만들려고 한다.

예를 들어, < 그림 1 >과 같이 전깃줄이 연결되어 있는 경우 A의 1번 위치와 B의 8번 위치를 잇는 전깃줄,
A의 3번 위치와 B의 9번 위치를 잇는 전깃줄, A의 4번 위치와 B의 1번 위치를 잇는 전깃줄을 없애면 남아있는 모든 전깃줄이 서로 교차하지 않게 된다.



< 그림 1 >

전깃줄이 전봇대에 연결되는 위치는 전봇대 위에서부터 차례대로 번호가 매겨진다.
전깃줄의 개수와 전깃줄들이 두 전봇대에 연결되는 위치의 번호가 주어질 때,
남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 구하는 프로그램을 작성하시오.
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
    result.append(data[0][1])
    for i in range(1,n):
        if result[-1]<data[i][1]:
            result.append(data[i][1])
        else:
            idx = binary_search(len(result), result, data[i][1])  # 이분탐색하여 해당 숫자가 어디에 들어갈지 결정
            result[idx] = data[i][1]

    return n-len(result)



if __name__=="__main__":
    n=int(input())
    data = [list(map(int,input().split()))for _ in range(n)]
    data = sorted(data, key=lambda x:x[0])
    print(solution(n, data))
