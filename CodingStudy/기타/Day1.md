# Study 1일차

정리해야하는 사항 
zip, map, join, lambda
- zip
>1. 기본사용법 
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

>2. 병렬처리
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

>3. unzip()
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
>4.  사전 변환
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
```
```
```
