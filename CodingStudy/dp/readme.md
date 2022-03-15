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
