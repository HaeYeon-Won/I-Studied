
#  1. 자료형
### 수 자료형
- 정수형 : int()
- 실수형 : float()
- INF(무한)을 표현할 때 1e9(10억)으로 보통 사용하면 무방
### 리스트
- 리스트 슬라이싱
```python
a = [1,2,3,4,5,6,7,8,9]
print(a[1:4])
> 출력 : [2,3,4]
```
- 리스트 컴프리헨션
```python
a = [i for i in range(10) if i%2==1]
print(a)
> 출력 : [1,3,5,7,9]
```
2차원 리스트를 초기화 할때는 반드시 리스트 컴프리헨션을 이용해야한다!

- 리스트 관련 기타 메서드

|메서드명|사용법|설명|시간복잡도|
|:----:|:---|:---:|:---:|
|append()|리스트.append(추가할 내용)|리스트에 원소 삽입|O(1)|
|sort()|리스트.sort(), 리스트.sort(reverse=True)|리스트 정렬|O(NlogN)|
|reverse()|리스트.reverse()|리스트 원소 뒤집기|O(N)|
|insert()|리스트.insert(삽입할 위치)|리스트 특정위치에 값 삽입|O(N)|
|count()|리스트.count(특정값)|리스트안의 특정값 개수|O(N)|
|remove()|리스트.remove(특정값)|특정값 제거, 여러개면 하나만|O(N)|

### 사전 자료형
```python
data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['코코넛'] = 'coconut'

print(data)
> 출력 : {'사과' : apple, . . ., '코코넛' : 'coconut}
```
- 사전자료형 관련 함수
```python
data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['코코넛'] = 'coconut'

key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)
> 출력 :
> dict_keys(['사과'], ['바나나'], ['코코넛'])
> dict_values(['apple', 'banana', 'coconut'])
```

### 집합 자료형
- 중복을 허용하지 않는다.
- 순서가 없다.
```python
data = set([1,1,2,3,4,4,5])
print(data)
a = set([1,2,3,4,5])
b = set([3,4,5,6,7])
print(a|b) # 합집합
print(a&b) # 교집합
print(a-b) # 차집합
> 출력 :
> {1,2,3,4,5} #집합자료형 선언
> {1,2,3,4,5,6,7} #합집합
> {3,4,5} #교집합
> {1,2} #차집합
```

- 집합자료형 관련 함수

|메서드명|사용법|설명|시간복잡도|
|:----:|:---|:---:|:---:|
|add()|data.add(추가할 값)|값을 추가|O(1)|
|update()|data.update(리스트)|여러값을 한번에 대입|O(1)|
|remove()|data.remove(특정값)|특정값을 가지는 원소 제거|O(1)|

# 2. 조건문
```python
# 조건문의 기본
if 조건1:
	조건1이 True일때 실행하는 코드
elif 조건2:
	조건1이 만족하지않고, 조건2가 True일때 실행
else:
	위 모든 조건문에 부합하지 않을 시 실행 
```
