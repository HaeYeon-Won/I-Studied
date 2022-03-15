
#  Longest Common Subsequence(LCS)

- 최장 공통 부분수열을 뜻함.
- 문자열 **ABCDEF**와 **GBCDFE** 로 예시를 들어보면
![1](https://user-images.githubusercontent.com/73468962/158317134-2ce2afb9-b9a8-4140-9dd1-68c634f8e309.png)
LCS = "BCDF", "BCDE"
- 점화식
```python
if i == 0 or j == 0:  # 마진 설정
	LCS[i][j] = 0
elif string_A[i] == string_B[j]:
	LCS[i][j] = LCS[i - 1][j - 1] + 1
else:
	LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
```
1.  문자열A, 문자열B의  **한글자씩**  비교해봅니다.
2.  두 문자가  **다르다면  `LCS[i - 1][j]`와  `LCS[i][j - 1]`  중에 큰값을 표시**합니다.
3.  두 문자가  **같다면  `LCS[i - 1][j - 1]`  값을 찾아  `+1`**  합니다.
4.  위 과정을 반복합니다.

# LCS 찾기
- 위에서 LCS 구현과정을 통해 LCS 배열을 만들며 LCS의 길이를 구함. 
- 앞에서 만든 LCS 배열을 이용해 최장 공통 부분수열 탐색. 경우에 따라 여러가지 답이 나올 수 있음.

과정은 아래와 같다.

1.  LCS 배열의  **가장 마지막 값**에서 시작합니다. 결과값을 저장할  `result`  배열을 준비합니다.
2.  `LCS[i - 1][j]`와  `LCS[i][j - 1]`  중 현재 값과 같은 값을 찾습니다.  
    2-1. 만약  **같은 값이 있다면 해당 값으로 이동**합니다.  
    2-2. 만약  **같은 값이 없다면  `result`배열에 해당 문자를 넣고  `LCS[i -1][j - 1]`로 이동**합니다.
3.  2번 과정을 반복하다가 0으로 이동하게 되면 종료합니다.  `result`  배열의 역순이  **LCS**  입니다.

## 구현과정
![image](https://user-images.githubusercontent.com/73468962/158317851-f5620a9a-8c5a-426e-b737-4c3c7346e0cb.png)
![image](https://user-images.githubusercontent.com/73468962/158317885-4f2b87cc-a4ef-401c-b25c-14f56959d62c.png)
![image](https://user-images.githubusercontent.com/73468962/158317965-7733f332-343d-4ae6-ac4e-33bfaba4ba4d.png)
![image](https://user-images.githubusercontent.com/73468962/158320180-07b1ea86-f06b-44ec-9f86-1dd0cf116ca0.png)
![image](https://user-images.githubusercontent.com/73468962/158320204-562e5d38-60fa-4728-a974-8059d0b25890.png)
![image](https://user-images.githubusercontent.com/73468962/158320227-990d7939-ff38-415d-ae88-8b9b4960d03a.png)
![image](https://user-images.githubusercontent.com/73468962/158320300-6dc84f3f-08f3-4f60-a044-9c9761efdf0e.png)
#  Longest Increasing Subsequence(LIS)
- 원소가 n개인 배열의 일부 원소를 골라내서 만든 부분 수열 중, 각 원소가 이전 원소보다 크다는 조건을 만족 + 길이가 최대인 부분 수열을 의미
- 예를 들어, [6,2,5,1,7,4,8,3] -> [2,5,7,8]이 된다.
1. dp를 이용한 풀이 방법
```python
for (int k = 0; k < n; k++)
{
	length[k] = 1;
    for (int i = 0; i < k; i++)
    {
        if(arr[i] < arr[k])
        {
            length[k] = max(length[k], length[i] + 1);
        }        
    }
}
```
하지만 시간 복잡도는 O(N^2)

2. 이분탐색을 이용한 방법
```python
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
	result.append(data[0])
	for i in range(1,n):
		if result[-1]<data[i]:
			result.append(data[i])
		else:#같을때에는 어차피 서치하면 result안에서 해당 위치로 치환되기 때문에 문제없음
			idx = binary_search(len(result), result, data[i]) # 이분탐색하여 해당 숫자가 어디에 들어갈지 결정
			result[idx] = data[i]
	return len(result)

if __name__=="__main__":
	n=int(input())
	data = list(map(int,input().split()))
	print(solution(n, data))
```
시간 복잡도는 O(NlogN)
