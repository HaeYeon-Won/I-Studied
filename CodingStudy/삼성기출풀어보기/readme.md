## 정리중


## 회전변환 기본
![image](https://user-images.githubusercontent.com/73468962/160547113-7efe652d-41ee-4636-b010-40dab8383ce2.png)
![image](https://user-images.githubusercontent.com/73468962/160547141-4416b8c9-f372-4915-9343-bb16780e71c9.png)

#순열

```py
from collections import deque
def permutation():
    if len(q)==m: #정해진 길이가 되면 해당 수 출력
        printQue(q) #해당 길이 순열 완성
        return
    for i in range(1, n+1):
        if i not in q: #중복허용 방지 조건
            q.append(i)
            solution()
            q.pop()
```

#순열
```py
from collections import deque
def Combination(start):
    if len(q)==m:
        printQue(q) #해당길이 조합 완성
        return
    for i in range(start, n+1):
        if i not in q: #중복 방지 조건
            q.append(i)
            solution(i+1) # 순열과 다르게 (1,2)와 (2,1)을 같은것으로 봄. 따라서 재귀마다 start를 증가시켜 중복을 피함
            q.pop()
```
