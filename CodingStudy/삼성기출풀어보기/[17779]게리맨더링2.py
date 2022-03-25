"""

1. 기준점 (x, y)와 경계의 길이 d1, d2를 정한다.

    (d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)

2. 다음 칸은 경계선이다.

    (x, y), (x+1, y-1), ..., (x+d1, y-d1)

    (x, y), (x+1, y+1), ..., (x+d2, y+d2)

    (x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)

    (x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)

3. 경계선과 경계선의 안에 포함되어있는 곳은 5번 선거구이다.

4. 5번 선거구에 포함되지 않은 구역 (r, c)의 선거구 번호는 다음 기준을 따른다.

    1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y

    2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N

    3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2

    4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N

"""

def Division(x,y,d1,d2, data, size, population):
    result = [0 for _ in range(5)] #각 구역별 사람 수
    area = [[0 for _ in range(size)] for _ in range(size)]

    #경계 구역
    for i in range(d1+1): area[x+i][y-i]=5
    for i in range(d2+1): area[x+i][y+i]=5
    for i in range(d2+1): area[x+d1+i][y-d1+i]=5
    for i in range(d1+1): area[x+d2+i][y+d2-i]=5

    # 1번 선거구
    for r in range(x + d1):
        for c in range(y + 1):
            if area[r][c] == 5:
                break
            else:
                result[0] += data[r][c]
    # 2번 선거구
    for r in range(x+d2+1):
        for c in range(n-1, y, -1):
            if area[r][c] == 5:
                break
            else:
                result[1] += data[r][c]
    # 3번 선거구
    for r in range(x + d1, n):
        for c in range(y - d1 + d2):
            if area[r][c] == 5:
                break
            else:
                result[2] += data[r][c]
    # 4번 선거구
    for r in range(x+d2+1, n):
        for c in range(n-1, y - d1 + d2 - 1, -1):
            if area[r][c] == 5:
                break
            else:
                result[3] += data[r][c]
    # 5번 선거구
    result[4] = population - sum(result)
    return max(result) - min(result)


def solution(n ,data, population):
    #1. 기준점 (x, y)와 경계의 길이 d1, d2를 정한다.
    # (d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)
    result = []
    for x in range(n):
        for y in range(n):
            for d1 in range(1,n):
                for d2 in range(1,n):
                    if 1 <= x < x+d1+d2 <n and  1 <= y-d1 < y < y+d2 <n:
                        result.append(Division(x,y,d1,d2, data, n, population))
                    else:
                        continue
    return min(result)

if __name__=="__main__":
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    population = 0
    for d in data: population+=sum(d)
    print(solution(n,data, population))
