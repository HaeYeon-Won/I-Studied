"""
n일의 휴가 동안 외주 개발을 하여 수익을 최대화 하려고 합니다. 
수행할 수 있는 외주 작업이 하루에 한 개씩 있고, 각 외주 작업은 수행 완료하는데 걸리는 기한 t와 이를 완료 했을 때의 수익 p가 주어집니다. 
두 개 이상의 외주 작업은 동시에 수행할 수 없으며, 휴가 기간 이후로는 일을 할 수 없다고 할 때 외주 수익의 최대값을 출력하는 코드를 작성해보세요.

예를 들어 n=3 이고 외주 작업이 다음과 같이 주어진 경우를 생각해봅시다.



1,2번 외주를 같이 하게 된다면 일해야하는 기간이 겹치게 되어 불가능합니다.

1,3번 외주를 같이 하게 된다면 겹치지 않게 일을 할 수 있고, 총 25 만큼의 돈을 얻게 됩니다.

2번 외주만 하게 된다면 26 만큼의 돈을 얻게 됩니다.
"""
def solution(n,data,idx, time, prev, cash):
    global result
    if time>=n:
        if time>n:
            cash-=prev
        result = max(result, cash)
        return
    for i in range(idx, n):
        if time-1<i:
            solution(n,data,i+1,i+data[i][0], data[i][1], cash+data[i][1])
    
if __name__=="__main__":
    result = 0
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))
    solution(n,data, 0, 0, 0, 0)
    print(result)