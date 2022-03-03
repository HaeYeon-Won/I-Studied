# Study 1일차

정리해야하는 사항 
zip, map, join, lambda
- zip
>(1) 기본사용법 
>zip() 함수는 여러 개의 순회 가능한(iterable한) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 튜플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환.
>예제 코드
>1. zip 함수를 사용
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

>2. index를 사용해서 작성
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
>(2) zip() 함수는 여러 개의 순회 가능한(iterable한) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 튜플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환.
