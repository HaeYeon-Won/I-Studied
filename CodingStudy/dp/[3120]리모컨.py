"""
- Project : 3120 : 리모컨
- dp
- https://codeup.kr/problem.php?id=3120
- Author : Hae-Yeon-Won
- Date of last update : 2022.04.05.
"""
def solution(now, target):
    diff = now - target
    result = 0
    if diff==0:
        return 0
    elif diff>0: #빼야하는 경우
        while diff//10 !=0:
            diff-=10
            now-=10
            result+=1
        if diff>=8:
            return result+(11-diff) #9도 => -10도 + 1도, 8도 -10도 +1도 +1도

        while diff//5!=0:
            diff-=5
            now-=5
            result+=1
        if diff==4: #+5-1
            result+=2
        else:
            result+=diff
    else:
        diff*=-1
        while diff // 10 != 0:
            diff -= 10
            now += 10
            result += 1
        if diff>=8:
            return result+(11-diff) #9도 => -10도 + 1도, 8도 -10도 +1도 +1도
        while diff // 5 != 0:
            diff -= 5
            now += 5
            result += 1
        if diff == 4: #+5 -1
            result += 2
        else:
            result += diff
    return result

if __name__ =="__main__":
    now, target = map(int, input().split())
    print(solution(now, target))
