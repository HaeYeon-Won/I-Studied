# Study 1일차

## 정리해야하는 사항 
### zip, map, join, lambda
## - zip
1. 기본사용법 
>zip() 함수는 여러 개의 순회 가능한(iterable한) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 튜플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환.
>예제 코드
>(1) zip 함수를 사용
>```py
>>> numbers = [1, 2, 3]
>>> letters = ["A", "B", "C"]
>>> for pair in zip(numbers, letters):
>>>     print(pair)
>>>
>출력 결과
>>>(1, 'A')
>>>(2, 'B')
>>>(3, 'C')

>(2) index를 사용해서 작성
>```py
>>> numbers = [1, 2, 3]
>>> letters = ["A", "B", "C"]
>>> for i in range(3):
>>>     pair = (numbers[i], letters[i])
>>>     print(pair)
>>>
>출력 결과
>>>(1, 'A')
>>>(2, 'B')
>>>(3, 'C'))

2. 병렬처리
>zip() 함수를 활용하면 여러 그룹의 데이터를 루프를 한번만 돌면서 처리가능. 가변인자를 받기 때문에 2개 이상의 인자를 넘겨서 병렬 처리 가능.
>예제 코드
>```py
>>> for number, upper, lower in zip("12345", "ABCDE", "abcde"):
>>>     print(number, upper, lower)
>출력 결과
>>>1 A a
>>>2 B b
>>>3 C c
>>>4 D d
>>>5 E e

3. unzip()
>zip() 함수로 엮어 놓은 데이터를 다시 해제
>예제 코드
>먼저  `zip()`  함수로 2개의 터플의 데이터를 엮은 후 리스트로 변환.

```py
>>> numbers = (1, 2, 3)
>>> letters = ("A", "B", "C")
>>> pairs = list(zip(numbers, letters))
>>> pairs
>>>[(1, 'A'), (2, 'B'), (3, 'C')]
```

이 리스트 앞에 풀기(unpacking) 연산자 붙여서 다시  `zip()`  함수에 넘기면 다시 원래의 2개의 터플을 얻을 수 있음.

```py
>>> numbers, letters = zip(*pairs)
>>> numbers
(1, 2, 3)
>>> letters
>>>('A', 'B', 'C')
```
4.  사전 변환
> `zip()`  함수를 이용하면 두 개의 리스트나 터플 부터 쉽게 사전(dictionary)을 만들 수 있음. 키를 담고 있는 리스트와 값을 담고 있는 리스트를  `zip()`  함수에 넘긴 후, 그 결과를 다시  `dict()`  함수에 넘기면 됨.

```py
>>> keys = [1, 2, 3]
>>> values = ["A", "B", "C"]
>>> dict(zip(keys, values))
>>>{1: 'A', 2: 'B', 3: 'C'}
```


```py
>>> dict(zip(["year", "month", "date"], [2001, 1, 31]))
>>>{'year': 2001, 'month': 1, 'date': 31}
```
## - map
1. 기본사용법 
>map(function, iterable)
- 첫 번째 매개변수로는 함수가 오고
- 두 번째 매개변수로는 반복 가능한 자료형(리스트, 튜플등)이 온다.
- map 함수의 반환값은 map 객체이므로 해당 자료형을 list 또는 tuple로 변환해야함.
- 함수의 동작은  두 번째 인자로 들어온 반복 가능한 자료형 (리스트나 튜플)을  첫 번째 인자로 들어온 함수에 하나씩 집어넣어서 함수를 수행하는  함수.

map(적용시킬 함수, 적용할 값들) 와 같다고 보면 된다. 
- 예를 들어 첫 번째 인자가 값에 +1을 더해주는 함수라고 하고 두번째 인자에 [1, 2, 3, 4, 5] 라는 리스트를 집어넣는다 가정한다.

즉
map( 값에 +1 을 더해주는 함수, [1,2,3,4,5])  
함수의 반환을 list(. )로 감싸주면  
**[2,3,4,5,6]**  이 되는 함수.

>예제 코드
```py
# 리스트에 값을 하나씩 더해서 새로운 리스트를 만드는 작업 
myList = [1, 2, 3, 4, 5] 
# for 반복문 이용 
result1 = [] for val in myList: 
	result1.append(val + 1) print(f'result1 :  {result1}') 

# map 함수 이용  
def  add_one(n):  
	return n + 1 result2 = list(map(add_one, myList)) 
	# map반환을 list 로 변환 
	print(f'result2 :  {result2}')  
  

>출력 결과
>>>result1 : [2, 3, 4, 5, 6]
>>>result2 : [2, 3, 4, 5, 6]


# map 과 lambda  # 일반 함수 이용  
def  func_mul(x):  
	return x * 2 result1 = list(map(func_mul, [5, 4, 3, 2, 1])) 
	print(f"map(일반함수, 리스트) :  {result1}") 

# 람다 함수 이용 
result2 = list(map(lambda x: x * 2, [5, 4, 3, 2, 1])) 
print(f"map(람다함수, 리스트) :  {result2}")  

>출력 결과
>>>result1 : [10, 8, 6, 4, 2]
>>>result2 : [10, 8, 6, 4, 2]
```
## - lambda
-원래 함수라는게 복잡한 명령들을 편하게 반복해서 사용할 수 있도록 모아두는 역할을 하는데, def 를 이용해서 다른곳에 함수를 만들고 그걸 또 호출해서 부르기까지의 수고가 필요하지 않은 그런 "가벼운? 함수"들을 위해서 만들어진게 람다 함수 이다.

#### **> 람다함수 선언 방법**

**lambda 인자: 표현식**

lambda 라는 키워드를 입력하고 뒤에는 매개변수(인자)를 입력하고 콜론(:)을 넣은다음에 그 매개변수(인자)를 이용한 동작들을 적으면 됩니다.  
예를 들면 인자로 들어온 값에 2를 곱해서 반환한다고 하면 lambda x : x * 2 이런식으로 됨.

#### **> 이해를 돕기위한 람다함수와 일반함수 비교**

위에서 설명했듯이 람다함수는 일반함수를 가볍게 만든 함수이기 때문에  
짝수를 판별하는 함수를 만든다고 했을때 일반함수는  
```py
def is_even(x):
	return x % 2 == 0  
이런식으로 표현을 할 수 있습니다.

이걸 람다로 표현하게 되면  
is_even = lambda x : x % 2 == 0  
이런식으로 표현할수 있습니다.

물론 일반함수, 람다함수 둘다 사용법은 같습니다.  
이런식으로 호출을 하겠죠?  
is_even(1) # False  
is_even(2) # True
```
## - join
1. join 이란?
>함수의 모양은 아래와 같음.

> **"".join(리스트)**

> **"구분자".join(리스트)**

join 함수는 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환하는 함수.

**"".join(리스트)**  
"".join(리스트)를 이용하면 매개변수로 들어온 **['a', 'b', 'c'] 이런 식의 리스트를 'abc'의 문자열로 합쳐서 반환**해주는 함수.

**"구분자".join(리스트)**  
"구분자".join(리스트)를 이용하면 리스트의 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문자열로 합쳐줌.  
**"_".join(['a', 'b', 'c']) 라 하면 "a_b_c" 와 같은 형태로**  문자열을 만들어서 반환.
